from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, name):
        item = self.find_by_name(name)

        if item:
          return item
        
        return {'message': 'Item not found'}, 404
    
    @classmethod
    def find_by_name(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=? LIMIT 1"

        result = cursor.execute(query, (name,))
        item = result.fetchone()
        connection.close()

        if item:
          return {'item': {'name': item[0], 'price': item[1]}}
        
    @classmethod
    def insert(self, name, price):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        item = {'name': name, 'price': price}
        
        insert_query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(insert_query, (name, price))
        
        connection.commit()
        connection.close()

        return item
    
    @classmethod
    def update(self, name, price):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        item = {'name': name, 'price': price}
        
        insert_query = "UPDATE items SET name=?, price=? WHERE name=?"
        cursor.execute(insert_query, (name, price, name))
        
        connection.commit()
        connection.close()

        return item
    
    @jwt_required()
    def post(self, name):
        item = self.find_by_name(name)
        if item:
            return {'message': "An item with name '{}' already exists".format(name)}, 400
            
        data = Item.parser.parse_args()
        item = self.insert(name, data['price'])

        return item, 201
    
    @jwt_required()
    def delete(self, name):
        item = self.find_by_name(name)
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
        item = self.find_by_name(name)
        data = Item.parser.parse_args()
        if item:
            item = self.update(name, data['price'])
            return item, 200
        else:
            item = self.insert(name, data['price'])
            return item, 201

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = result.fetchall()
        
        connection.close()
        
        return {'items': items}
