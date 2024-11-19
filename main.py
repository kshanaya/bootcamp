from flask import Flask, render_template, request, url_for, redirect
from model import *
import os 


current_dir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///" + os.path.join(current_dir, 'data_base.sqlite3')
UPLOAD_FOLDER= 'static/songs'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER



db.init_app(app)
app.app_context().push()



@app.route('/', methods=['GET','POST']) #http://127.0.0.1:5000/
def home():
    
    if request.method=='POST':
        form_email=request.form['email']    
        form_password=request.form['password']
        
        
        check_user=user.query.filter_by(email=form_email).first()
        
        if check_user:
            if check_user.password==form_password:
                
                if check_user.user_type=='enduser':
                    return redirect(url_for('enduser',id=check_user.id))
                elif check_user.user_type=='artist':
                    
                    check_artist=artist_check.query.filter_by(artist_id=check_user.id).first()#can also use (email=check_user.email)
                    if check_artist.status==False:
                        return "you are not yet verified"
                    else:
                        return redirect(url_for('artist', id=check_user.id))
                    
                elif check_user.user_type=='admin':
                    return redirect(url_for('admin'))
            
            else:
                return 'Incorrect password'    
            
        else:
            return 'Email not registered, please go back and sign up'
        
    
    return render_template('home.html')



@app.route('/enduser/<id>', methods=['GET']) 
def enduser(id):
    user_detail=user.query.filter_by(id=id).first()
    
    return render_template('enduser.html',username=user_detail.username)



@app.route('/artist/<id>', methods=['GET']) 
def artist(id):
    artist_detail=user.query.filter_by(id=id).first()
        
    return render_template('artist.html', artist_detail=artist_detail)




@app.route('/admin', methods=['GET',"POST"]) 
def admin():
    
    if request.method == "POST":
        form_id = request.form['id']
        form_status = request.form['status']

        verify= artist_check.query.filter_by(artist_id=form_id).first()
        if form_status == "T":
            verify.status= True
            db.session.commit()

    
    data=artist_check.query.filter_by(status=False).all()
    
    return render_template('admin.html', data=data)




@app.route('/signup_enduser', methods=['GET','POST']) 
def signup_enduser():
    if request.method=='POST':
        form_username=request.form['username']
        form_email=request.form['email']    
        form_password=request.form['password']
        
        print(form_username)
        print(form_email)
        print(form_password)
        
        
        
        
        if user.query.filter_by(email=form_email).count()>0:
            return "email already exists, please go back to artist"
        else:
            new_data= user(username=form_username ,email=form_email , password= form_password , user_type='enduser')
            db.session.add(new_data)
            db.session.commit()
        
        
            return redirect(url_for('home'))
        
        
        
        
    return render_template('signup_enduser.html')


@app.route('/signup_artist', methods=['GET','POST']) 
def signup_artist():
    
    if request.method=='POST':
        form_username=request.form['username']
        form_email=request.form['email']
        form_password=request.form['password']
        form_type=request.form['user_type']
        
        print(form_username)
        print(form_email)
        print(form_password)
        
        
        check_user=user.query.filter_by(email=form_email).first()
        if check_user:
            return "email already exists, please go back to sign up"
        else:
            new_data= user(username=form_username ,email=form_email , password= form_password , user_type=form_type)
            db.session.add(new_data)
            db.session.commit()
            
            status = artist_check(artist_id=new_data.id, username=new_data.username, email=new_data.email)#changed artist to artist_check since there was function def artist already in line 56
            db.session.add(status)
            db.session.commit()
        
        
            return redirect(url_for('home'))
        
        
        
    return render_template('signup_artist.html')



@app.route('/upload', methods=['POST'])
def upload():
    file=request.files['file']
    
    
    file_path=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    return f"File uploaded successfully: {file_path}"

    




@app.route('/demo_query', methods=['GET'])
def demo():
    print('''
          
          
          
          
          
          ''')
    
    # quering data
    """data = user.query.all()
    for i in data:
        print(i.username, i.user_type)
        
    data=user.query.filter_by(user_type='artist').all()
    for i in data:
        print(i.username, i.user_type)
        
    print('''
          
          difference between all and first
          
          ''')
    
    data2=user.query.filter_by(user_type='artist').first()
    print(data2.username, data2.user_type)
    
    
    query='a%'
    data3=user.query.filter(user.username.like(query)).all()
    for i in data3:
        print(i.username)"""
        
        
    # adding data to database
    '''new_data= user(username='misty',email='misty@gmail.com', password='123', user_type='enduser')
    db.session.add(new_data)
    db.session.commit()'''
    
    
    
    print('''
          
          
          
          
          ''')
    
    return "look in to the vs code terminal for results"
    




if __name__ == "__main__":
    
    db.create_all()
    
    app.debug= True
    
    app.run()
    
    

    