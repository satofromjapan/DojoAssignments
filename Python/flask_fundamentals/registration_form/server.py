from flask import Flask, flash, redirect, request, render_template, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'thesecret'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def register():
    if len(request.form['email']) < 1:
        flash('Email cannot be blank!')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address! Please enter a valid email.')
    elif len(request.form['first_name'])<1:
        flash('First name required!')
    elif request.form['first_name'].isalpha() != True:
        flash('First name can only be alphabetic characters.')
    elif len(request.form['last_name'])<1:
        flash('Last name required!')
    elif request.form['last_name'].isalpha() != True:
        flash('Last name can only be alphabetic characters.')
    elif (any(x.isupper() for x in request.form['password']) != True and any(x.isdigit() for x in request.form['password']) != True):
        flash('Password must contain at least one uppercase letter and one number.')
    elif request.form['confirm_password'] != request.form['password']:
        flash('Password and confirm password must be the same.')
    else:
        flash('Thanks for submitting your information!')
    return redirect('/')

app.run(debug=True)
