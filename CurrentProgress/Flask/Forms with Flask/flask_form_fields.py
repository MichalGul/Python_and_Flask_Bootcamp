from flask import Flask, redirect, render_template, session, url_for
from flask_wtf import FlaskForm
from wtforms import (BooleanField, DateTimeField, RadioField, SelectField,
                     StringField, SubmitField, TextAreaField, TextField)

# do sprawdzania zawatosci danych
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

#Przygotowanie formularza+
class InfoForm(FlaskForm):

    #Rozne kontolki dla formularza
    breed = StringField(label="What breed are you?", validators=[DataRequired()])
    neutered = BooleanField(label="Have you benn neutered?")
    mood = RadioField('Please choose your mood:',
                        choices=[('mood_one', "Happy"), ('mood_two', "Excited")])

    food_choice = SelectField(u'Pick your favorite food:', 
                                choices=[('chi', 'Chicken'), ('bf','Beef'),
                                        ('fish', 'Fish') ])
    
    feedback = TextAreaField()

    submit = SubmitField('Submit')




@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit(): # Gdy nacisniety guzik
        #Zapisywanie danych z formularza w obiekcie sesji (aktywne tylko podczas polaczenia uzytkownika z serwerem 
        # (gdy wchodzi i sie loguje, dane sa ulotne))
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        #Przekierowanie bezpośrednio z formlularza do innego view a nie przez html
        return redirect(url_for('thankyou'))


    return render_template('index_fields.html', form=form)


@app.route('/thankyou')
def thankyou():
   return render_template('thankyou.html')



if __name__ == '__main__':
    app.run(debug=True)
