from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from userRegister import UserRegister

app = Flask(__name__)
app.secret_key="francis"
api = Api(app)

jwt=JWT(app, authenticate, identity)    # new JWT object that creates /auth endpoint
                                        # auth endpoint returns JWT token that is then used with subsequent requests
                                        # it uses the identity function to verify the token 

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
        type=float,
        required=True,
        help="The field can not be left blank"
        )

    @jwt_required()
    def get(self, name):
        # return {'item': next(filter(lambda x: x['name'] == name, items), None)}
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404
    
    def post(self, name):
           # data = request.get_json()
        data = Item.parser.parse_args()

        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "Item with name '{}' already exists.".format(name)}, 400
     
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201
    
    def delete(self, name):
        global items
        newItemList = filter(lambda x: x['name'] != name, items)
        items = newItemList
        return {'message': 'Item deleted'}
    
    def put(self, name):
        
        data = Item.parser.parse_args()
       # data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item



class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')

app.run(port=5000, debug=True)