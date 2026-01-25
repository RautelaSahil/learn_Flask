import os
#Get the absolute path of the directory where this file is located
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    #Set SECRET_KEY from environment variable or use 'default' if not set
    #Secret key is used for session management and CSRF protection
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'default'
    
    #Set the database URI from environment variable or use a default SQLite database
    #taking the database URL from the DATABASE_URL environment variable, and if that isn't defined,
    #I'm configuring a database named app.db located in the main directory of the application,
    #which is stored in the basedir variable.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///'+ os.path.join(basedir,'app.db')