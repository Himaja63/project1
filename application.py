import os

from flask import Flask, render_template, request
import json 
from flask import Flask, session,url_for,redirect
from flask import flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from models import *

from  datetime import datetime

app = Flask(__name__, template_folder=r"C:\Users\Himaja\Documents\project1\project1\templates")
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def home():    
    return render_template('index.html')

@app.route("/register", methods=["POST"])
def register():
    # name = request.form.get("name")
    # password = request.form.get("password")    
    # return render_template("register.html", name=name, password=password)
    Users.query.all()
    name = request.form.get("name")
    password = request.form.get("password")
    timestamp = str(datetime.now())
    userdata = Users(username=name, password=password, timestamp=timestamp)
    # print(f"added the user {name}{password}******************")
    try:
        db.session.add(userdata)
        db.session.commit()
        return render_template("register.html", name=name, password=password)
    except Exception :
	    return render_template("error.html", error = "This name already exists")

@app.route("/admin")

def Member():     
      u_list = Users.query.all()
      return render_template("admin.html", Users=u_list)



@app.route("/auth",methods = ["GET","POST"])
def authenticate():
    if request.method == "POST":   
        name = request.form.get("name")
        password = request.form.get("password")
        userdata = Users.query.filter_by(username=name).first()        
        if userdata is not None:
            # validate username and password
            if userdata.username == name and userdata.password == password:         
                return render_template("login.html", name=name, 
                data=[{'name':'select an option'},{'name':'ISBN number of a book'}, {'name':'title of a book'}, {'name':'author of a book'}])
            
            else:
                return render_template("index.html", message="Invalid username/password.")
        # new user
        else:
            return render_template("index.html", message="Not yet registered..please register")
    else :
        return "Invalid login request"

@app.route("/search" , methods=['POST'])
def search():
    Booklist = BOOKS.query.all()
    select = request.form.get('comp_select')    
    if (select == 'ISBN number of a book'):
        holder = 'Give an isbn number'
        text = 'Give an isbn number in the in the following search box' 
        return render_template('search.html', holder = holder, text = text)
    if (select == 'title of a book'):
        holder = 'Give a book title'
        text = 'Give title of a book in the in the following search box' 
        return render_template('search.html', holder = holder, text = text)
    if (select == 'author of a book'):
        holder = 'Give an author'
        text = 'Give the name of an auther of a book in the following search box'
        return render_template('search.html', holder = holder, text = text)
    else:
        holder = 'select an option'    
        text = 'Please select an option from the above drop down box'    
        return render_template('search.html', holder = holder, 
        message = "select an option in the previous page", text = text)        

   

@app.route("/results", methods = ['POST'])
def results():    
    option = request.form.get("option")
    print(option)  
    if (option is not None):  
        result = db.session.query(BOOKS.tittle).\
            filter(BOOKS.isbn == request.form.get("option")).\
            scalar()
        
        if (result is not None):
            return render_template('search.html', option = option, result = result)
        else:
            result = db.session.query(BOOKS.tittle).\
            filter(BOOKS.tittle == request.form.get("option")).\
            scalar()                   
            if (result is not None):
                return render_template('search.html', option = option, result = result)
            else :
                result = db.session.query(BOOKS.tittle).\
                    filter(BOOKS.author == request.form.get("option")).all()
                
                result = json.dumps(result) 
                
                if (result is not None):
                    return render_template('search.html', option = option, result = result)
                else:
                    return render_template('search.html', message = 'Give valid input')
    else :
        return render_template('search.html', message = 'Give an input')


if __name__ == '__main__': 
    app.run()



