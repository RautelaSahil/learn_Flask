from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#read config from Config class in config.py
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
# import after creation of app so later when we need to call app in routes it don't cause circular imports.
from app import routes, models