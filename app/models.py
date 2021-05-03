from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
from hashlib import md5
from datetime import datetime
import random



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=True)
    password_hash = db.Column(db.String(128), nullable=True)
    source = db.Column(db.String(128))
    discord_id = db.Column(db.BigInteger, unique=True, nullable=True)
    about_me = db.Column(db.String(255))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    # one-to-many pet
    pets = db.relationship('Pet', backref='user')
    # one-to-one inventory
    inventory = db.relationship('Inventory', backref='user', uselist=False)

    # used for password hashing
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # used for retrieving a password given a hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=robohash&s={size}'
    
    def username(self):
        return self.user_id[0 : self.user_id.rfind('-')]



    def __repr__(self):
        return f'<User {self.user_id}>'

# one-to-one relationship
# one user can only have one inventory
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eggs = db.Column(db.Integer, index=True)
    coins = db.Column(db.Integer, index=True)
    # one-to-one user
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Inventory {self.id}>'

# one-to-many relationship
# one user can have many pets
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    species = db.Column(db.String(128))
    color = db.Column(db.String(128))
    closeness = db.Column(db.Integer)
    size = db.Column(db.String(64))
    ability_type = db.Column(db.String(128))
    rarity = db.Column(db.String(128))
    # one-to-many user
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Pet {self.name}>'


# flask-login expects a load_user function to help load a user given an id
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
