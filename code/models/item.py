import sqlite3

class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}   

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=? LIMIT 1"

        result = cursor.execute(query, (name,))
        item = result.fetchone()
        connection.close()

        if item:
          return cls(*item)
        
    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        insert_query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(insert_query, (self.name, self.price))
        
        connection.commit()
        connection.close()
    
    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        insert_query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(insert_query, (self.price, self.name))
        
        connection.commit()
        connection.close()
