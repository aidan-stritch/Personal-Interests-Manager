# Personal Interests Manager
This project is to develop an interface for users to create an account, and add the movies, 
tv shows and games that they follow and mark the movies and episodes that they have watched, 
and also the games quests that they have completed. 

In today's world, we watch many different tv shows and often forget where we have left off when we 
take a break from a series. The TV show section of this site will allow users to add their show and 
mark the episodes that they watch as they go so that they can easily come back later and find out where 
they left off. 

Also, we often see movies advertised that we would like to watch, only to forget about them until a year 
later when we see another advertisement. The Movies section will allow users to add a movie to their 
profile as soon as they hear of it so that they do not forget to watch it. 

Lastly, the Games section allows users to track the games that they are playing (or wish to play) and 
can mark off the quests that they have completed as they go.

## UX
This project was designed to allow users to, through CRUD functionality, manage a collection of data
related to TV shows, movies and games along with the users themselves. In particular;
- Allow users to read data from the database
- Allow users to edit the data through the web application
- Allow users to create new data through the web application
- Allow users to delete data through the web application

This website is designed for those of us who are organised and like to have a place to keep track 
of the different interests that we might have. Often in our busy lives, we can take a break from 
watching a series or playing a game, or might see an advertisement for a movie, only to forget 
where we left off or what we have not seen yet. Essentially, this website will allow those users to 
add to their profile the things that they wish to follow or keep track of. 

The functionality is in place for users to create and account and log in, and also to see their 
profile. From there they can see all movies, tv shows (and episodes), and games (along with the 
associated quests) in the database. 

I feel that this website satisfies the base requirements in that the users can create, read, update
and delete data related to items in the collections in the database in an easy to use and visually
appealing interface. 

### User Stories
#### New Users
- As a new user, I would like to be able to create an account, so that I can log into my new 
account.
#### Existing Users
- As an existing user, I would like to be able to log in, so that I can view my account.
- As an existing user, I would like to be able to add a movie I saw a trailer for, so that I will 
remember to watch it. 
- As an existing user, I would like to log out of my account, so that I can make sure no others use 
my account on this computer.
- As an existing user, I would like to mark an episode as watched, so that I can make sure I know
what episode I am to watch next.
- As an existing user, I would like to delete a show from my account, as I no longer like it and 
dont want to watch it anymore
- As an existing user, I would like to see what quest's I have left to complete on my game, so that 
I can see how much of the game is left to complete
#### Administrator Users
- As an admin user, I would like to be able to add new content to the database, so that I can 
update the collection
- As an admin user, I would like to view all users, so that I can delete those who are no longer 
valid.
- As an admin user, I would like to view all users, so that I can update the password for a user 
who has forgotten their login details.
- As an admin user, I would like to update the director of The Avengers: Endgame, so that the details 
are correct in the database.

### Wireframes
#### Desktop View
![desktop view index.html](static/wireframes/Index.html-Desktop.png "index.html page for desktop view")

![desktop view index.html](static/wireframes/Sign_Up.html-Desktop.png "sign_up.html page for desktop view")

![desktop view index.html](static/wireframes/Manage_Users.html-Desktop.png "manage_users.html page for desktop view")

![desktop view index.html](static/wireframes/edit_user.html-Desktop.png "edit_user.html page for desktop view")

![desktop view index.html](static/wireframes/User_Profile.html-Desktop.png "user_profile.html page for desktop view")

![desktop view index.html](static/wireframes/My_Movies.html-Desktop.png "my_movies.html page for desktop view")

![desktop view index.html](static/wireframes/Add_Movie.html-Desktop.png "add_movie.html page for desktop view")

![desktop view index.html](static/wireframes/Edit_Movie.html-Desktop.png "edit_movie.html page for desktop view")

![desktop view index.html](static/wireframes/My_Games.html-Desktop.png "my_games.html page for desktop view")

![desktop view index.html](static/wireframes/Add_Game.html-Desktop.png "add_game.html page for desktop view")

![desktop view index.html](static/wireframes/Edit_Game.html-Desktop.png "edit_game.html page for desktop view")

![desktop view index.html](static/wireframes/My_Quests.html-Desktop.png "my_quests.html page for desktop view")

![desktop view index.html](static/wireframes/Add_Quest.html-Desktop.png "add_quest.html page for desktop view")

![desktop view index.html](static/wireframes/Edit_Quest.html-Desktop.png "edit_quest.html page for desktop view")

![desktop view index.html](static/wireframes/My_TV_Shows.html-Desktop.png "my_tv_shows.html page for desktop view")

![desktop view index.html](static/wireframes/Add_TV_Show.html-Desktop.png "add_tv_show.html page for desktop view")

![desktop view index.html](static/wireframes/Edit_TV_Show.html-Desktop.png "edit_tv_show.html page for desktop view")

![desktop view index.html](static/wireframes/My_Episodes.html-Desktop.png "my_episodes.html page for desktop view")

![desktop view index.html](static/wireframes/Add_Episode.html-Desktop.png "add_episode.html page for desktop view")

![desktop view index.html](static/wireframes/Edit_Episode.html-Desktop.png "edit_episode.html page for desktop view")

![desktop view index.html](static/wireframes/User_Profile.html-Desktop.png "user_profile.html page for desktop view")

#### Mobile View
![mobile view index.html](static/wireframes/Index.html-Mobile.png "index.html page for mobile view")

![mobile view index.html](static/wireframes/Sign_Up.html-Mobile.png "sign_up.html page for mobile view")

