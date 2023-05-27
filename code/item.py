from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404
    
    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201
    
    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
    
        return {'message': 'Item deleted'}
    
    @jwt_required()
    def put(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        data = Item.parser.parse_args()

        if item:
            item.update(data)
        else:
            item = {'name': name, 'price': data['price']}
            items.append(item)

        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}
