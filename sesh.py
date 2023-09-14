from flask import session

def set_session(key, value):                            # set session with a key
    session[key] = value                                # set key
    session.modified = True                             # Mark the session as modified

def get_session(key, default=None):                     # get session data by key
    return session.get(key, default)                    # return


db_config = {                                                       # Configure MySQL database connection: 
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



