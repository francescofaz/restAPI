import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("postgresql://mrucubjyvoomcj:864bc4125ed3d78be6a6657f4df578ca42e68b7dd727ce52d8da1a53eda2e02f@ec2-34-252-251-16.eu-west-1.compute.amazonaws.com:5432/d12r2s9pu1pgu7", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'secret_key'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/<name>
api.add_resource(Store, '/store/<string:name>')  # http://127.0.0.1:5000/item/<name>
api.add_resource(ItemList, '/items')  # http://127.0.0.1:5000/items
api.add_resource(UserRegister, '/register')  # http://127.0.0.1:5000/item/<name>
api.add_resource(StoreList, '/stores')  # http://127.0.0.1:5000/stores/

if __name__ == '__main__':
    from section6.db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
