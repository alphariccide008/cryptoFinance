import random,string
import json,requests
from functools import wraps

from flask import render_template,request,abort,redirect,flash,make_response,session,url_for,jsonify
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash, check_password_hash


from pkg import app,csrf
from pkg.models import db,User
from pkg.forms import *



#This is a decoratoer to help check if there is a user logged in
def login_required(f):
    @wraps(f)
    def login_check(*args,**kwargs):
        if session.get('user')!=None:
            return f(*args,**kwargs)
        else:
            flash("Access denied ,Login", "danger")
            return redirect('/login')
    return login_check 


def generate_string(howmany):#call this function as renerate_string(10)
    x = random.sample(string.digits,howmany)
    return ''.join(x)


@app.route("/")
def homepage():
    return render_template("users/index.html",title="Landing Page")


@app.route("/login/",methods=["POST","GET"])
def login():
    if request.method =="GET":
        return render_template('users/login.html')
    else:
        email = request.form.get('email')
        pwd =request.form.get('pwd')
        deets = db.session.query(User).filter(User.email==email).first()
        if deets != None:
            hashed_pwd=deets.password
            if check_password_hash(hashed_pwd,pwd)==True:
                session['user']=deets.user_id
                return redirect(url_for('dashboard'))
            else:
                flash('invalid credentials, try again',"danger")
                return redirect(url_for('login'))
        else:
            flash('invalid Credentials, try again',"danger")
            return redirect(url_for('login'))
    





@app.route("/register",methods=['POST','GET'])
def register():
    form= RegForm(request.form)
    if request.method=="POST":
        # Generate a unique token for
        hash_password = generate_password_hash(form.pwd.data)
        # validate if the user email is already in the database   
        if User.query.filter_by(email=form.email.data).first():
            flash("This Email is already in use","danger")
            return redirect(url_for('register'))
        else:
            new_user=User(fname=form.fname.data,lname=form.lname.data,address=form.address.data,city=form.city.data,zipcode=form.zipcode.data, email=form.email.data, ssn=form.ssn.data, password=hash_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully', "success")
            return redirect(url_for('login'))
    return render_template("users/register.html", form=form)


@app.route("/about/")
def about_us():
    return render_template("users/about.html", title="About Us")

@app.route("/plans/")
def plans():
    return render_template("users/plan.html", title="Plans")

@app.route("/faq/")
def faq():
    return render_template("users/faq.html", title="FAQ")

@app.route("/dashboard/")
@login_required
def dashboard():
    id= session.get('user')
    userdeets = db.session.query(User).get_or_404(id)
    return render_template("users/dashboard.html", userdeets=userdeets)


            
       





@app.route("/logout")
def logout():
    if session.get('user')!= None:
        session.pop('user',None)
        flash('you\'ve logged out successfully',"success")
    return redirect(url_for('login'))





@app.errorhandler(404)
def error_page(errors):
    return render_template("users/errorpage.html")



@app.after_request
def after_request(response):
    response.headers["cache-control"]="no-cache, no-store, must-revalidate"
    return response





# @app.errorhandler(500)
# def server_error_page(errors):
#     return render_template("users/errorpage.html")
 

# @app.errorhandler(403)
# def forbbiden_page(errors):
#     return render_template("forbbiden.html")



# # @app.route("/registration")
# # def registration():
# #     if request.method =="GET":
# #         return render_template("users/reg_log.com")

# @app.route("/layout")
# def layout():
#     return render_template("users/layout.html")








