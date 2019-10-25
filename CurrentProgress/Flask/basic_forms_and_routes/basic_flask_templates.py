from flask import Flask, render_template


app = Flask(__name__)

# @app.route('/')
# def index():
# #Przekazywanie zmiennych do template html
#     name = "Mark" 
#     pup_dict = {"pup_name": "Sammy"}
#     letters =list(name)                 #my_variable - Nadanie nazwy wlasnej zmiennej ktora bedzie przekazana do html template'a
#     return render_template('basic.html', 
#                             html_name=name, 
#                             html_letters = letters,
#                             html_pup_dict = pup_dict) #Flask automatycznie szuka w tym samym katalogtu folderu templates i w nim szuka pliku html w parametrze

#Control flow example
@app.route('/')
def index():
#Przekazywanie zmiennych do template html
    mylist = [1,2,3,4,5]
    puppies = ['Fluffy', 'Rufus', 'Sparky']
    name = "Mark" 
    pup_dict = {"pup_name": "Sammy"}
    letters =list(name)                 #my_variable - Nadanie nazwy wlasnej zmiennej ktora bedzie przekazana do html template'a
    user_logged_in = False
    return render_template('basic.html', 
                            html_name=name, 
                            html_letters = letters,
                            html_pup_dict = pup_dict,
                            html_mylist = mylist,
                            html_puppies = puppies,
                            html_user_logged_in = user_logged_in) #Flask automatycznie szuka w tym samym katalogtu folderu templates i w nim szuka pliku html w parametrze



if __name__ == '__main__':
    app.run(debug=True)