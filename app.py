from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import time

app = Flask(__name__)                                   # FLASK_APP
sesh = Session(app)                                     # Create Session to store flask-session information
app.config['SECRET_KEY'] = 'my secret key, not yours'   # APP_ENCRYPTION_KEY
app.config['SESSION_TYPE'] = 'filesystem'               # STORE SESSION IN FILESYSTEM
app.config['SESSION_KEY_PREFIX'] = 'appy'               # PREFIX SESSION KEY
app.config['SESSION_PERMANENT'] = False                 # SET SESSION EXPIRE ON BROWSER RESTART
app.config['SESSION_USE_SIGNER'] = True                 # ADD ENCRYPTION SIGNATURE TO SESSION DATA
db_config = {                                           # Configure MySQL database connection: 
    "host": "app-database.carawrzvoi8u.us-west-2.rds.amazonaws.com", # Host
    "user": "admin",                                                 # UserName
    "password": "administrator",                                     # Password
    "database": "User_Log"                                           # Database
}
class CursorContext:                    # CursorContext gives context manger functionality
    def __init__(self, **config):       #       __init__
        self.config = config            # assign self.config which is conf dictionary
        self.connection = None          # associated database connection 
    def __enter__(self):                #       __enter__
        self.connection = mysql.connector.connect(**self.config) # initiate connection upon implicit enter method call
        return self.connection          # return a connection
    def __exit__(self, exc_type, exc_value, exec_tb):               #       __exit__
        if self.connection:             # if theres a connection open:
            self.connection.close()     #   close it

        # Routes
@app.route('/')                         #   HOME route
def home():
    if "user" in session:               # if there is an active session:
        print(session['user'])          #   debug
    return render_template('home.html') # render the template


@app.route('/log_in', methods=['GET', 'POST'])                              #       LOG_IN
def log_in():

    if request.method == 'POST':                                            # POST method
        user_name = request.form['userName'].strip()                        # username
        password = request.form['passWord'].strip()                         # password

        with CursorContext(**db_config) as connection:                      # Connect with wrapper class for context 
            cursor = connection.cursor()                                    # cursor
            query = "SELECT password FROM Users WHERE user_name = %s"       # query database for username and select pw hash
            cursor.execute(query, (user_name,))                             # execute query
            result = cursor.fetchone()                                      # get result
            if result:                                                      # if username exists:
                stored_password_hash = result[0]                            # convert stored_hash[tuple] to [str]
                if check_password_hash(stored_password_hash, password):     # check passwd
                    session['user'] = user_name                             # store session data of user
                    print('login successful')                               # debug 
                    return redirect(url_for('home'))                        # redirect back to home page
                else:
                    print('login unsuccessful')                             # debug
            else:
                print('all code ran')                                       # debug
    return render_template('login.html')                                    # render the template






@app.route('/register', methods=['GET', 'POST'])                                #       REGISTRATION method 
def register():
    if request.method == 'POST':                                                # POST method
        firstName = request.form['firstName'].strip()                           # get first name
        lastName = request.form['lastName'].strip()                             # get last name 
        userName = request.form['userName'].strip()                             # get user name
        e_mail = request.form['e-mail'].strip()                                 # get email
        password1 = request.form['password1'].strip()                           # get password1
        password2 = request.form['password2'].strip()                           # get password2 


        with CursorContext(**db_config) as connection:                          # connect with wrapper class
            cursor = connection.cursor()                                        # cursor

            #           CHECK IF ACCOUNT EXISTS WITH USERNAME AND EMAIL 
            query = "SELECT user_name, email FROM Users WHERE user_name = %s AND email = %s" # query
            cursor.execute(query, (userName, e_mail))   # retrieve username and email
            user = cursor.fetchone()                    # get result
            if user:                                    # if user exists: DENY REGISTRATION
                pass

            #           CHECK IF USERNAME IS TAKEN 
            query = "SELECT user_name FROM Users WHERE user_name = %s" # query
            cursor.execute(query, (userName,))          # execute
            username_taken = cursor.fetchone()          # get result
            if username_taken:                          # if username is taken: PLEASE USE ANOTHER USERNAME
                pass

            #           CHECK IF EMAIL IS IN USE
            query = "SELECT email FROM Users WHERE email = %s"         # query  
            cursor.execute(query, (e_mail,))            # execute
            email_taken = cursor.fetchone()             # get result
            if email_taken:                             # if email is taken: PLEASE USE ANOTHER EMAIL
                pass
            #           INITIATE REGISTRATION AS ALL CHECKS HAVE PASSED
            stored_password_hash = generate_password_hash(password1, 'pbkdf2:sha256', 8) # store input password hash
            query = "INSERT INTO Users (first_name, last_name, user_name, email, password) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (firstName, lastName, userName, e_mail, stored_password_hash)) # execute query
            connection.commit()                         # commit changes
            cursor.close()                              # close cursor
    return render_template('home.html')                 # render template

@app.route('/user')                                     #       USER 
def user():
    if "user" in session:
        print(f"the user is {user}")
    pass


@app.route('/sign_up', methods=['GET', 'POST']) #   SIGNUP - (not really being used atm)
def sign_up():
    return render_template('sign-up.html')








