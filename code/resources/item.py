from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
          return item
        
        return {'message': 'Item not found'}, 404
    
    @jwt_required()
    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'message': "An item with name '{}' already exists".format(name)}, 400
            
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}

        item = ItemModel.insert(item)

        return item, 201
    
    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            delete_query = "DELETE FROM items WHERE name=?"
            
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            cursor.execute(delete_query, (name,))
            
            connection.commit()
            connection.close()
            
            return {'message': 'Item deleted'}

        return {'message': 'Item does not exist'}, 404
    
    @jwt_required()
    def put(self, name):
        item = ItemModel.find_by_name(name)
        
        data = Item.parser.parse_args()
        updated_item = {'name': name, 'price': data['price']}

        if item:
            try:
                ItemModel.update(updated_item)
            except:
                return {'message': 'An error occurred updating the item'}, 500
        
            return updated_item, 200
        else:
            try:
                ItemModel.insert(updated_item)
            except:
                return {'message': 'An error occurred inserting the item'}, 500
        
            return updated_item, 201

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()
        
        return {'items': items}
