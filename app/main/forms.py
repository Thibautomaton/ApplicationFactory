from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectMultipleField
from wtforms.validators import DataRequired, Length


class NameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    role = SelectMultipleField("Role", choices=[(1, "Admin"), (2, "Moderator"), (3, "Member")], coerce=int)
    # email = EmailField("Email", validators=[DataRequired(), Length(max=64)])
    # password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=16)])
    send = SubmitField("Send")
