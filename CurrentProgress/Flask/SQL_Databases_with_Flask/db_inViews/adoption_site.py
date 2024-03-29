import os
from forms import AddForm, DelForm, OwnerForm
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# this allows use forms in our application
app.config['SECRET_KEY'] = 'mysecretkey'

#setup database
#############################
### SQL DATABASE SECTION ####
#############################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

#Create models --> sql tables
############################
### MODELS #################
############################

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    
    # ONE TO ONE
    # ONE PUPPY <----> ONE OWNER
    owner = db.relationship("Owner", backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"{self.id}. Puppy name: {self.name} and have owner {self.owner}!" 
        else:
            return f"Puppy name: {self.name} and have no owner yet!"


class Owner(db.Model):

    __tablename__ = 'owners'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))


    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner Name: {self.name}"



###################################
### VIEW FUNCTIONS -- HAVE FORMS ##
###################################

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
   
    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data

        #Add data from form to database table
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html', form=form)


@app.route('/list')
def list_pup():
    
    #Get all pupues from database
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
        
    return render_template('delete.html', form=form)



@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():

    form = OwnerForm()

    if form.validate_on_submit():

        owner_name = form.name.data
        puppy_id = form.id_puppy.data

        new_owner = Owner(owner_name, puppy_id)
        db.session.add(new_owner)
        db.session.commit()

        flash(f"You have just added new Owner named: {owner_name} to puppy {puppy_id}!")

        return redirect(url_for('list_pup'))

    return render_template('add_owner.html', form=form)


if __name__ == "__main__":
    app.run(debug = True)


