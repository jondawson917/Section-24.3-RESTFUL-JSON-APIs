"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

CUPCAKE_URL = "https://tinyurl.com/demo-cupcake"

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Cupcake Model"""

    __tablename__ = "cupcakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=CUPCAKE_URL)
    

    def serialize(self):
        """Returns a dict representation of cupcake which we can turn into JSON"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }

    def __repr__(self):
        return f"<Cupcake id: {self.id} Flavor={self.flavor} Size={self.size} Rating: {self.rating} Image: {self.image} >"