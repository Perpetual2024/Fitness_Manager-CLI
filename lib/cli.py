# lib/cli.py

from helpers import (
    exit_program,
    add_category
)
from database.app import create_tables


def main():
    create_tables()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_category()
        elif choice == "2":
            add_exercises()
        elif choice == "3":
            view_exercises()
        elif choice == "4":
            delete_exercises()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a new category")
    print("2. Add a new exercise")
    print("3. view your exercise from category")
    print("4. Delete outdated exercises")


if __name__ == "__main__":
    main()
