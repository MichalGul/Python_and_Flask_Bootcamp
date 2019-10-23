from flask import Flask
from flask import request

#Stworzenie instancji Flaska dla tego skryptu, ktory bedzie traktowany jako wyjsciowy do innych plikow/stron
app = Flask(__name__)

@app.route('/') #routowanie do innych stron pojedynczy slash to home page czyli do localhosta eq. #127.0.0.1:5000
def index(): #tu bedzie mozna przekazywac/generowac cale strony html
   return "<h1>Hello Puppy! Go to /puppy_latin/name to see your name in puppy latin!</h1>"


#Przyklady multiple routingu

@app.route('/information') #127.0.0.1:5000/information
def info(): #tzw view function
    return "<h1>Puppers are the best!</h1>"

#Dynamic route
@app.route('/puppy/<name>') #name mozna podac dynamicznie w nazwie strony
def puppy(name):
   return "<h1>100th leter: {}</h1>".format(name[100])


#Routing excesise puppy_latin

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    latin_name = ""
    if name[-1] != 'y':
       latin_name = name + 'y'
    else:
        latin_name = name[:-1] + 'iful'
    return "<h1>Hi {} ! Your puppylatin name is {} </h1>".format(name, latin_name)


if __name__ == '__main__':
    app.run(debug=True) #Odpalenie serwera/applikacji