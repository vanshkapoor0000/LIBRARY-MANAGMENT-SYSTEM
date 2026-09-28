# Project Statement & Scope

## Problem Statement

Traditional manual record-keeping for small libraries or personal book collections often leads to inefficiencies, human error, and difficulty in tracking book availability. Tracking which books are currently checked out versus available can become confusing without a structured tool. Furthermore, full-scale library management enterprise software is often overly complex, heavy, and requires elaborate database installations for simple or educational use cases.

There is a need for a lightweight, accessible, and intuitive terminal-based application that allows users to seamlessly catalog, search, check out, and return books without setup overhead.

## Scope of the Project

### In-Scope
* **CLI Interface**: Providing an interactive command-line interface with menu-based navigation.
* **Core Inventory Operations**: Ability to register new books into the collection using unique identifiers (Book ID, Title, Author).
* **Search & View Functionality**: Browsing the complete library directory and searching for specific titles by Book ID.
* **Circulation Handling**: Updating status transitions for borrowing (issuing) and returning books with availability validation.
* **In-Memory Operations**: Managing state efficiently using standard Python data structures during runtime execution.

### Out-of-Scope
* **Persistent Storage**: Integration with external databases (e.g., PostgreSQL, SQLite) or persistent flat files (JSON, CSV).
* **User Authentication**: User login systems, role-based access control (e.g., differentiating between Admin and Patron roles).
* **Advanced Lending Logic**: Tracking due dates, late return fines, reservation queues, or user borrowing limits.
* **Graphical User Interface (GUI) / Web Interface**: Desktop windows or browser interfaces.

## Target Users

1. **Small Library Administrators / Librarians**: Individuals looking for a lightweight system to manage small physical book collections or temporary catalogs.
2. **Students & Educators**: Learners and teachers seeking a practical, clear example of core Python concepts (data structures, functions, control loops, and interactive terminal interfaces).
3. **Developers & Evaluators**: Software reviewers analyzing standard CLI application architecture and basic algorithmic logic in Python.

## High-Level Features

* **Book Registration & Cataloging**: Input unique IDs, titles, and authors to instantly register new entries with an initial status of `Available`.
* **Catalog Inventory Inspection**: View all registered books at once, along with their live availability status (`Available` or `Issued`).
* **Book ID Lookup**: Fast retrieval of detailed book information by entering a target Book ID.
* **Circulation Management**:
  * **Issue Book**: Prevents duplicate issuing by checking current availability before changing status to `Issued`.
  * **Return Book**: Revalidates status to ensure only currently issued books can be returned to `Available` status.
* **Interactive Terminal Loop**: A robust command loop that prompts users for input and handles invalid menu selections gracefully.