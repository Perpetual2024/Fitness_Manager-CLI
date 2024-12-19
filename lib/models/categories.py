
import sqlite3


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
