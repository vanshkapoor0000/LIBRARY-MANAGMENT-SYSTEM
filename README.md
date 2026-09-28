# Library Management System

## 1. Project Title

**Library Management System (CLI)**

## 2. Project Overview

The Library Management System is a command-line application developed in Python for managing books in a library.

The system allows users to add books, view all available books, search for a specific book, issue books, and return books. Book data is managed through a storage layer so that library information can be persisted between program runs.

The application follows a layered structure with separate components for:

- **CLI / Presentation Layer** – Handles user interaction and menu display.
- **Library Service Layer** – Handles library operations and business logic.
- **Storage Layer** – Handles saving and retrieving book data.

## 3. Features

The system provides the following features:

### Add Book
- Add a new book using a unique Book ID.
- Enter the book title and author name.
- Validates that required fields are not empty.

### View Books
- Display all books stored in the library.
- Shows:
  - Book ID
  - Book Title
  - Author
  - Current Status

### Search Book
- Search for a book using its Book ID.
- Displays the book's details if it exists.
- Displays an appropriate message if the book is not found.

### Issue Book
- Issue a book using its Book ID.
- Updates the book's availability status.

### Return Book
- Return a previously issued book using its Book ID.
- Updates the book's availability status.

### Exit
- Safely exit the application through the menu.

## 4. Technologies and Tools Used

| Technology / Tool | Purpose |
|---|---|
| Python 3 | Main programming language |
| Command Line Interface (CLI) | User interaction |
| File Storage | Persistent storage of library data |
| Python Modules | Organizing application components |

### Project Modules

The application uses the following Python modules:

- `config.py` – Stores application configuration such as the data file location.
- `storage.py` – Provides the `StorageManager` for data storage and retrieval.
- `library.py` – Provides the `LibraryService` containing library business logic.
- `main.py` – Provides the CLI interface and application entry point.

## 5. Installation and Setup

### Prerequisites

Make sure Python 3 is installed on your computer.

Check the Python version using:

```bash
python --version
```

or, depending on your system:

```bash
python3 --version
```

### Step 1: Clone or Download the Project

Download the project files or clone the project repository.

Example:

```bash
git clone <repository-url>
```

Then move into the project directory:

```bash
cd <project-directory>
```

### Step 2: Check the Project Files

Make sure the project contains the required Python modules, for example:

```text
project/
│
├── main.py
├── config.py
├── storage.py
├── library.py
├── README.md
└── ...
```

### Step 3: Configure the Data File

The application uses:

```python
config.DATA_FILE
```

to determine where library data is stored.

Make sure `config.py` defines the required `DATA_FILE` path.

### Step 4: Run the Application

Run the main Python file:

```bash
python main.py
```

or:

```bash
python3 main.py
```

The application will display the Library Management System menu.

## 6. How to Use the Application

After starting the program, the following menu is displayed:

```text
===== LIBRARY MANAGEMENT SYSTEM =====
1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Exit
Enter your choice (1-6):
```

Enter the corresponding number to perform an operation.

### Adding a Book

Select:

```text
1
```

Then enter:

```text
Book ID
Book Title
Author Name
```

The system validates that the Book ID, title, and author are not empty.

### Viewing Books

Select:

```text
2
```

The system displays all books and their current status.

### Searching for a Book

Select:

```text
3
```

Enter the Book ID to search for the book.

### Issuing a Book

Select:

```text
4
```

Enter the Book ID of the book that should be issued.

### Returning a Book

Select:

```text
5
```

Enter the Book ID of the book that should be returned.

### Exiting

Select:

```text
6
```

The application will display:

```text
Thank you for using the Library Management System!
```

and terminate.

## 7. Testing Instructions

Testing should verify that each major feature works correctly and that invalid inputs are handled properly.

### Test 1: Add a Valid Book

1. Run the application.
2. Select option `1`.
3. Enter a valid Book ID.
4. Enter a book title.
5. Enter an author name.
6. Verify that the book is successfully added.

Example:

```text
Enter Book ID: B001
Enter Book Title: Python Programming
Enter Author Name: John Smith
```

### Test 2: Add a Book with Empty Book ID

1. Select option `1`.
2. Leave the Book ID empty.
3. Verify that the system displays:

```text
Error: Book ID cannot be empty.
```

### Test 3: Add a Book with Empty Title or Author

1. Select option `1`.
2. Enter a valid Book ID.
3. Leave the title or author empty.
4. Verify that the system displays:

```text
Error: Title and Author cannot be empty.
```

### Test 4: View Books

1. Add one or more books.
2. Select option `2`.
3. Verify that all stored books are displayed with their ID, title, author, and status.

### Test 5: Search for an Existing Book

1. Select option `3`.
2. Enter the ID of an existing book.
3. Verify that the correct book details are displayed.

### Test 6: Search for a Non-Existing Book

1. Select option `3`.
2. Enter an ID that does not exist.
3. Verify that the system displays:

```text
Book not found.
```

### Test 7: Issue a Book

1. Select option `4`.
2. Enter the ID of an available book.
3. Verify that the book's status changes to the issued/unavailable state.

### Test 8: Return a Book

1. Select option `5`.
2. Enter the ID of an issued book.
3. Verify that the book's status changes back to the available state.

### Test 9: Invalid Menu Choice

1. Enter an invalid menu option such as `7` or `abc`.
2. Verify that the system displays:

```text
Invalid choice. Please try again.
```

### Test 10: Exit the Application

1. Select option `6`.
2. Verify that the application displays the exit message and terminates correctly.

## 8. Expected Result

After successful testing, the application should:

- Allow valid books to be added.
- Prevent empty required fields.
- Display stored books correctly.
- Search books using their IDs.
- Allow available books to be issued.
- Allow issued books to be returned.
- Handle invalid menu choices.
- Exit without errors.
- Preserve library data according to the configured storage mechanism.

## 9. Conclusion

The Library Management System provides a simple command-line interface for performing common library operations. Its separation into presentation, service, and storage components makes the application easier to maintain, test, and extend in the future.
