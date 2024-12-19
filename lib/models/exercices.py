import sqlite3
from database.connection import get_db_connection


class Exercises():

    all = {} 

    def __init__(self,name, details, category_id, id=None ):
        self.name = name
        self.details = details
        self.category_id = category_id
        self.id = id

    def __repr__(self): 
        return f"Exercises('{self.name}', '{self.details}', '{self.category_id}')"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        else:
            self._name = value

    @property 
    def details(self, add_details):
        if isinstance (add_details, str):
            if len(add_details) > 0:
                self._details = add_details
        else:
            raise TypeError("Details must be a string and not empty")
        

    @property
    def category_id(self):
        return self._category_id
        
    def save(self) :
        conn = get_db_connection
        cursor = conn.cursor()
        sql ="""


        INSERT INTO TABLE exercises (name, details, category_id) 
                     VALUES (?, ?, ?)"""
        
        cursor.execute(sql, (self.name, self.details, self.category_id,))
        conn.commit ()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        conn.close()

    
    def delete(self):
        conn = get_db_connection
        cursor = conn.cursor()
        sql = """
        DELETE FROM exercises WHERE id = ?"""
        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]
        conn.close()

    @classmethod 
    def fetch_all(cls):
        conn = get_db_connection
        cursor = conn.cursor()
        sql = """SELECT * FROM exercises"""
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:#loop
            excercise = cls(id=row[0], name=row[1], details=row[2], category_id=row[3])
            cls.all[row[0]] = excercise #index for the id
        conn.close() 

    @classmethod
    def fetch_by_category(cls, category_id):
        conn = get_db_connection
        cursor = conn.cursor()
        sql = """SELECT * FROM exercises WHERE category_id = ?"""
        cursor.execute(sql, (category_id,))
        rows = cursor.fetchall()
        exercises = []

        for row in rows:
            excercise = cls(id=row[0], name=row[1], details=row[2], category_id=[3])
            exercises.append(excercise)
        conn.close() 
        return exercises   
            




        
                     
    

        
