from myproject import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user

from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def home():
   return render_template('home.html')

#Ekran powitania po zalogowaniu
@app.route('/welcome')
@login_required #Zeby widziec ten view uzytkownik musi byc zalogowany, jezeli nie jest zalogowany to przekieruje na strone logowania
def welcome_user():
   return render_template('welcome_user.html')

# Ekran log out
@app.route('/logout')
@login_required
def logout():
   logout_user()
   flash("You are logged out!")
   return redirect(url_for('home'))

# Logowanie usera
@app.route('/login', methods=['GET', 'POST'])
def login():

   form = LoginForm()

   if form.validate_on_submit():

      user = User.query.filter_by(email=form.email.data).first()

      if user.check_password(form.password.data) and user is not None:
         #logowanie usera metoda z flaska
         login_user(user)
         flash('Logged in Successfully!')

         # If a user was trying to visit a page that requires a login
         # flask saves that URL as 'next'.
         next = request.args.get('next')

         # So let's now check if that next exists, otherwise we'll go to
         # the welcome page.
         if next == None or not next[0]=='/':
            next = url_for('welcome_user')

         return redirect(next)

      #przy pierwszym odwiedzeniu strony
   return render_template('login.html', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():

   form = RegistrationForm()
   if form.validate_on_submit():

      user = User(email = form.email.data,
                  username = form.username.data,
                  password = form.password.data)

      db.session.add(user)
      db.session.commit()

      flash('Thanks for registration')
      return redirect(url_for('login'))

   return render_template('register.html', form=form)


if __name__ == '__main__':
   app.run(debug=True)
