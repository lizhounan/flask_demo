from flask import Blueprint
from flask import Flask, redirect, url_for, render_template, request, session
from flask import flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from website.database import users, db
admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates')

@admin.route('/home')
@admin.route('/')
def home():
    return render_template('admin/home.html')

@admin.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        session.permanent = True  
        session['usr'] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session['email'] = found_user.email
        else:
            usr = users(user, "", "")
            db.session.add(usr)
            db.session.commit()
        flash('login succesful!')
        return redirect(url_for('admin.user'))
    else:
        if 'usr' in session:
            flash('already login')
            return redirect(url_for('admin.home'))
        return render_template('admin/login.html')

@admin.route('/usr', methods=['POST', 'GET'])
def user():
    email = None
    if 'usr' in session:
        name = session['usr']

        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email
            found_user = users.query.filter_by(name=name).first()
            found_user.email = email
            db.session.commit()
            flash('email saved')
        else:
            if 'email' in session:
                email = session['email']
        return render_template('admin/user.html', name=name, email=email)
    else:
        flash('you are not login')
        return redirect(url_for('login'))