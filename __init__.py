from flask import Flask
from flask_session import Session
from datetime import datetime, timedelta
from routes import Blueprint, server, pdb

app = Flask(__name__)                                               # FLASK_APP
app.config['SECRET_KEY'] = 'my secret key, not yours'               # APP_ENCRYPTION_KEY
app.config['SESSION_TYPE'] = 'filesystem'                           # STORE SESSION IN FILESYSTEM
app.config['SESSION_KEY_PREFIX'] = 'app'                            # PREFIX SESSION KEY
app.config['SESSION_COOKIE_NAME'] = 'session_id'                    # SESSION COOKIE NAME
app.config['SESSION_COOKIE_DURATION'] = timedelta(minutes=30)       # SESSION COOKIE DURATION
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)    # SESSION WILL EXPIRE 30 mins
app.config['SESSION_PERMANENT'] = False                             # SET SESSION EXPIRE ON BROWSER RESTART
app.config['SESSION_USE_SIGNER'] = True                             # ADD ENCRYPTION SIGNATURE TO SESSION DATA
# app.config['SESSION_SECURE'] = False                              # ONLY SERVER HAS ACCESS TO SESSION DATA
# app.config['SESSION_HTTPONLY'] = False                            # HTTPS ONLY - False by default 
sess = Session(app)                                                 # Create Session to store flask-session information


pdb.set_trace() # BREAK
app.register_blueprint(server)      # BLUEPRINT REGISTER
