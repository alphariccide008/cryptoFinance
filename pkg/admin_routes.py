import random,string,os
import json,requests
from functools import wraps

from flask import render_template,request,abort,redirect,flash,make_response,session,url_for,jsonify
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash, check_password_hash


from pkg import app,csrf
from pkg.models import db,User,Adminreg
from pkg.forms import *





#This is a decoratoer to help check if there is a user logged in
def login_required(f):
    @wraps(f)
    def login_check(*args,**kwargs):
        if session.get('admin') !=None:
            return f(*args,**kwargs)
        else:
            flash('Access Denied')
            flash('You must be logged in first')
            return redirect('/admin/')
    return login_check


@app.route("/admin/",methods=["POST","GET"])
def admin():
    if request.method =="GET":
        return render_template('admin/adminlog.html')
    else:
        username = request.form.get('username')
        pwd =request.form.get('pwd')
        deets = db.session.query(Adminreg).filter(Adminreg.admin_username==username).first()
        if deets != None:
            hashed_pwd =deets.admin_pwd

            if check_password_hash(hashed_pwd,pwd)==True:
                session['admin']=deets.admin_id

                return redirect(url_for('all_user'))
            else:
                flash('invalid credentials, try again',category='error')
                return redirect('/admin/')
        else:
            flash('invalid Credentials, try again',category='error')
            return redirect('/admin/')


