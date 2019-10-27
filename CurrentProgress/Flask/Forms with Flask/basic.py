from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

#Add secret key for forms (passing data etc.)
app.config['SECRET_KEY'] = 'mysecretkey' #Bedzie lepszy sposob pozniej

#Stworzenie formularza
class InfoFrom(FlaskForm):

    breed = StringField(label="What Breed are you?") # Miejsce na stringa
    submit = SubmitField(label="Submit") #Summit button
                #GET POST pozwalaja na przesylanie danych z formularza
@app.route('/', methods=['GET', 'POST'])
def index():
   
    breed = False

    form = InfoFrom()
        #Funkcja wywoluwana gdy formularz jest dobrze wypelniony i przeslany
    if form.validate_on_submit():

        breed = form.breed.data # Read data from form
        form.breed.data = " " # Refresh data in form

    return render_template('index.html', form = form, breed = breed)


if __name__ == '__main__':
    app.run(debug=True)


