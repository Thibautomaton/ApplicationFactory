from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import NameForm
from .. import db
from ..models import User

from flask_login import login_required


@main.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is None:
            user = User(name=form.name.data, role_id = form.role.data[0])
            session["known"]=False
            db.session.add(user)
            db.session.commit()
        else:
            session["known"]=True
            flash("user was already in database")
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, known=session.get("known"))

@main.route('/secret')
@login_required
def secret():
    return "<h1>You reached well done!</h1>"