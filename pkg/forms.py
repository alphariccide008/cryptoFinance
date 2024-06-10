from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import StringField, SubmitField, TextAreaField ,PasswordField,RadioField,validators
from wtforms.validators import Email, DataRequired, EqualTo, Length



class RegForm(FlaskForm):
    fname = StringField("FirstName",validators=[DataRequired(message="Input your First Name")])
    lname = StringField("Last Name",validators=[DataRequired(message="Input your Last Name")])
    email = StringField("Email",validators=[Email(),DataRequired(message="Input valid email")])
    ssn = StringField("Ssn",validators=[Email(),DataRequired(message="Input valid ssn")])
    address = StringField("Email",validators=[Email(),DataRequired(message="Input valid Address")])
    city = StringField("Email",validators=[Email(),DataRequired(message="Input valid city")])
    zipcode = StringField("Email",validators=[Email(),DataRequired(message="Input valid zipcode")])
    pwd = PasswordField("Enter Password",validators=[DataRequired(message="Password must match")])
    confpwd = PasswordField("Confirm Password",validators=[DataRequired(message="password don't match"),EqualTo("pwd")])
    btnsubmit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email()])
    password = PasswordField('New Password', [validators.DataRequired()])


