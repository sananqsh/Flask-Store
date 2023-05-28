from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

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
          return item.json()
        
        return {'message': 'Item not found'}, 404
    
    @jwt_required()
    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'message': "An item with name '{}' already exists".format(name)}, 400
            
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])

        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500

        return item.json(), 201
    
    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted'}

        return {'message': 'Item does not exist'}, 404
    
    @jwt_required()
    def put(self, name):
        item = ItemModel.find_by_name(name)        
        data = Item.parser.parse_args()

        status_code = 200
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, data['price'])
            status_code = 201
        
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500
    
        
        return item.json(), status_code

class ItemList(Resource):
    def get(self):
        result = ItemModel.all()
        return {'items': [item.json() for item in result]}
