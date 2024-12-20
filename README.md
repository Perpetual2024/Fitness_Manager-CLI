# Phase 3 CLI+ORM Project Template
### INTRODUCTION
This is a command-line interface (CLI) application for managing simple fitness routines .

By Perpetual Akinyi Odhiambo

### DESCRIPTION
The Fitness Tracker CLI Application is a Python-based command-line interface program that allows users to manage their fitness routines. Users can:

   - Create and manage categories of exercises (e.g., Cardio, Strength, Flexibility).

   - Add, list, update, and delete exercises under specific categories.

   - View exercises by category.

This application is built using object-oriented programming principles, SQLite for database management, and provides a simple and intuitive CLI for interaction.

### FEATURES
 ## Category Management
   - Add a new category
   - List all categories
   - List exercises by category
   - Delete a category
 ##  Exercises Management
   - Add a new exercise
   - List all exercises
   - Assign an exercise to a category
   - Delete an exercise

### TECHNOLOGIES 
- Python : Programming language
- SQLite
- Object-Oriented Programming (OOP)

###  INSTALLATION AND SETUP
1. Clone the repository
   git clone <repository_url>
   cd <repository_name>
   code .

2.  Set up Virtual Environment
- To set up run the following comands
     ```bash
     pipenv install
     pipenv shell
     

3.  Run the application
- In your terminal run the following command
    ```bash
     python lib/cli.py

### USAGE
- Run the application
On the CLI, you will be presented with a menu to choose from the following options:

  0. Exit program
  1. Add a new category
  2. List all categories
  3. Add a new exercise
  4. List exercises by category
  5. List all exercises
  6. Delete an exercise
  7. Delete a category

  You pick the choice by inserting the number of your desired choice.
  You will be prompted to enter the required information.
  You can view the outputs on the SQLIte database file or the CLI.

  ### PROJECT STRUCTURE
    ```bash
    Fitness_Manager
    ├── github/                    # Optional folder for GitHub-related files (e.g., actions, templates)
    │
    ├── lib/                        # Library files
    │   ├── __pycache__/            # Compiled Python files (ignored by Git)
    │   ├── database/               # Database-related functionality
    │   │   ├── __pycache__/        # Compiled files (ignored)
    │   │   ├── connection.py       # Task management functionality
    │   │   └── setup.py            # User management functionality
    │
    ├── models/                     # Models for different entities
    │   ├── categories.py           # Defines task categories (task management functionality)
    │   └── exercise.py             # Defines exercises (user management functionality)
    │
    ├── cli.app                     # CLI logic for interacting with the app
    ├── debug.py                    # SQLite database file (if applicable, can be renamed to database.py)
    ├──fitness_manager.db           # You can view your cli inputs on this SQLite database file
    ├── Pipfile                     # Dependencies and virtual environment setup
    ├── Pipfile.lock                # Dependency lock file  
    ├── README.md                   # Documentation about the project

## AUTHOR
Name Perpetual Akinyi Odhiambo

### CONTACTS
You can reach me at 
- Github : [Perpetual Akinyi Odhiambo](https://github.com/Perpetual2024)
 - Email: [akinyiperpetual2@gmail.com](mailto:perpetualakinyi)
 - Phone: +254 721 12 66 98

### Contributions
 Fell free to contribute or reach out for any inquiries with my contact info placed.
   
### LICENSE
This project is licensed under MIT License.
Copyright &copy; 2024 Perpetual Akinyi Odhiambo. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

   