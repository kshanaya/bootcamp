from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class demo_table(db.Model):
    __tablename__ ="demo_table"
    id=db.Column(db.Integer , primary_key= True, autoincrement=True)
    phoneNo=db.Column(db.Integer)
    age=db.Column(db.Integer)


#type of users:
#Admin -  maintain the app, manage the app
#artist - content creators of app
#enduser - consumers of your app


class user(db.Model):
    __tablename__ ="user"
    id=db.Column(db.Integer , primary_key= True, autoincrement=True)
    username= db.Column(db.String)
    email= db.Column(db.String, unique= True)
    password= db.Column(db.String)
    user_type= db.Column(db.String)
    
    
class artist_check(db.Model):
    __tablename__ ="artist_check"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_id=db.Column(db.Integer)
    username=db.Column(db.String)
    email=db.Column(db.String)
    status=db.Column(db.Boolean, default=False)
    song_list=db.relationship('songs',secondary='artist_song_relationship')
    
    
class artist_song_relatinship(db.Model):
    __tablename__='artist_song_relationship'
    song_id=db.Column(db.Integer, db.ForeignKey('songs.id'),primary_key=True)
    artist_id2=db.Column(db.Integer, db.ForeignKey('artist_check.id'),primary_key=True)

    
    
class songs(db.Model):
    __tablename__='songs'
    id= db.Column(db.Integer, primary_key=True, autoincrement =True)
    title= db.Column(db.String)
    likes= db.Column(db.Integer, default=0)
    dislikes=db.Column(db.Integer, default=0)
    genre=db.Column(db.String)
    url=db.Column(db.String)
    song_artist= db.relationship('artist_check', secondary='artist_song_relationship')
    