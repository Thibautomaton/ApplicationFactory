# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import click

import app
from app import create_app, db
from app.models import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        admin_role = Role(name="Admin", id=1)
        user_john = User(email = "email@gmail.com", username="john", role = admin_role, password="password")
        db.session.add_all([admin_role, user_john])
        db.session.commit()

        app.run(debug=True)

"""
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        admin_role= Role(name="Admin")
        moderator_role = Role(name="Moderator")
        member_role = Role(name="Member")
        user_john = User(name="john", role=admin_role)

        db.session.add_all([admin_role, moderator_role, member_role, user_john])
        db.session.commit()

    app.run(debug=True)
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
