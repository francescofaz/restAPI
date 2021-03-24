from flask_restful import Resource
from flask_jwt import jwt_required
from section6.models.store import StoreModel


class Store(Resource):

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    def post(self, name):

        if StoreModel.find_by_name(name):
            return {'message': "A store with name {} already exists".format(name)}, 400  # Bad Request

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred inserting the store"}, 500 #Internal Server Error

        return store.json(), 201  # Created

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if not store:
            return {'message': "A Store with name {} doesn't exist".format(name)}, 400  # Bad Request

        store.delete_from_db()
        return {'message': "Store deleted"}



class StoreList(Resource):

    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
