"""This area imports the neccessary libraries for this Python file"""
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

"""Creating an instance of a Flask app and linking it to the MongoDB"""
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Interests_DB'
app.config["MONGO_URI"] = 'mongodb+srv://PIM_Admin:PIM_R00T@interests-cluster-9djrk.mongodb.net/Interests_DB?retryWrites=true&w=majority'

"""Creates an instance of PyMongo with the app inside"""
mongo = PyMongo(app)

"""Creating our app routes"""
@app.route('/')
@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')
@app.route('/add_user', methods=['POST'])
def add_user():
    Users = mongo.db.Users
    Users.insert_one(request.form.to_dict())
    return redirect(url_for('manage_users'))

@app.route('/manage_users')
def manage_users():
    return render_template('manage_users.html', Users=mongo.db.Users.find())



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
