from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_form.html')

@app.route('/signup_form')
def signup_form():
   return render_template('sign_up.html')

@app.route('/thank_you')
def thank_you():
    #Get arguments from html form when user submits in sing_up.html and press submit
   first = request.args.get('first')
   last = request.args.get('last')

   return render_template('thankyou.html',
                            html_first = first,
                            html_last = last)


if __name__ == '__main__':
    app.run()