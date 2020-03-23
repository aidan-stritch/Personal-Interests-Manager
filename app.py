"""This area imports the neccessary libraries for this Python
files functionality"""
import os
import bcrypt
from flask import Flask, render_template, redirect, request
from flask import url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user
from flask_login import current_user, logout_user
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

"""creates a class for user that extends UserMixin so that we can use this
class when loging in a user in user_login"""


class User(UserMixin):
    def __init__(self, logged_user):
        self.logged_user = logged_user

    def get_id(self):
        object_id = self.logged_user.get('_id')
        return str(object_id)


@login_manager.user_loader
def load_user(user_id):
    users = mongo.db.Users
    logged_user = users.find_one({'_id': ObjectId(user_id)})
    return User(logged_user)


@app.route('/')


@app.route('/login')
def login():
    return render_template('index.html')


@app.route('/user_login', methods=['POST'])
def user_login():
    form_pwd = request.form.get('user_password')
    form_username = request.form.get('user_username')

    unhashed_pwd = form_pwd.strip()
    this_user = form_username.strip()

    user_log = mongo.db.Users.find_one({"Username": this_user})
    if user_log:
        if bcrypt.check_password_hash(user_log["Password"], unhashed_pwd):
            loginuser = User(user_log)
            login_user(loginuser, remember=True)
            session['user'] = this_user
            return redirect(url_for('user_profile'))
        else:
            flash('The login credentials do not match our records')
            flash('(Note: username and password are case sensitive)')

    else:
        flash('The login credentials do not match our records')
        flash('(Note: username and password are case sensitive)')
    return render_template('index.html')


@app.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')


@app.route('/manage_users')
def manage_users():
    """this IF statement redirects the user to the login page if they have not
    already logged in"""
    if current_user.is_authenticated:
        return render_template('manage_users.html',
                               Users=mongo.db.Users.find())
    else:
        flash('Please login to view this page')
        return render_template('index.html')


@app.route('/new_user')
def new_user():
    return render_template('add_user.html')


@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


"""this app route adds the new user from the form
to the MongoDB Users collection and using bcrypt
it hashes out the password for security"""


@app.route('/add_user', methods=['POST'])
def add_user():
    Users = mongo.db.Users
    form_password = request.form.get('Password')
    hash_pass = bcrypt.generate_password_hash(form_password).decode('utf-8')
    fields = request.form.to_dict()
    fields['Password'] = hash_pass
    Users.insert_one(fields)
    """if the user is authenticated then they are brought back to the
    manage_user's page and if not they are logged in and redirected
    to their user profile"""
    if current_user.is_authenticated:
        flash('Successfully created new user')
        return redirect(url_for('manage_users'))
    else:
        form_user = request.form.get('Username')
        new_user = Users.find_one({"Username": form_user})
        loginuser = User(new_user)
        login_user(loginuser, remember=True)
        form_user = request.form.get('Username')
        session['user'] = form_user
        flash('Successfully created account!')

    return redirect(url_for('user_profile'))


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
        new_pass = bcrypt.generate_password_hash(form_password).decode('utf-8')

    user.update({'_id': ObjectId(user_id)},
                {
                    'First_Name': request.form.get('First_Name'),
                    'Last_Name': request.form.get('Last_Name'),
                    'Address_Line_1': request.form.get('Address_Line_1'),
                    'Address_Line_2': request.form.get('Address_Line_2'),
                    'Address_Line_3': request.form.get('Address_Line_3'),
                    'City': request.form.get('City'),
                    'Postcode': request.form.get('Postcode'),
                    'Phone': request.form.get('Phone'),
                    'Email': request.form.get('Email'),
                    'Username': request.form.get('Username'),
                    'Password': new_pass,
                })
    flash('User profile successfully updated')
    return redirect(url_for('manage_users'))


@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.Users.remove({"_id": ObjectId(user_id)})
    flash('User successfully deleted')
    return redirect(url_for('manage_users'))


@app.route('/user_profile')
def user_profile():
    """this IF statement redirects the user to the login page if they have not
    already logged in"""
    if current_user.is_authenticated:
        return render_template('user_profile.html')
    else:
        flash('Please login to view this page')
        return render_template('index.html')


