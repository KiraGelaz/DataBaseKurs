from flask import Blueprint, url_for, redirect, flash, render_template, request
from flask_login import login_user, logout_user

from ..extentions import db, bcrypt
from ..forms import RegistrationFrom, LoginFrom
from ..models.user import User

user = Blueprint('user', __name__)


# REGISTRATION FORM  #


@user.route("/user/register", methods=['POST', 'GET'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        status = "user"
        user = User(status=status, login=form.login.data, password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f"You're registrated", "success")
            return redirect(url_for('user.login'))
        except Exception as e:
            print(str(e))
            flash(f"Error! Try again", "danger")
    return render_template('user/register.html', form=form)


# LOGIN FORM  #


@user.route("/user/login", methods=['POST', 'GET'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash(f"Error! Try again", "danger")
    return render_template('user/login.html', form=form)


@user.route('/user/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('main.index'))
