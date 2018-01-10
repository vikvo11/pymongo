import pymongo
from pymongo import MongoClient
import json
import pymongo
from bson import BSON
from bson import json_util
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,logging #For work with HTTP and templates
import requests # For HTTP requests

client = MongoClient("ds141786.mlab.com:41786", username = 'podarkin', password = 'podarkin', authSource = 'heroku_q51pzrtm')
db = client["heroku_q51pzrtm"]
bookings_coll = db.bookings

app = Flask(__name__)
'''
@app.route('/')
def index():
    #
    #id=doc[-1]['chat_id']
    #flash('id', 'danger')

    return render_template('home.html')
'''
@app.route('/')
def dashbord():
    msg = py()
    #a= py()
    return render_template('dashbordpymongo.html', articles=msg)


def py():
    client = MongoClient("ds141786.mlab.com:41786", username = 'podarkin', password = 'podarkin', authSource = 'heroku_q51pzrtm')
    db = client["heroku_q51pzrtm"]
    bookings_coll = db.bookings
    doc = bookings_coll.find_one()
    asa = json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)
    #id=doc['name']
    docs = bookings_coll.find()
    id = docs[0]['name']
    return docs

def main():
    doc = bookings_coll.find_one()
    #asa = json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)
    #print(asa)
    #a = [x for x in bookings_coll.find()]
    #asa = json.dumps(a, sort_keys=True, indent=4, default=json_util.default)
    #print(asa)

    pass
   # a = [x for x in bookings_coll.find()]


if __name__ == '__main__':
    main()
