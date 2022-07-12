"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)
print(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "not-so-secret-anymore"

connect_db(app)

def serialize_cupcakes(cupcake):
    """Serialize a cupcake from obj to dictionary"""
    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image,
    }


@app.route('/')
def index_page():
    """Displays the HTML template"""
    cupcakes = Cupcake.query.all()
    return render_template('index.html', cupcakes=cupcakes)



@app.route('/api/cupcakes')
def list_all_cupcakes():
    """Displays the HTML template"""
    cupcakes = Cupcake.query.all()
    serialized_cupcakes = [serialize_cupcakes(c) for c in cupcakes]

    return jsonify(cupcakes=serialized_cupcakes)    

@app.route('/api/cupcakes/<int:id>')
def list_one_cupcake(id):
    """Returns JSON w/ {"cupcake"=[{id, flavor, size, rating, image}]}"""

    cupcake = Cupcake.query.get_or_404(id)
    serialized_cupcake = serialize_cupcakes(cupcake)

    return jsonify(cupcake=serialized_cupcake)
    # end list_one_cupcake

@app.route("/api/cupcakes", methods=["POST"])
def make_cupcake():
    """Create cupcake from form data & return it.

    Returns JSON {'cupcake': {id, flavor, size, rating, iamge}}
    """

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image=  request.json["image"]

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized_cupcake = serialize_cupcakes(new_cupcake)

    # Return w/status code 201 --- return tuple (json, status)
    return ( jsonify(cupcake=serialized_cupcake), 201 )

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    """Returns JSON for one todo in particular"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)
    db.session.commit()

    return jsonify(cupcake=serialize_cupcakes(cupcake))

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """Deletes a particular todo"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted cupcake!!")