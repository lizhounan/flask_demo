from flask import Flask, redirect, url_for, render_template, request, session
from flask import flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'zhounanli'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



from website.views.admin import admin
app.register_blueprint(admin, url_prefix='/admin')

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/ML_projects')
def show_ML_proejcts():
    return render_template('ML_projects.html')

@app.route('/DA_projects')
def show_DA_proejcts():
    return render_template('DA_projects.html')

@app.route('/Other_projects')
def show_Other_proejcts():
    return render_template('Other_projects.html')