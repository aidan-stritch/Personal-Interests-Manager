import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

"""this is a comment"""
app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Interests_DB'
app.config["MONGO_URI"] = 'mongodb+srv://PIM_Admin:PIM_R00T@interests-cluster-9djrk.mongodb.net/Interests_DB?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
@app.route('/manage_users')
def manage_users():
    user_name = mongo.db.Users.find({"First_Name": "Aidan"})
    print(user_name)
    return render_template('manage_users.html', Users=mongo.db.Users.find())
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)