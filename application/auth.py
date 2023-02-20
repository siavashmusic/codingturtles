from flask import Blueprint, render_template, request, flash \
    , redirect, url_for
from .models import User
# import MySQLdb.cursors
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from application import db

auth = Blueprint('auth', __name__)


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash('Logged in successfully !', category='success')
                return redirect(url_for("views.index"))
            else:
                flash('Incorrect email / password !', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template('login.html', user=current_user)


@auth.route("/signup/", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST' \
            and 'name' in request.form \
            and 'email' in request.form \
            and 'password' in request.form \
            and 'repassword' in request.form:

        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        repassword = request.form.get('repassword')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Your email already exists!', category='error')
        elif len(name) < 4:
            flash('Name must be greater than 4 characters', category='error')
        elif password != repassword:
            flash("Please check your password.They aren't matched", category='error')
        else:
            # cursor.execute('INSERT INTO users VALUES (NULL, % s, % s, % s)',
            #                (name, email, generate_password_hash(password, 'sha256'),))
            # db.connection.commit()
            new_user = User(name=name, email=email, password=generate_password_hash(password, method="sha256") )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("auth.login"))

    elif request.method == 'POST':
        flash("Please try again.", category='error')
    return render_template("signup.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You're logged out successfully!", category='success')
    return redirect(url_for("auth.login"))
