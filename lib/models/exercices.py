from database.connection import get_db_connection


class Exercises:

    all = {}

    def __init__(self, name, details, category_id, id=None):
        self.id = id
        self.name = name
        self.details = details
        self.category_id = category_id

    def __repr__(self):
        return f"Exercises('{self.id}', '{self.name}', '{self.details}', '{self.category_id}')"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Details must be a non-empty string.")
        self._details = value

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Category ID must be an integer.")
        self._category_id = value

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            sql = """
            INSERT INTO exercises (name, details, category_id) 
            VALUES (?, ?, ?)"""
            cursor.execute(sql, (self.name, self.details, self.category_id))
            self.id = cursor.lastrowid
            type(self).all[self.id] = self
        else:
            sql = """
            UPDATE exercises 
            SET name = ?, details = ?, category_id = ? 
            WHERE id = ?"""
            cursor.execute(sql, (self.name, self.details, self.category_id, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is None:
            raise ValueError("Exercise does not exist in the database.")
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """DELETE FROM exercises WHERE id = ?"""
        cursor.execute(sql, (self.id,))
        conn.commit()
        conn.close()
        if self.id in type(self).all:
            del type(self).all[self.id]

    @classmethod
    def fetch_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """SELECT * FROM exercises"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close()

        exercises = []
        for row in rows:
            exercise = cls(id=row[0], name=row[1], details=row[2], category_id=row[3])
            exercises.append(exercise)
            cls.all[row[0]] = exercise
        return exercises

    @classmethod
    def fetch_by_category(cls, category_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """SELECT * FROM exercises WHERE category_id = ?"""
        cursor.execute(sql, (category_id,))
        rows = cursor.fetchall()
        conn.close()

        exercises = []
        for row in rows:
            exercise = cls(id=row[0], name=row[1], details=row[2], category_id=row[3])
            exercises.append(exercise)
        return exercises

    @classmethod
    def fetch_by_id(cls, id):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """SELECT * FROM exercises WHERE id = ?"""
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row[0], name=row[1], details=row[2], category_id=row[3])
        return None



        
                     
    

        
