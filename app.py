"""This area imports the neccessary libraries for this Python file"""
import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import flash

"""Creating an instance of a Flask app and linking it to the MongoDB"""
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Interests_DB'
app.config["MONGO_URI"] = 'mongodb+srv://PIM_Admin:PIM_R00T@interests-cluster-9djrk.mongodb.net/Interests_DB?retryWrites=true&w=majority'

"""Creates an instance of PyMongo with the app inside and sets the default app route"""
mongo = PyMongo(app)

@app.route('/')

@app.route('/login')
def login():
    return render_template('index.html')






"""this route checks the login fields against the Users DB collection and if successful logs in the user 
and redirects to user profile.. if unsuccessful shows message and returns user to index.html"""


@app.route('/user_login', methods=['POST'])
def user_login():
    unhashed_pwd = request.form.get('user_password')
    this_user = request.form.get('user_username')
    if mongo.db.Users.find({"Username": this_user}):
        user = mongo.db.Users.find_one({"Username": this_user})
        if bcrypt.checkpw(unhashed_pwd, user["Password"]):
            return redirect('user_profile.html')
        else:
            flash("Password does not match our records")
            return render_template('index.html')
    else:
        flash("User does not exist in our records")
        return render_template('index.html')













"""these app routes handle the user's pages and functionality"""

"""this app route displays all of the users in the DB Users collection"""
@app.route('/manage_users')
def manage_users():
    return render_template('manage_users.html', Users=mongo.db.Users.find())

"""this app route displays the form for a new user to sign up or for an admin to sign up a new user"""
@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

"""this app route adds the new user from the form 
to the MongoDB Users collection and using bcrypt 
it hashes out the password for security"""
@app.route('/add_user', methods=['POST'])
def add_user():
    Users = mongo.db.Users
    old_password = request.form.get('Password')
    hash_pass = bcrypt.hashpw(old_password.encode("utf-8"), bcrypt.gensalt())
    fields = request.form.to_dict()
    fields['Password'] = hash_pass
    Users.insert_one(fields)
    return redirect(url_for('manage_users'))

"""these app routes allows the user to edit a specific user"""   
@app.route('/edit_user/<user_id>')
def edit_user(user_id):
    this_user = mongo.db.Users.find_one({"_id": ObjectId(user_id)})
    return render_template('edit_user.html', user=this_user)

@app.route('/update_user/<user_id>', methods=['POST'])
def update_user(user_id):
    user = mongo.db.Users
    """for security, we must encrypt the password again using bcrypt for 
    when the users information is updated to a new password and if the field
    is left blank (i.e. not changed) we will pass back the original bcrypted 
    password""" 
    form_password = request.form.get('Password')

    if form_password == "":
        this_user = mongo.db.Users.find_one({"_id": ObjectId(user_id)})
        new_pass = this_user["Password"]
    else:
        new_pass = bcrypt.hashpw(form_password, bcrypt.gensalt())
    
    print(new_pass)

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
        'Password':new_pass,
    })

    

    return redirect(url_for('manage_users'))

"""this app route allows the user to delete a specific user"""
@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.Users.remove({"_id": ObjectId(user_id)})
    return redirect(url_for('manage_users'))

"""this app route allows the user view the profile of the user"""
"""in future versions of this site, this area will be specific for one user.
For this version, it will simply be linked to all of the results in the DB"""
@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html')

"""these app routes handle the film pages and functionality"""

"""this app route loads and displays all results in the 
MongoDB Films collection"""
@app.route('/view_movies')
def view_movies():
    return render_template('my_movies.html', Films=mongo.db.Films.find())

"""this app route displays the form for a new film 
to be added to the Films collection"""
@app.route('/new_film')
def new_film():
    return render_template('add_movie.html')

"""this app route adds the new film from the form 
to the MongoDB Films collection"""
@app.route('/add_film', methods=['POST'])
def add_film():
    new_film = mongo.db.Films
    new_film.insert_one(request.form.to_dict())
    return redirect(url_for('view_movies'))
    
"""these app routes allows the user to edit a specific film"""   
@app.route('/edit_film/<film_id>')
def edit_film(film_id):
    this_film = mongo.db.Films.find_one({"_id": ObjectId(film_id)})
    return render_template('edit_movie.html', film=this_film)

