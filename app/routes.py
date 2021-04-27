from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

import random

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
        username_id = 0
        while True:
            username_id = random.randint(1000, 9999)
            user = User.query.filter_by(username=form.username.data + '#' + str(username_id))
            if user is not None:
                break

        user = User(username=form.username.data + '#' + str(username_id), email=form.email.data, source='website')
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route('/')
@app.route('/protected')
@login_required
def protected():
    return render_template('protected.html')

@app.route('/home')
def home():
    return render_template('home.html', title='Home')