from app import app, login_manager
from flask import render_template, request, redirect, url_for
from flask_login import login_user
from models import User

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            login_user(User('admin', 'admin@mail'))
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/invoices')
def invoices():
    return 'invoices !'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