@app.route('/update_film/<film_id>', methods=['POST'])
def update_film(film_id):
    film = mongo.db.Films
    film.update( {'_id': ObjectId(film_id)},
    {
        'Name':request.form.get('Name'),
        'Release_Date':request.form.get('Release_Date'),
        'Director':request.form.get('Director'),
        'Rating':request.form.get('Rating'),
        'Description':request.form.get('Description'),
        'Genre':request.form.get('Genre'),
        'Watched':request.form.get('Watched'),
        'Image':request.form.get('Image'),
    })
    return redirect(url_for('view_movies'))

"""this app route allows the user to delete a specific film"""
@app.route('/delete_film/<film_id>')
def delete_film(film_id):
    mongo.db.Films.remove({"_id": ObjectId(film_id)})
    return redirect(url_for('view_movies'))

"""these app routes handle the tv show pages and functionality"""

"""this app route loads and displays all results in the 
MongoDB TV collection"""
@app.route('/view_tv')
def view_tv():
    return render_template('my_tv_shows.html', TV=mongo.db.TV.find())

"""this app route displays the form for a new tv show 
to be added to the TV collection"""
@app.route('/new_tv_show')
def new_tv_show():
    return render_template('add_tv_show.html')

"""this app route adds the new tv show from the form 
to the MongoDB TV collection"""
@app.route('/add_tv', methods=['POST'])
def add_tv():
    new_tv = mongo.db.TV
    new_tv.insert_one(request.form.to_dict())
    return redirect(url_for('view_tv'))

"""these app routes allows the user to edit a specific TV show"""   
@app.route('/edit_tv/<tv_id>')
def edit_tv(tv_id):
    this_tv = mongo.db.TV.find_one({"_id": ObjectId(tv_id)})
    return render_template('edit_tv_show.html', tv=this_tv)

@app.route('/update_tv/<tv_id>', methods=['POST'])
def update_tv(tv_id):
    tv = mongo.db.TV
    tv.update( {'_id': ObjectId(tv_id)},
    {
        'Name':request.form.get('Name'),
        'Pilot_Date':request.form.get('Pilot_Date'),
        'Director':request.form.get('Director'),
        'Rating':request.form.get('Rating'),
        'Description':request.form.get('Description'),
        'Genre':request.form.get('Genre'),
        'Image':request.form.get('Image'),
    })
    return redirect(url_for('view_tv'))

"""this app route allows the user to delete a specific TV show"""
@app.route('/delete_tv/<tv_id>')
def delete_tv(tv_id):
    mongo.db.TV.remove({"_id": ObjectId(tv_id)})
    return redirect(url_for('view_tv'))

"""these app routes handle the episodes pages and functionality"""

"""this app route loads and displays all results in the 
MongoDB Episodes collection"""
@app.route('/new_episode/<tv_name>')
def new_episode(tv_name):
    return render_template('add_episode.html', show=tv_name)

"""this app route displays the form for a new episode 
to be added to the Episodes collection"""
@app.route('/view_episodes/<tv_name>')
def view_episodes(tv_name):
    this_show = tv_name
    return render_template('my_episodes.html', Episodes=mongo.db.Episodes.find({"Show": tv_name}), show=this_show)

"""this app route adds the new episode from the form 
to the MongoDB Episodes collection"""
@app.route('/add_episode', methods=['POST'])
def add_episode():
    new_episode = mongo.db.Episodes
    new_episode.insert_one(request.form.to_dict())
    show_name = request.form.get('Show')
    return redirect(url_for('view_episodes', tv_name=show_name))

"""these app routes allows the user to edit a specific episode"""   
@app.route('/edit_episode/<episode_id>')
def edit_episode(episode_id):
    this_episode = mongo.db.Episodes.find_one({"_id": ObjectId(episode_id)})
    return render_template('edit_episode.html', episode=this_episode)

@app.route('/update_episode/<episode_id>', methods=['POST'])
def update_episode(episode_id):
    episode = mongo.db.Episodes
    episode.update( {'_id': ObjectId(episode_id)},
    {
        'Name':request.form.get('Name'),
        'Season_Number':request.form.get('Season_Number'),
        'Show':request.form.get('Show'),
        'Air_Date':request.form.get('Air_Date'),
        'Rating':request.form.get('Rating'),
        'Description':request.form.get('Description'),
        'Watched':request.form.get('Watched'),
        'Episode_Number':request.form.get('Episode_Number'),
    })
    show_name = request.form.get('Show')
    return redirect(url_for('view_episodes', tv_name=show_name))

