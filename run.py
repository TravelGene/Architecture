#!flask/bin/python
from travelgene import app
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension

if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = '<replace with a secret key>'
    #
    # toolbar = DebugToolbarExtension(app)
    #
    # toolbar.DEBUG_TB_INTERCEPT_REDIRECTS=False
    app.run()
