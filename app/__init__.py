from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
migrate = Migrate(app, db)

jwt = JWTManager(app)
db.init_app(app)

def create_app():
    from app import routes, models

    return app