from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required

from app import app, login_manager, bcrypt, db
from models import User


@app.route('/')
def index():
    return render_template('index.html', current_user=current_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(User.query.filter_by(email=email).first())
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User(email, password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/invoices')
@login_required
def invoices():
    return 'invoices !'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
