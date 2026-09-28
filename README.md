Library Management System

A simple Python-based console application for managing books in a library. The system allows users to add, view, search, issue, and return books through an interactive menu.

Features

Add new books with Book ID, title, and author.

View all books and their availability status.

Search for a book using its Book ID.

Issue an available book.

Return an issued book.

Exit the application safely.

Uses Python lists and dictionaries for data storage.

Technologies Used

Python 3

Python built-in functions and data structures

No external libraries or dependencies are required.

Project Structure
Library-Management-System/
│
├── library.py
└── README.md

Requirements

Before running the project, make sure you have:

Python 3.7 or later installed.

A terminal/command prompt.

A text editor or Python IDE such as VS Code, PyCharm, or IDLE.

No database, third-party package, or internet connection is required.

Step 1: Install Python

Download and install Python 3 from the official Python website.

After installation, verify that Python is available by opening a terminal or command prompt and running:

python --version


On some systems, use:

python3 --version


You should see a Python 3 version number, for example:

Python 3.x.x

Step 2: Get the Project

Download or clone this project to your computer.

If you are using Git:

git clone <repository-url>


Then move into the project directory:

cd Library-Management-System


If you downloaded the project as a ZIP file, extract it and open the extracted project folder in your terminal or IDE.

Step 3: Environment Setup

This project does not require a virtual environment because it uses only Python's built-in features.

However, you can optionally create one.

Windows
python -m venv venv
venv\Scripts\activate

macOS/Linux
python3 -m venv venv
source venv/bin/activate

Step 4: Install Dependencies

There are no external dependencies required for this project.

Therefore, no pip install command is necessary.

If the project is extended in the future and a requirements.txt file is added, dependencies can be installed with:

pip install -r requirements.txt

Step 5: Configuration

No configuration file, database, API key, environment variable, or external service is required.

The application stores book information temporarily in a Python list while the program is running.

Important: Book data is stored in memory and will be lost when the program is closed.

Step 6: Run the Application

Make sure you are inside the project directory.

Run the program using:

python library.py


On macOS/Linux, you may need:

python3 library.py


The application will display the main menu:

===== LIBRARY MANAGEMENT SYSTEM =====
1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Exit

Enter your choice:

Step 7: Using the Application
1. Add Book

Select option 1.

Enter:

Book ID

Book Title

Author Name

The book will be added with an Available status.

2. View Books

Select option 2 to display all books stored in the system.

Each book displays:

ID

Title

Author

Status

3. Search Book

Select option 3 and enter the Book ID.

If the book exists, its details and current status will be displayed.

4. Issue Book

Select option 4 and enter the Book ID.

If the book is available, its status changes to Issued.

If it has already been issued, the system displays an appropriate message.

5. Return Book

Select option 5 and enter the Book ID.

If the book is currently issued, its status changes back to Available.

6. Exit

Select option 6 to close the application.

Example
===== LIBRARY MANAGEMENT SYSTEM =====
1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Exit

Enter your choice: 1

Enter Book ID: B101
Enter Book Title: Python Programming
Enter Author Name: John Smith

Book added successfully!


You can then select View Books to see:

--- Library Books ---
ID: B101
Title: Python Programming
Author: John Smith
Status: Available
--------------------

Data Storage

The application uses a Python list called books to store book records.

Each book is represented as a dictionary containing:

{
    "id": "B101",
    "title": "Python Programming",
    "author": "John Smith",
    "available": True
}


The available value is:

True when the book is available.

False when the book is issued.

Troubleshooting
Python command not found

If the terminal reports that Python is not recognized, install Python and make sure it is added to your system's PATH.

File not found

Make sure you are running the command from the directory containing library.py.

You can check the files in the current directory with:

dir


on Windows, or:

ls


on macOS/Linux.

No books appear after restarting

This is expected. The current version stores data only in memory and does not use a database or permanent file storage.

