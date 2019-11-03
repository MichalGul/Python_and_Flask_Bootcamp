#Setup db inside the __init__.py under mypfoject folder

from myproject import db


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