from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key="francis"
api = Api(app)

jwt=JWT(app, authenticate, identity)    # new JWT object that creates /auth endpoint
                                        # auth endpoint returns JWT token that is then used with subsequent requests
                                        # it uses the identity function to verify the token 

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        # return {'item': next(filter(lambda x: x['name'] == name, items), None)}
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404
    
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "Item with name '{}' already exists.".format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)