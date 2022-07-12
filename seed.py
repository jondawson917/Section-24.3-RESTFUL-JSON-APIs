from app import app
from models import db, connect_db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
    flavor="strawberry",
    size="medium",
    rating=3,
    image="https://www.cookingclassy.com/wp-content/uploads/2014/06/strawberry-cupcakes8-edit+srgb..jpg"
)

db.session.add_all([c1, c2, c3])
db.session.commit()