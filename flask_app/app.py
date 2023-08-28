from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector 
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key, not yours'
db_config = {
    "host": "app-database.carawrzvoi8u.us-west-2.rds.amazonaws.com",
    "user": "admin",
    "password": "administrator",
    "database": "User_Log"
}

class CursorContext:
    def __init__(self, **config):
        self.config = config
        self.connection = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.config)
        return self.connection

    def __exit__(self, exc_type, exc_value, exec_tb):
        if self.connection:
            self.connection.close()



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign-up.html')


@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    # Use POST method to hide user credentials for login
    if request.method == 'POST':
        # set up vars for form inputs
        user_name = request.form['userName'].strip()
        password = request.form['passWord'].strip()

        # Set up connection with CursorContext class
        with CursorContext(**db_config) as connection:
            # Set up cursor
            cursor = connection.cursor()
            # Query database for a match of the user_name and SELECT the password to check_password_hash()
            query = "SELECT password FROM Users WHERE user_name = %s"
            cursor.execute(query, (user_name,))
            # Capture stored password hash into result 
            result = cursor.fetchone()
            # If a password was returned, check_password_hash()
            if result:
                # Convert stored password hash from a tuple into a str
                stored_password_hash = result[0]
                # If provided hashed password matches stored password hash  
                if check_password_hash(stored_password_hash, password):
                    print('login successful')
                    return redirect(url_for('home'))
                else:
                    print('login unsuccessful')
            else: 
                print('all code ran')
            

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstName = request.form['firstName'].strip()
        lastName = request.form['lastName'].strip()
        userName = request.form['userName'].strip()
        e_mail = request.form['e-mail'].strip()
        password1 = request.form['password1'].strip()
        password2 = request.form['password2'].strip()

        # Establish context of working with sql database
        with CursorContext(**db_config) as connection:
            cursor = connection.cursor()

            # Query database to check if account already exits
            query = "SELECT user_name, email FROM Users WHERE user_name = %s AND email = %s"
            cursor.execute(query, (userName, e_mail))
            # Return query result
            user = cursor.fetchone()
            # Check if a result was returned
            if user:
                # Deny registration because of account existence
                pass

            # Query database to check if username is taken 
            query = "SELECT user_name FROM Users WHERE user_name = %s"
            cursor.execute(query, (userName,))
            # Return query result
            username_taken = cursor.fetchone()
            # Check to see if username is taken 
            if username_taken: 
                # Deny registration because of username availability 
                pass
            # Query database to check if email is already in use 
            query = "SELECT email FROM Users WHERE email = %s"
            cursor.execute(query, (e_mail,))
            # Return query result
            email_taken = cursor.fetchone()
            # Check to see if email is taken 
            if email_taken:
                # Deny registration because of email already being in use 
                pass 

            # Create password hash to be stored in the database 
            stored_password_hash = generate_password_hash(password1, 'pbkdf2:sha256', 8)

            # Register User
            query = "INSERT INTO Users (first_name, last_name, user_name, email, password) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (firstName, lastName, userName, e_mail, stored_password_hash))
            connection.commit()

            # Close cursor
            cursor.close()




    return render_template('home.html')











