#!flask/bin/python
from travel import app
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension

if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = '<replace with a secret key>'

    toolbar = DebugToolbarExtension(app)
    app.run()
