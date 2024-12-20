
import sqlite3
from database.connection import get_db_connection

class Categories:
    all = {}  # Dictionary to store all categories by their IDs

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Categories {self.id}: {self.name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Name cannot be empty")

    def save(self):
        """Save a new category to the database."""
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
        """Create a new category."""
        category = cls(name)
        category.save()
        return category

    @classmethod
    def fetch_category_by_id(cls, id):
        """Fetch a category by its ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """SELECT * FROM categories WHERE id = ?"""
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            category = cls(name=row[1], id=row[0])
            cls.all[row[0]] = category
            return category
        return None

    @classmethod
    def fetch_all_categories(cls):
        """Fetch all categories from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """SELECT * FROM categories"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close()

        categories = []
        for row in rows:
            category = cls(name=row[1], id=row[0])
            categories.append(category)
            cls.all[row[0]] = category
        return categories

    def update(self, new_name):
        """Update the category name."""
        self.name = new_name  # Validate with the property setter
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """UPDATE categories SET name = ? WHERE id = ?"""
        cursor.execute(sql, (self.name, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        """Delete the category."""
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """DELETE FROM categories WHERE id = ?"""
        cursor.execute(sql, (self.id,))
        conn.commit()
        conn.close()

        if self.id in type(self).all:
            del type(self).all[self.id]
