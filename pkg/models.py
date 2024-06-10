from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()




class User(db.Model):
    user_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    fname = db.Column(db.String(64), index=True, nullable=False)
    lname = db.Column(db.String(64), index=True, nullable=False)
    address = db.Column(db.String(200), index=True, nullable=False)
    city = db.Column(db.String(64), index=True, nullable=False)
    zipcode = db.Column(db.String(64), index=True, nullable=False)
    regdate = db.Column(db.DateTime(), default=datetime.utcnow)
    email = db.Column(db.String(100), index=True, nullable=False)
    ssn = db.Column(db.String(50), index=True, nullable=True) 
    password = db.Column(db.String(225), index=True, nullable=False)
    


class Transaction(db.Model):
    trans_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    order_user_id=db.Column(db.Integer(), db.ForeignKey('user.user_id',ondelete='CASCADE', onupdate='CASCADE'))



    




class Adminreg(db.Model):
    admin_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    admin_username=db.Column(db.String(20),nullable=False)
    admin_pwd=db.Column(db.String(200),nullable=False)

    
