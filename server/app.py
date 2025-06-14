# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here

@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    quake = Earthquake.query.filter_by(id=id).first()
    
    if quake:
        return jsonify(quake.to_dict()), 200
    else:
        return jsonify({"message": f"Earthquake {id} not found."}), 404
    
    

@app.route('/earthquakes/magnitude/<float:magnitude>')
def earthquakes_by_magnitude(magnitude):
    # Filter all earthquakes with magnitude >= the given value
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    # Serialize each quake into a dictionary
    quake_list = [quake.to_dict() for quake in quakes]

    # Build the response data
    response_data = {
        "count": len(quake_list),
        "quakes": quake_list
    }

    return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
