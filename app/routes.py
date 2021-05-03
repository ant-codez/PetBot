from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from app.models import User, Pet


from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from datetime import datetime
import random

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if the user is already logged in redirect them to the 'home' page
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # create the login-form defined in 'forms.py'
    form = LoginForm()
    if form.validate_on_submit():
        # user has hit submit so we look for them in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            # could not find user in the database so we redirect to the login page
            flash(f'Invalid email or password')
            return redirect(url_for('login'))

        # we successfully found the user, redirect to the home page
        #flash(f'Login requested for user {form.username.data}, remember me={form.remember_me.data}')
        login_user(user, remember=form.remember_me.data)

        # if we don't have any next queries in the url query string then redirect back to the home
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # if the user is already logged in redirect them to the 'home' page
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        # TODO: make this a function - generate_username_with_suffix(username)
        username = ""
        while True:
            suffix = '-' + str(random.randint(1000, 9999))
            user = User.query.filter_by(user_id=form.username.data + suffix)
            if user is not None:
                username = form.username.data + suffix
                break
        user = User(user_id=username, email=form.email.data, source='website')
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        # TODO: make this a function - generate_username_with_suffix(username)
        username = form.username.data

        while True:
            suffix = '-' + str(random.randint(1000, 9999))
            unique_username = str(username) + suffix
            #print(unique_username)
            user = User.query.filter_by(user_id=unique_username).first()
            if user is None:
                username = unique_username
                break
        current_user.user_id = username
        current_user.about_me = form.about_me.data
        db.session.commit()
    return render_template('edit_profile.html', form=form)

@app.route('/user/<user_id>')
@login_required
def user(user_id):
    user = User.query.filter_by(user_id=user_id).first_or_404()
    #pets = Pet.query.filter_by(owner_id=user.id)

    return render_template('user.html', user=user)

@app.route('/protected')
@login_required
def protected():
    return render_template('protected.html')

@app.route('/home')
def home():
    return render_template('home.html', title='Home')