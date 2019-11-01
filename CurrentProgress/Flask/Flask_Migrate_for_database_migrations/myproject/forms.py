from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
# Validatory to pol formularza, czyli sprawdzanie czy wpisywaniy jest mail, wymaganie danych w formularzu, etc
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Log in")


class RegistrationForm(FlaskForm):

    email = StringField(label="Email", validators=[Email(), DataRequired()])
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField('Passwird', validators=[DataRequired(), EqualTo('pass_confirm', message="Passwords must match!")]) #to ma sie rownac pass_confirm
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField(label='Register!')


    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has been already registered")

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is taken!')