![mobile view index.html](static/wireframes/Manage_Users.html-Mobile.png "manage_users.html page for mobile view")

![mobile view index.html](static/wireframes/edit_user.html-Mobile.png "edit_user.html page for mobile view")

![mobile view index.html](static/wireframes/User_Profile.html-Mobile.png "user_profile.html page for mobile view")

![mobile view index.html](static/wireframes/My_Movies.html-Mobile.png "my_movies.html page for mobile view")

![mobile view index.html](static/wireframes/Add_Movie.html-Mobile.png "add_movie.html page for mobile view")

![mobile view index.html](static/wireframes/Edit_Movie.html-Mobile.png "edit_movie.html page for mobile view")

![mobile view index.html](static/wireframes/My_Games.html-Mobile.png "my_games.html page for mobile view")

![mobile view index.html](static/wireframes/Add_Game.html-Mobile.png "add_game.html page for mobile view")

![mobile view index.html](static/wireframes/Edit_Game.html-Mobile.png "edit_game.html page for mobile view")

![mobile view index.html](static/wireframes/My_Quests.html-Mobile.png "my_quests.html page for mobile view")

![mobile view index.html](static/wireframes/Add_Quest.html-Mobile.png "add_quest.html page for mobile view")

![mobile view index.html](static/wireframes/Edit_Quest.html-Mobile.png "edit_quest.html page for mobile view")

![mobile view index.html](static/wireframes/My_TV_Shows.html-Mobile.png "my_tv_shows.html page for mobile view")

![mobile view index.html](static/wireframes/Add_TV_Show.html-Mobile.png "add_tv_show.html page for mobile view")

![mobile view index.html](static/wireframes/Edit_TV_Show.html-Mobile.png "edit_tv_show.html page for mobile view")

![mobile view index.html](static/wireframes/My_Episodes.html-Mobile.png "my_episodes.html page for mobile view")

![mobile view index.html](static/wireframes/Add_Episode.html-Mobile.png "add_episode.html page for mobile view")

![mobile view index.html](static/wireframes/Edit_Episode.html-Mobile.png "edit_episode.html page for mobile view")

### Entity Relationship Diagram (ERD)
![Entity Relationship Diagram](static/erd's/ERD.png "Entity Relationship Diagram showing relationships on Database")

## Features
This version of the website is the administrator side of this site, which allows all users to view 
the users as well as to create, read, update and delete data related to the users, movies, tv shows, 
games, quests and episodes. Please see the Features Left to Implement section for more details on 
version two of the website.

### Existing Features
1. **Login -** The customers are able to create their own accounts and log into the website 
with secure details.
2. **Sign-Up -** New users can sign up themselves if they wish to set up an account. 
3. **User Profile -** Each user has their own profile that welcomes them by Username for
personalisation. 
4. **Create Data -** Users can add new items to the database using a simple form.
5. **Read Data -** All users can read the data from the database relating to the Movies, 
TV shows, and Games they wish to view. 
6. **Update Data -** Users can edit the data relating to the items from the database in an 
easy to use form.
7. **Delete Data -** Users can delete any item that is no longer required with one button. 
8. **User Management -** Users can currently view all users and create new users, edit them 
or delete them with our simple to use Manage Users page. 
9. **Quest tracking -** Users can update the quests in the games that they follow with an 
easy to use switch that lets them mark the quest as "active" or "completed" to help them
track their progress easier.
10. **Episode tracking -** Users can update the episodes of the shows that they watch by 
marking them as "watched" with an easy to use switch. This allows them to monitor where
they are in each show. 
11. **Log-out -** Users can log out of the website at any time by clicking on the logout 
button on any page in the nav bar. 

### Features Left to Implement
1. **Administrator Privileges -** Currently, the website is set up for users to have unlimited 
functionality once logged in. Version 2 would include a limitation on functionality depending 
on user privileges. If the user is an administrator, they will have access to all functionality
and will be able to view the user's in the manage users page. Non-administrator users will only 
have access to their own user data, their profile, and will only be able to read from the database.
2. **User Specific Content -** In version 2, when a user logs in, they will be able to view only the 
games, tv shows, and movies that they personally have added to their profile. They will also be allowed 
remove these items from their profile (which will not delete the items from the database collections)
3. **Search functionality -** In future releases, the user will be able to search by keywords 
to find items that they can add to their profile for tracking. 
4. **News Feed -** The user will be able to click on a "news feed" that will show them updates
on the interests that they follow, along with suggestions for similar content they may wish to add. 
5. **Game Trophy Tracking -** Users will be able to see the trophies available in games (where
applicable) and mark them as "unlocked" or "locked" to track their progress with these. 
6. **Current Quest Banner -** When a user clicks into a specific game, a banner at the top 
will show them the "current" quest that they should be working on. In this instance, only 
one quest can be marked as "current" and by marking a quest as "current" a popup will advise
the customer that by doing this it will mark all other quests in this game as not "current"
7. **Social Profiles -** In future releases, the user will be able to share their profile 
with friends and connect with other users to see what they follow and how they are progressing
with different interests. 
8. **Expand Interests -** In future releases, the user will be able to track other interests
on their profile such as "music" (for artists and concerts etc.) and "sports". 
9. **Login Checks -** In version 2, when a user is being created, it will prompt the user 
if the entered username or email address already exists on the database and request a different
entry. 
## Technologies Used

## Testing

## Deployment

## Credits
### Content
### Media
### Acknowledgements
