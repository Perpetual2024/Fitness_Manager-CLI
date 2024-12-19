# lib/helpers.py
import sqlite3
from models.categories import get_connection

def add_category():
    name = input("Enter category name: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    print(f"Category {name} added successfully.")




def exit_program():
    print("Goodbye!")
    exit()
