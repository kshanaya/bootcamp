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
    
    
class artist(db.Model):
    __tablename__ = 'artist'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_user_id=db.Column(db.Integer)
    status=db.Column(db.Boolean, default=False)
    