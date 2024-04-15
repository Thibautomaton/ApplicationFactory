from . import auth
from .forms import LoginForm
from ..models import User, Role
from flask import url_for, request, redirect, render_template, flash
from flask_login import login_user, logout_user, current_user, login_required

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password_hash(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
    return render_template("auth/login.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been loggout ")
    flash("bad luck")
    return redirect(url_for('main.index'))





