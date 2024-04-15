from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(UserMixin, db.Model):
    __tablename__ = "users"
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<User %r>" % self.username

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password_hash(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tablename__ = "roles"
    name = db.Column(db.String(64), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship("User", backref='role', lazy="dynamic")

    def __repr__(self):
        return "<Role %r>" % self.name


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

