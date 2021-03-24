from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from section6.resources.user import UserRegister
from section6.resources.item import Item, ItemList
from section6.resources.store import Store, StoreList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
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
