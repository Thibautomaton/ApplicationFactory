from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    email = EmailField("Your email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired(), Length(8, 16)])
    remember_me = BooleanField("stay logged in ")
    submit = SubmitField("log in")