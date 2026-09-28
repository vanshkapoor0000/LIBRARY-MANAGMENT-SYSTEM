"""
Command-Line Interface (CLI) presentation layer and entry point.
"""
import config
from storage import StorageManager
from library import LibraryService


def print_header(title: str) -> None:
    print(f"\n--- {title} ---")


def prompt_add_book(service: LibraryService) -> None:
    print_header("Add New Book")
    book_id = input("Enter Book ID: ").strip()
    if not book_id:
        print("Error: Book ID cannot be empty.")
        return

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    if not title or not author:
        print("Error: Title and Author cannot be empty.")
        return

    success, message = service.add_book(book_id, title, author)
    print(message)


def prompt_view_books(service: LibraryService) -> None:
    books = service.get_all_books()
    if not books:
        print("\nNo books available.")
        return

    print_header("Library Books")
    for book in books:
        print(f"ID:     {book.id}")
        print(f"Title:  {book.title}")
        print(f"Author: {book.author}")
        print(f"Status: {book.status_string()}")
        print("-" * 20)


def prompt_search_book(service: LibraryService) -> None:
    book_id = input("\nEnter Book ID to search: ").strip()
    book = service.find_book(book_id)

    if book:
        print("\nBook Found!")
        print(f"ID:     {book.id}")
        print(f"Title:  {book.title}")
        print(f"Author: {book.author}")
        print(f"Status: {book.status_string()}")
    else:
        print("Book not found.")


def prompt_issue_book(service: LibraryService) -> None:
    book_id = input("\nEnter Book ID to issue: ").strip()
    _, message = service.issue_book(book_id)
    print(message)


def prompt_return_book(service: LibraryService) -> None:
    book_id = input("\nEnter Book ID to return: ").strip()
    _, message = service.return_book(book_id)
    print(message)


def main() -> None:
    storage = StorageManager(config.DATA_FILE)
    service = LibraryService(storage)

    actions = {
        "1": lambda: prompt_add_book(service),
        "2": lambda: prompt_view_books(service),
        "3": lambda: prompt_search_book(service),
        "4": lambda: prompt_issue_book(service),
        "5": lambda: prompt_return_book(service),
    }

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "6":
            print("Thank you for using the Library Management System!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()