@app.route('/view_movies')
def view_movies():
    return render_template('my_movies.html', Films=mongo.db.Films.find())


@app.route('/new_film')
def new_film():
    return render_template('add_movie.html')


@app.route('/add_film', methods=['POST'])
def add_film():
    new_film = mongo.db.Films
    new_film.insert_one(request.form.to_dict())
    flash('Successfully added new film')
    return redirect(url_for('view_movies'))


@app.route('/edit_film/<film_id>')
def edit_film(film_id):
    this_film = mongo.db.Films.find_one({"_id": ObjectId(film_id)})
    return render_template('edit_movie.html', film=this_film)


@app.route('/update_film/<film_id>', methods=['POST'])
def update_film(film_id):
    film = mongo.db.Films
    film.update({'_id': ObjectId(film_id)},
                {
                'Name': request.form.get('Name'),
                'Release_Date': request.form.get('Release_Date'),
                'Director': request.form.get('Director'),
                'Rating': request.form.get('Rating'),
                'Description': request.form.get('Description'),
                'Genre': request.form.get('Genre'),
                'Watched': request.form.get('Watched'),
                'Image': request.form.get('Image'),
                })
    flash('Successfully edited film')
    return redirect(url_for('view_movies'))


@app.route('/delete_film/<film_id>')
def delete_film(film_id):
    mongo.db.Films.remove({"_id": ObjectId(film_id)})
    flash('Successfully deleted film')
    return redirect(url_for('view_movies'))


@app.route('/view_tv')
def view_tv():
    return render_template('my_tv_shows.html', TV=mongo.db.TV.find())


@app.route('/new_tv_show')
def new_tv_show():
    return render_template('add_tv_show.html')


@app.route('/add_tv', methods=['POST'])
def add_tv():
    new_tv = mongo.db.TV
    new_tv.insert_one(request.form.to_dict())
    flash('Successfully added new TV Show')
    return redirect(url_for('view_tv'))


@app.route('/edit_tv/<tv_id>')
def edit_tv(tv_id):
    this_tv = mongo.db.TV.find_one({"_id": ObjectId(tv_id)})
    return render_template('edit_tv_show.html', tv=this_tv)


@app.route('/update_tv/<tv_id>', methods=['POST'])
def update_tv(tv_id):
    tv = mongo.db.TV
    tv.update({'_id': ObjectId(tv_id)},
              {
              'Name': request.form.get('Name'),
              'Pilot_Date': request.form.get('Pilot_Date'),
              'Director': request.form.get('Director'),
              'Rating': request.form.get('Rating'),
              'Description': request.form.get('Description'),
              'Genre': request.form.get('Genre'),
              'Image': request.form.get('Image'),
              })
    flash('Successfully edited TV Show')
    return redirect(url_for('view_tv'))


@app.route('/delete_tv/<tv_id>')
def delete_tv(tv_id):
    mongo.db.TV.remove({"_id": ObjectId(tv_id)})
    flash('Successfully deleted TV Show')
    return redirect(url_for('view_tv'))


@app.route('/new_episode/<tv_name>')
def new_episode(tv_name):
    return render_template('add_episode.html', show=tv_name)


@app.route('/view_episodes/<tv_name>')
def view_episodes(tv_name):
    this_show = tv_name
    return render_template('my_episodes.html', Episodes=mongo.db.Episodes.find
                           ({"Show": tv_name}), show=this_show)


@app.route('/add_episode', methods=['POST'])
def add_episode():
    new_episode = mongo.db.Episodes
    new_episode.insert_one(request.form.to_dict())
    show_name = request.form.get('Show')
    flash('Successfully added new episode')
    return redirect(url_for('view_episodes', tv_name=show_name))


@app.route('/edit_episode/<episode_id>')
def edit_episode(episode_id):
    this_episode = mongo.db.Episodes.find_one({"_id": ObjectId(episode_id)})
    return render_template('edit_episode.html', episode=this_episode)


