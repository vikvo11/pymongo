import pymongo
from pymongo import MongoClient
import json
import pymongo
from bson import BSON
from bson import json_util
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,logging #For work with HTTP and templates
import requests # For HTTP requests
from functools import wraps # For lock access
from HTTP_basic_Auth import auths # For lock access

client = MongoClient("ds141786.mlab.com:41786", username = 'podarkin', password = 'podarkin', authSource = 'heroku_q51pzrtm')
db = client["heroku_q51pzrtm"]
bookings_coll = db.bookings

app = Flask(__name__)
app.config['SECRET_KEY'] = 'morkovka18'
#Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            #flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('test'))
    return wrap

@app.route('/')
def home():
    #msg = py()
    #a= py()
    return redirect(url_for('index'))

@app.route('/index')
def dashbord():
    msg = py()
    #a= py()
    return render_template('dashbordpymongo.html', articles=msg)
@app.route('/test')
def test():
    msg = py()
    return render_template('home.html', articles=msg)
#User Login
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #Get Form fields
        username = request.form['username']
        password_candidate = request.form['password']
        #users=auths()
        if auths(username,password_candidate):
            session['logged_in']= True
            return redirect(url_for('index'))
        else:
                error='Invalid login'
                return render_template('login.html',error=error)

    return render_template('login.html')

def py():
    client = MongoClient("ds141786.mlab.com:41786", username = 'podarkin', password = 'podarkin', authSource = 'heroku_q51pzrtm')
    db = client["heroku_q51pzrtm"]
    bookings_coll = db.bookings
    doc = bookings_coll.find_one()
    asa = json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)
    docs = bookings_coll.find()
    id = docs[0]['name']
    return docs

def main():
    doc = bookings_coll.find_one()


    pass
   # a = [x for x in bookings_coll.find()]


if __name__ == '__main__':
    main()
