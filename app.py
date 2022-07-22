"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "here-we-are"

connect_db(app)

@app.route('/')
def list_cupcakes():
    """Return all cupcakes"""
    cupcakes = Cupcake.query.all()
    
    return render_template('index.html', cupcakes=cupcakes)


@app.route('/api/cupcakes')
def get_cupcakes():
    """Renders html template of all the cupcakes"""
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)



@app.route('/api/cupcakes/<int:cupcake_id>')
def one_cupcake(cupcake_id):
    """Renders html template of all the cupcakes"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())



@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
    """Add a new cupcake"""
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], image=request.json["image"] or None)
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return  (response_json, 201)
    

    

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    """Updates a single cupcake in the list of cupcakes"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())




@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted Cupcake")