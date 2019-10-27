# Set up your imports and your flask app.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # This home page should have the form.
    return render_template('home.html')


# This page will be the page after the form
@app.route('/report')
def report():
    #Get arguments from html form when user submits in sing_up.html and press submit
    user_name = request.args.get('name')

    # Check the user name for the 3 requirements.
    has_upper_case = any(c.isupper() for c in user_name)
    has_lower_case = any(c.islower() for c in user_name) 
    is_last_digit = user_name[-1].isdigit()


    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.
    return render_template("report.html",
                            has_upper_case = has_upper_case,
                            has_lower_case = has_lower_case,
                            is_last_digit = is_last_digit
                            )

# Handlowanie bledu gdy wpisze sie jakis nieistniejace route
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