"""this app route allows the user to delete a specific episode"""
@app.route('/delete_episode/<episode_id>/<tv_name>')
def delete_episode(episode_id, tv_name):
    mongo.db.Episodes.remove({"_id": ObjectId(episode_id)})
    return redirect(url_for('view_episodes', tv_name=tv_name))

"""these app routes handle the games pages and functionality"""

"""this app route loads and displays all results in the 
MongoDB Games collection"""
@app.route('/view_games')
def view_games():
    return render_template('my_games.html', Games=mongo.db.Games.find())

"""this app route displays the form for a new game 
to be added to the Games collection"""
@app.route('/new_game')
def new_game():
    return render_template('add_game.html')

"""this app route adds the new game from the form 
to the MongoDB Games collection"""
@app.route('/add_game', methods=['POST'])
def add_game():
    new_game = mongo.db.Games
    new_game.insert_one(request.form.to_dict())
    return redirect(url_for('view_games'))

"""these app routes allows the user to edit a specific game"""   
@app.route('/edit_game/<game_id>')
def edit_game(game_id):
    this_game = mongo.db.Games.find_one({"_id": ObjectId(game_id)})
    return render_template('edit_game.html', game=this_game)

@app.route('/update_game/<game_id>', methods=['POST'])
def update_game(game_id):
    game = mongo.db.Games
    game.update( {'_id': ObjectId(game_id)},
    {
        'Game_Name':request.form.get('Game_Name'),
        'Console':request.form.get('Console'),
        'Rating':request.form.get('Rating'),
        'Description':request.form.get('Description'),
        'Image':request.form.get('Image'),
    })
    return redirect(url_for('view_games'))

"""this app route allows the user to delete a specific game"""
@app.route('/delete_game/<game_id>')
def delete_game(game_id):
    mongo.db.Games.remove({"_id": ObjectId(game_id)})
    return redirect(url_for('view_games'))

"""these app routes handle the quests pages and functionality"""

"""this app route loads and displays all results in the 
MongoDB Quests collection"""
@app.route('/view_quests/<game_name>')
def view_quests(game_name):
    this_game = game_name
    return render_template('my_quests.html', Quests=mongo.db.Quests.find({"Game": game_name}), game=this_game)

"""this app route displays the form for a new quest 
to be added to the Quests collection"""
@app.route('/new_quest/<game_name>')
def new_quest(game_name):
    return render_template('add_quest.html', game=game_name)

"""this app route adds the new quest from the form 
to the MongoDB Quests collection"""
@app.route('/add_quest', methods=['POST'])
def add_quest():
    new_quest = mongo.db.Quests
    quest = request.form.to_dict()
    print(quest)
    new_quest.insert_one(quest) 
    game_name = request.form.get('Game')
    return redirect(url_for('view_quests', game_name=game_name))

"""these app routes allows the user to edit a specific quest"""   
@app.route('/edit_quest/<quest_id>')
def edit_quest(quest_id):
    this_quest = mongo.db.Quests.find_one({"_id": ObjectId(quest_id)})
    return render_template('edit_quest.html', quest=this_quest)

@app.route('/update_quest/<quest_id>', methods=['POST'])
def update_quest(quest_id):
    quest = mongo.db.Quests
    quest.update( {'_id': ObjectId(quest_id)},
    {
        'Game':request.form.get('Game'),
        'Quest_Name':request.form.get('Quest_Name'),
        'Description':request.form.get('Description'),
        'Active_Quest':request.form.get('Active_Quest'),
        'Completed':request.form.get('Completed'),
        'Rec_Level':request.form.get('Rec_Level'),
    })
    game_name = request.form.get('Game')
    return redirect(url_for('view_quests', game_name=game_name))

"""this app route allows the user to delete a specific quest"""
@app.route('/delete_quest/<quest_id>/<game_name>')
def delete_quest(quest_id, game_name):
    mongo.db.Quests.remove({"_id": ObjectId(quest_id)})
    return redirect(url_for('view_quests', game_name=game_name))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)