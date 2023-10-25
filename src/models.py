from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    gravity = db.Column(db.Integer)
    population = db.Column(db.Integer)
    diameter = db.Column(db.Integer)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            # do not serialize the password, its a security breach
        }
    
class Favorite(db.Model):
    __tablename__ = 'favorite'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(250), nullable=False)
    tipo = db.Column(db.String(250), nullable=False)
    id_tipo = db.Column(db.Integer)

    def __repr__(self):
        return '<Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "id_tipo": self.id_tipo
            
            # do not serialize the password, its a security breach
        }