@app.route('/update_episode/<episode_id>', methods=['POST'])
def update_episode(episode_id):
    episode = mongo.db.Episodes
    episode.update({'_id': ObjectId(episode_id)},
                   {
                    'Name': request.form.get('Name'),
                    'Season_Number': request.form.get('Season_Number'),
                    'Show': request.form.get('Show'),
                    'Air_Date': request.form.get('Air_Date'),
                    'Rating': request.form.get('Rating'),
                    'Description': request.form.get('Description'),
                    'Watched': request.form.get('Watched'),
                    'Episode_Number': request.form.get('Episode_Number'),
                })
    show_name = request.form.get('Show')
    flash('Successfully edited episode')
    return redirect(url_for('view_episodes', tv_name=show_name))


@app.route('/delete_episode/<episode_id>/<tv_name>')
def delete_episode(episode_id, tv_name):
    mongo.db.Episodes.remove({"_id": ObjectId(episode_id)})
    flash('Successfully deleted episode')
    return redirect(url_for('view_episodes', tv_name=tv_name))


@app.route('/view_games')
def view_games():
    return render_template('my_games.html', Games=mongo.db.Games.find())


@app.route('/new_game')
def new_game():
    return render_template('add_game.html')


@app.route('/add_game', methods=['POST'])
def add_game():
    new_game = mongo.db.Games
    new_game.insert_one(request.form.to_dict())
    flash('Successfully added new game')
    return redirect(url_for('view_games'))


@app.route('/edit_game/<game_id>')
def edit_game(game_id):
    this_game = mongo.db.Games.find_one({"_id": ObjectId(game_id)})
    return render_template('edit_game.html', game=this_game)


@app.route('/update_game/<game_id>', methods=['POST'])
def update_game(game_id):
    game = mongo.db.Games
    game.update({'_id': ObjectId(game_id)},
                {
                    'Game_Name': request.form.get('Game_Name'),
                    'Console': request.form.get('Console'),
                    'Rating': request.form.get('Rating'),
                    'Description': request.form.get('Description'),
                    'Image': request.form.get('Image'),
                })
    flash('Successfully edited game')
    return redirect(url_for('view_games'))


@app.route('/delete_game/<game_id>')
def delete_game(game_id):
    mongo.db.Games.remove({"_id": ObjectId(game_id)})
    flash('Successfully deleted game')
    return redirect(url_for('view_games'))


@app.route('/view_quests/<game_name>')
def view_quests(game_name):
    this_game = game_name
    return render_template('my_quests.html', Quests=mongo.db.Quests.find
                           ({"Game": game_name}), game=this_game)


@app.route('/new_quest/<game_name>')
def new_quest(game_name):
    return render_template('add_quest.html', game=game_name)


@app.route('/add_quest', methods=['POST'])
def add_quest():
    new_quest = mongo.db.Quests
    quest = request.form.to_dict()
    print(quest)
    new_quest.insert_one(quest)
    game_name = request.form.get('Game')
    flash('Successfully added new quest')
    return redirect(url_for('view_quests', game_name=game_name))


@app.route('/edit_quest/<quest_id>')
def edit_quest(quest_id):
    this_quest = mongo.db.Quests.find_one({"_id": ObjectId(quest_id)})
    return render_template('edit_quest.html', quest=this_quest)


@app.route('/update_quest/<quest_id>', methods=['POST'])
def update_quest(quest_id):
    quest = mongo.db.Quests
    quest.update({'_id': ObjectId(quest_id)},
                 {
                    'Game': request.form.get('Game'),
                    'Quest_Name': request.form.get('Quest_Name'),
                    'Description': request.form.get('Description'),
                    'Active_Quest': request.form.get('Active_Quest'),
                    'Completed': request.form.get('Completed'),
                    'Rec_Level': request.form.get('Rec_Level'),
                })
    game_name = request.form.get('Game')
    flash('Successfully edited quest')
    return redirect(url_for('view_quests', game_name=game_name))


@app.route('/delete_quest/<quest_id>/<game_name>')
def delete_quest(quest_id, game_name):
    mongo.db.Quests.remove({"_id": ObjectId(quest_id)})
    flash('Successfully deleted quest')
    return redirect(url_for('view_quests', game_name=game_name))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
