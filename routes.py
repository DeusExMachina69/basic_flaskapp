from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from sesh import session, set_session, get_session, db_config, CursorContext
import pdb


server = Blueprint("server", __name__, static_folder="static", template_folder="templates", root_path="/home/ubuntu/flaskapp")       # BLUEPRINT


# DEBUG
#@server.before_request
# def before_request():
#    headers = request.headers
#    app.logger.info(f"Request Headers: {headers}")


@server.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')



    return render_template('home.html')   # render the template



@server.route('/log_in', methods=['GET', 'POST'])                              #       LOG_IN
def log_in():

    if request.method == 'POST':                                            # POST method
        user_name = request.form['userName'].strip()                        # username
        password = request.form['passWord'].strip()                         # password

        with CursorContext(**db_config) as connection:            # Connect with wrapper class for context 
            cursor = connection.cursor()                                    # cursor
            query = "SELECT password FROM Users WHERE user_name = %s"       # query database for username and select pw hash
            cursor.execute(query, (user_name,))                             # execute query
            result = cursor.fetchone()                                      # get result
            if result:                                                      # if username exists:
                stored_password_hash = result[0]                            # convert stored_hash[tuple] to [str]
                if check_password_hash(stored_password_hash, password):     # check passwd
                    cursor.close()
                    session['user'] = user_name                             # store session data of user
                    print('login successful')                               # debug 
                    return redirect(url_for('home'))                        # redirect back to home page
                else:
                    print('login unsuccessful')                             # debug
            else:
                print('all code ran')                                       # debug
    return render_template('login.html')                                    # render the template




#   REGISTRATION method 
@server.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':                                                # POST method
        firstName = request.form['firstName'].strip()                           # get first name
        lastName = request.form['lastName'].strip()                             # get last name 
        userName = request.form['userName'].strip()                             # get user name
        e_mail = request.form['e-mail'].strip()                                 # get email
        password1 = request.form['password1'].strip()                           # get password1
        password2 = request.form['password2'].strip()                           # get password2 


        with CursorContext(**db_config) as connection:                     # connect with wrapper class
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
            session.clear()                             # clear session data
            # session["user"] = userName                  # set session username
            # session["log_status"] = true                # set session log status
            user_data = {
                "user": "userName",
                "log_status": "True"
            }
            return redirect(url_for('home', **user_data))
    return render_template('home.html')                 # render template

#@server.route('/user')                                     #       USER 
# def user():
#    if "user" in session:
#        print(f"the user is {user}")
#    pass



#@server.route('/favicon.ico')
# def favicon():
#    response = app.make_response('')  # Create an empty response
#    response.headers['Content-Type'] = 'image/x-icon'
#    app.logger.info(f"Response headers: {response.headers}")
#    return response




