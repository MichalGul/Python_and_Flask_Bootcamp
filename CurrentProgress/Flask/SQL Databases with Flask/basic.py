import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__)) # __file__ nazwa pliku 

app = Flask(__name__)

#STWORZENIE BAZY DANYCH
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///' + os.path.join(basedir, 'data.sqlite') #Sets database location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


##################################################
#Stworzenie modelu -> tabeli bazy danych
class Puppy(db.Model):

    #Manual table name choice! (optional)
    __tablename__ = "puppies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy {self.name} i {self.age} year/s old"

        