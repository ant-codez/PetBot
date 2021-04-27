from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
#from flask_restx import Api
#from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from config import Config

# create the flask application
app = Flask(__name__)
app.config.from_object(Config)

# create a login manager to remember users are logged in
login = LoginManager(app)
# set the login_view so that we can require users to be loggin for protected pages
login.login_view = 'login'

# connect to our database
db = SQLAlchemy()
migrate = Migrate(app, db)

#jwt = JWTManager(app)
db.init_app(app)

def create_app():
    from app import routes, models

    return app