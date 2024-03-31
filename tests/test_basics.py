import unittest
from flask import current_app
from app import create_app, db
from app.models import User, Role

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        #db.drop_all()
        db.create_all()
        admin_role= Role(name="Admin")
        moderator_role = Role(name="Moderator")
        member_role = Role(name="Member")
        user_john = User(name="john", role=admin_role)

        db.session.add_all([admin_role, moderator_role, member_role, user_john])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_database_is_writing(self):
        user = User.query.filter_by(name="john").first()
        self.assertTrue(user is not None)


