import sqlite3

class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}   

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
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        insert_query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(insert_query, (item['name'], item['price']))
        
        connection.commit()
        connection.close()

        return item
    
    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        insert_query = "UPDATE items SET name=?, price=? WHERE name=?"
        cursor.execute(insert_query, (item['name'], item['price'], item['name']))
        
        connection.commit()
        connection.close()

        return item