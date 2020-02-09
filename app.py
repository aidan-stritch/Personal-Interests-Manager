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

@app.route('/login')
def login():
    return render_template('index.html')

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html')

@app.route('/manage_users')
def manage_users():
    return render_template('manage_users.html', Users=mongo.db.Users.find())

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')
    
"""this route checks the login fields against the users DB and if successful logs in the user 
and redirects to user profile.. if unsuccessful shows message and returns user to index.html"""
@app.route('/user_login')
    def user_login():
    return render_template('index.html')

"""this app route adds the new user from the form 
to the MongoDB Users collection"""
@app.route('/add_user', methods=['POST'])
def add_user():
    Users = mongo.db.Users
    Users.insert_one(request.form.to_dict())
    return redirect(url_for('manage_users'))

"""these app routes allows the user to edit a specific user"""   
@app.route('/edit_user/<user_id>')
def edit_user(user_id):
    this_user = mongo.db.Users.find_one({"_id": ObjectId(user_id)})
    return render_template('edit_user.html', user=this_user)

@app.route('/update_user/<user_id>', methods=['POST'])
def update_user(user_id):
    user = mongo.db.Users
    user.update( {'_id': ObjectId(user_id)},
    {
        'First_Name':request.form.get('First_Name'),
        'Last_Name':request.form.get('Last_Name'),
        'Address_Line_1':request.form.get('Address_Line_1'),
        'Address_Line_2':request.form.get('Address_Line_2'),
        'Address_Line_3':request.form.get('Address_Line_3'),
        'City':request.form.get('City'),
        'Postcode':request.form.get('Postcode'),
        'Phone':request.form.get('Phone'),
        'Email':request.form.get('Email'),
        'Username':request.form.get('Username'),
        'Password':request.form.get('Password'),
    })
    return redirect(url_for('manage_users'))

"""this app route allows the user to delete a specific user"""
@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.Users.remove({"_id": ObjectId(user_id)})
    return redirect(url_for('manage_users'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
