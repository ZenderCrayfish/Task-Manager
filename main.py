from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)
app.config['DEBUG'] = True

from google.appengine.api import users

import os

USER = users.get_current_user()

@app.route('/')
def index ():
	global USER
	USER = users.get_current_user()
	if USER:
		return redirect(url_for('home'))
	else:
		return redirect(users.create_login_url( url_for('index') ))

@app.route('/home')
def home():
	return render_template('home.tmpl', user=USER)

@app.errorhandler(404)
def page_not_found (e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
