import os
import re

import jinja2
from flask import Flask, redirect, request, url_for

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

signup_form = jinja_env.get_template('signup_form.html')
success = jinja_env.get_template('success.html')


@app.route('/')
@app.route('/index')
def index():
    return signup_form.render()


def is_valid(usr_inpt):
    if re.match("^[A-Za-z0-9_\S]{3,20}$", usr_inpt):
        return True
    else:
        return False


@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def verify_input():

    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']

    username_error = ''
    password_error = ''
    password2_error = ''
    email_error = ''

    if username == '' or not is_valid(username):
        username_error = 'Not a valid username'

    if password == '' or not is_valid(password):
        password_error = 'Not a valid password'
        password = ''
        password2 = ''

    if password != password2:
        password2_error = "Passwords don't match"
        password = ''
        password2 = ''

    if email != '':
        if ' ' in email or "@" not in email or ".com" not in email:
            email_error = 'Not a valid email address'

    if not username_error and not password_error and not \
            password2_error and not email_error:
        return redirect(url_for('confirm'), code=307)

    else:
        return signup_form.render(
            username_error=username_error,
            password_error=password_error,
            password2_error=password2_error,
            email_error=email_error,
            username=username,
            password=password,
            password2=password2,
            email=email)


@app.route('/confirm', methods=['POST'])
def confirm():
    return success.render()


app.run()
