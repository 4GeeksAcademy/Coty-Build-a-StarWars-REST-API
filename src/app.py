"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = User.query.all()

    user_list = [user.serialize() for user in response_body]

    return jsonify(user_list), 200

@app.route('/people', methods=['GET'])
def get_people():

    response_body = People.query.all()

    people_list = [person.serialize() for person in response_body]

    return jsonify(people_list), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_people_by_id(people_id):

    response_body = People.query.get(people_id)

    return jsonify(response_body.serialize()), 200

@app.route('/planets', methods=['GET'])
def get_planets():

    response_body = Planets.query.all()

    planets_list = [planet.serialize() for planet in response_body]

    return jsonify(planets_list), 200

@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_planets_by_id(planets_id):

    response_body = Planets.query.get(planets_id)

    return jsonify(response_body.serialize()), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def crear_planets(planet_id):
        
    planeta = Favorite(
        tipo = "planeta",
        id_tipo = planet_id,
    )
    db.session.add(planeta)
    db.session.commit()

    return jsonify(planeta.serialize()), 200

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def crear_people(people_id):
        
    persona = Favorite(
        tipo = "persona",
        id_tipo = people_id,
    )
    db.session.add(persona)
    db.session.commit()

    return jsonify(persona.serialize()), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    favorite_planet = Favorite.query.filter_by(id_tipo=planet_id, tipo="planeta").first()
    if favorite_planet is None:
        return jsonify({'error': 'Favorite planet not found'}), 404

    db.session.delete(favorite_planet)
    db.session.commit()

    return jsonify({'success': True}), 200

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    favorite_people = Favorite.query.filter_by(id_tipo=people_id, tipo="persona").first()
    if favorite_people is None:
        return jsonify({'error': 'Favorite people not found'}), 404

    db.session.delete(favorite_people)
    db.session.commit()

    return jsonify({'success': True}), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
