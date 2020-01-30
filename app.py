import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] =  'Personal_Interest_Manager'
app.config["MONGO_URI"] =  'mongodb+srv://PIM_Admin:PIM_R00T@interests-cluster-9djrk.mongodb.net/Personal_Interest_Manager?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
@app.route('/manage_users')
def manage_users():
    return render_template('manage_users.html', user=mongo.db.users.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) 

