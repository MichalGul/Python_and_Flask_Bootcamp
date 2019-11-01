import os
#Setup locac Oauth (only used when local usage)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
                #Jest jeszcze wiecej parametrow, check docks for google blueprint
blueprint = make_google_blueprint(client_id='72342792172-gf05qu427i264t09u46qb32mi6c7s7ep.apps.googleusercontent.com',
                                     client_secret='hxAWgDxNWkBgeWj9lWoi-ITc', 
                                     offline=True,
                                     scope=['profile', 'email'])


app.register_blueprint(blueprint, url_prefix='/login') #idz odrazu do nowej strony po zalogowaniu googlem

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/welcome')
def welcome():
    # Return ERROR INTERNAL SERVER ERROR IF NOT LOGGED IN!!
    # Just for example
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email'] # pobranie adresu email od kogos kto sie zalogowal

    return render_template('welcome.html', email=email)


@app.route("/login/google")
def login():
    if not google.authorized:
        return render_template(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("welcome.html",email=email)


if __name__ == "__main__":
    app.run()


