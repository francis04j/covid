from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from item import Item, ItemList
from security import authenticate, identity
from userRegister import UserRegister


app = Flask(__name__)
app.secret_key="francis"
api = Api(app)

jwt=JWT(app, authenticate, identity)    # new JWT object that creates /auth endpoint
                                        # auth endpoint returns JWT token that is then used with subsequent requests
                                        # it uses the identity function to verify the token 

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__': 
    app.run(port=5000, debug=True)