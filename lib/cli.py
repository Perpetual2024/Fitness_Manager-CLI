# lib/cli.py
from models.categories import Categories
from models.exercices import Exercises
from database.connection import get_db_connection


def add_category():
    """Add a new category using the Categories model."""
    name = input("Enter category name: ")
    try:
        category = Categories.create(name)
        print(f"Category '{category.name}' added with ID {category.id}.")
    except ValueError as e:
        print(f"Error: {e}")

def list_categories():
    """List all categories using the Categories model."""
    categories = Categories.fetch_all_categories()
    if categories:
        print("\nCategories:")
        for category in categories:
            print(f"ID: {category.id}, Name: {category.name}")
    else:
        print("No categories found.")

def delete_category():
    """Delete a category using the Categories model."""
    category_id = input("Enter category ID to delete: ")
    try:
        category = Categories.fetch_category_by_id(int(category_id))
        if category:
            category.delete()
            print(f"Category ID {category_id} deleted.")
        else:
            print(f"Category ID {category_id} not found.")
    except ValueError as e:
        print(f"Error: {e}")        


def add_exercise():
    name = input("Enter exercise name: ")
    details = input("Enter exercise details: ")
    category_id = int(input("Enter category ID: "))
    try:
        exercise = Exercises(name=name, details=details, category_id=category_id)
        exercise.save()
        print(f"Exercise '{exercise.name}' added to category ID {exercise.category_id}.")
    except ValueError as e:
        print(f"Error: {e}")

def list_exercises_by_category():
    category_id = int(input("Enter category ID: "))
    exercises = Exercises.fetch_by_category(category_id)
    if exercises:
        print(f"\nExercises in category ID {category_id}:")
        for exercise in exercises:
            print(f"ID: {exercise.id}, Name: {exercise.name}, Details: {exercise.details}")
    else:
        print(f"No exercises found for category ID {category_id}.")

def list_all_exercises():
    exercises = Exercises.fetch_all()
    if exercises:
        print("\nAll Exercises:")
        for exercise in exercises:
            print(f"ID: {exercise.id}, Name: {exercise.name}, Details: {exercise.details}, Category ID: {exercise.category_id}")
    else:
        print("No exercises found.")

def delete_exercise():
    exercise_id = int(input("Enter exercise ID to delete: "))
    exercise = Exercises.fetch_by_id(exercise_id)
    if exercise:
        exercise.delete()
        print(f"Exercise ID {exercise_id} deleted.")
    else:
        print(f"Exercise ID {exercise_id} not found.")

def menu():
    print("\nPlease select an option:")
    print("0. Exit the program")
    print("1. Add a new category")
    print("2. List all categories")
    print("3. Add a new exercise")
    print("4. List exercises by category")
    print("5. List all exercises")
    print("6. Delete an exercise")
    print("7. Delete a category")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            add_category()
        elif choice == "2":
            list_categories()
        elif choice == "3":
            add_exercise()
        elif choice == "4":
            list_exercises_by_category()
        elif choice == "5":
            list_all_exercises()
        elif choice == "6":
            delete_exercise()
        elif choice == "7":
            delete_category()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
