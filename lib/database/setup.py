import sqlite3


def create_tables():
    conn = sqlite3.connect("fitness_manager.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS categories (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL)""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS exercises (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   details TEXT,
                   category_id INTEGER,
                   FOREIGN KEY (category_id) REFERENCES categories(id))""")

    conn.commit()
    conn.close()
    print("Database setup complete")

if  __name__ == "__main__" : 
    create_tables()  # Call the function to create the tables
