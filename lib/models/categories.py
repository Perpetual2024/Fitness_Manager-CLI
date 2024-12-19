
import sqlite3

from database.connection import get_db_connection

class Categories:
    all = {}#this is a dict that will hold all the categories by there (id)

    def __init__(self, name , id= None): #this is the initialization
        self.id = id
        self.name = name
        

    def __repr__(self):
        return f"<Categories {self.id}: {self.name}>" #making sure that when we print a category it will look like this as strings

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        if len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Name cannot be empty")
        
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
                INSERT INTO categories (name) 
                VALUES (?)
"""

        cursor.execute(sql, (self.name,)) 
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        conn.close()

    @classmethod
    def create(cls, name):
        category = cls(name)
        category.save()
        return category
    
    def get_category_id(self):
        return self.id

