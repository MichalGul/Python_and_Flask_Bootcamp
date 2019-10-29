import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #Do zmian w bazach danych z zewnatrz a nie w kodzie pythona za kazdym razem

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Polaczanie aplikacji z baza danych do wykonywania migracji
Migrate(app, db)

##################################################
#Stworzenie modelu -> tabeli bazy danych
class Puppy(db.Model):

    #Manual table name choice! (optional)
    __tablename__ = "puppies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)


    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f"Puppy {self.name} i {self.age} year/s old"

        