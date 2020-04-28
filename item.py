import sqlite3
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt import jwt_required

from userRegister import UserRegister

class Item(Resource):
    TABLE_NAME = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('price', 
        type=float,
        required=True,
        help="The field can not be left blank"
        )

    @classmethod
    def find_by_name(cls, name):    #cls cos it's a class method with a less
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM Items where name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
    
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

        # return {'item': next(filter(lambda x: x['name'] == name, items), None)}
        # item = next(filter(lambda x: x['name'] == name, items), None)
        # return {'item': item}, 200 if item else 404
    
    def post(self, name):
           # data = request.get_json()
        # data = Item.parser.parse_args()

        # if next(filter(lambda x: x['name'] == name, items), None):
        #     return {'message': "Item with name '{}' already exists.".format(name)}, 400
        if self.find_by_name(name):
            return {'message': "Item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()  
        item = {'name': name, 'price': data['price']}
        
        try:
            Item.insert(item)
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item, 201
    
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}
    
    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}
        if item is None:
            try:
                Item.insert(updated_item)
            except:
                return {"message": "An error occurred inserting the item."}
        else:
            try:
                Item.update(updated_item)
            except:
                return {"message": "An error occurred updating the item."}
        return updated_item



class ItemList(Resource):
    TABLE_NAME = 'items'
    
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        connection.close()

        return {'items': items}
