from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
#Przekazywanie zmiennych do template html
    name = "Mark" 
    pup_dict = {"pup_name": "Sammy"}
    letters =list(name)                 #my_variable - Nadanie nazwy wlasnej zmiennej ktora bedzie przekazana do html template'a
    return render_template('basic.html', 
                            html_name=name, 
                            html_letters = letters,
                            html_pup_dict = pup_dict) #Flask automatycznie szuka w tym samym katalogtu folderu templates i w nim szuka pliku html w parametrze


if __name__ == '__main__':
    app.run(debug=True)