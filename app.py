from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin 
from werkzeug.security import generate_password_hash, check_password_hash 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'my_key_not_yours'
db = SQLAlchemy(app) 

def init_app():
    with app.app_context():
        db.create_all()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    pass 

    def __init__(self, fn, ln, un, em, pw): 
        self.first_name = fn
        self.last_name = ln 
        self.username = un 
        self.email = em 
        self.password_hash = generate_password_hash(pw)

    def check_password(self, password): 
        return check_password_hash(self.password_hash, password)
    
    def set_password(self, password): 
        self.password_hash = generate_password_hash(password)

    



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign-up.html')

@app.route('/log_in', methods=['GET'])
def log_in():
    if request.method == 'POST': 
        login_username = request.form['userName'] 
        login_password = request.form['passWord']
        db.session.query.filter_by()
        return render_template('login.html')

@app.route('/submit', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        userName = request.form['userName']
        e_mail = request.form['e-mail']
        password1 = request.form['password1']
        password2 = request.form['password2']

        #query database to see if user already exists 

        #query database to see if username is taken 

        #query database to see if email is taken 

        #verify that passwords match 
        


    return render_template('home.html')











