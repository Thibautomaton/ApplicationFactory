from . import db

class User(db.Model):
    __tablename__="users"
    name = db.Column(db.String(64), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return "<User %r>" %self.name

class Role(db.Model):
    __tablename__="roles"
    name = db.Column(db.String(64), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship("User", backref='role', lazy="dynamic")

    def __repr__(self):
        return "<Role %r>" % self.name


def init_db():
    db.drop_all()
    db.create_all()
    admin_role = Role(name="Admin", id=1)
    db.session.add(admin_role)
    db.session.commit()


if __name__ == '__main__':
    init_db()