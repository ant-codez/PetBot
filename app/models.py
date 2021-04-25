from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=True)
    password_hash = db.Column(db.String(128), nullable=True)
    source = db.Column(db.String(128))
    discord_id = db.Column(db.BigInteger, unique=True, nullable=True)
    # one-to-many pet
    pets = db.relationship('Pet', backref='user')
    # one-to-one inventory
    inventory = db.relationship('Inventory', backref='user', uselist=False)

    def __repr__(self):
        return f'<User {self.username}>'

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

