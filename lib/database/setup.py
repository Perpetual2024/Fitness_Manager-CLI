from .connection import get_db_connection



def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS categories (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL)""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS exercises (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   detail TEXT,
                   category_id INTEGER,
                   FOREIGN KEY (category_id) REFERENCES categories(id))""")

    conn.commit()
    conn.close()
