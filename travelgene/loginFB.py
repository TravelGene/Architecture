__author__ = 'zhiyuel'

from travelgene import *

from flask import Flask, render_template, session, redirect, url_for, escape, request
import json
from pymongo import MongoClient
import pymongo
import flask_debugtoolbar
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.cors import CORS
from flask.ext.pymongo import PyMongo


FACEBOOK_APP_ID='1596233553958439'
FACEBOOK_APP_SECRET='6538bd24923ec5c0b4c126419ed0edd3'

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'user_posts,user_friends,public_profile,email,user_likes'},
    access_token_method="GET"
)

@app.route('/test1.html')
def test1():
    print 'test1.html'
    return render_template('test1.html')

# @app.route('/blog/add/ajax', methods=['POST', 'GET'])
# def add_blog_ajax():
#     if request.method == 'POST':
#         title = request.json['title']
#         article = request.json['article']
#         # blog = Blog(title, article)
#         # db.session.add(blog)
#         # db.session.commit()
#         # return jsonify(title=title, article=article)
#         print title
#         print article
#         return redirect(url_for("home_page"))


@app.route('/fb.html')
def testfb():
    print 'nnnnnn'
    if session.has_key('oauth_token'):
        print "already has.."
        del session['oauth_token']
    # del get_facebook_oauth_token
    # return redirect('test1.html')
    print request.args.get('next')
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))

@app.route('/fblogin/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    print 'authorize'
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    session['logged_in'] = True
    me = facebook.get('/me')
    friends=facebook.get('/me/taggable_friends')
    friendlists = map(lambda x: (x['name'], x['id'],x['picture']), friends.data['data'])
    print friendlists[0][2]['data']['url']
    print "####"
    print

    print 'Logged in as id=%s name=%s redirect=%s' % \
        (me.data['id'], me.data['name'], request.args.get('next'))

    # print request.args.get('next')
    return redirect(url_for("home_page"))

@app.route('/logout')
def logout():
    """Logout the user"""
    session.pop('logged_in', None)
    session.pop('oauth_token', None)
    return redirect(url_for('index'))

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

# def login_required(f):
#     """Decorator"""
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if g.user is None:
#             return redirect(url_for('login', next=request.url))
#         return f(*args, **kwargs)
#     return decorated_function
#
#
# @app.before_request
# def before_request():
#     g.user = None
#     g.conn, g.db = connect_db()
#     if 'oauth_token' in session:
#         g.user = facebook.get('/me').data
#
#
# @app.teardown_request
# def teardown_request(exception):
#     g.conn.close()
#
#
# def connect_db():
#     conn = Connection()
#     db = conn.FB
#     return conn, db
#
#
#
# @app.route('/login/authorized')
# @facebook.authorized_handler
# def facebook_authorized(resp):
#     """Authorize Facebook login"""
#     next_url = request.args.get('next') or url_for('index')
#     if resp is None or 'access_token' not in resp:
#         return 'Access denied: reason=%s error=%s' % (request.args['error_reason'], request.args['error_description'])
#
#     session['logged_in'] = True
#     session['oauth_token'] = (resp['access_token'], '')
#
#     return redirect(next_url)
#
#
# @facebook.tokengetter
# def get_facebook_oauth_token():
#     return session.get('oauth_token')
#
