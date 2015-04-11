from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

import os
import jinja2

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

@app.route('/')
def index():
    template = JINJA_ENV.get_template('templates/index.tmpl');
    return template.render();


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
