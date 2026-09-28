"""
Core business logic module handling book operations and updates.
"""
from typing import Optional, List, Tuple
from models import Book
from storage import StorageManager


class LibraryService:
    """Executes business logic for book management."""

    def __init__(self, storage: StorageManager):
        self.storage = storage
        self.books: List[Book] = self.storage.load_books()

    def add_book(self, book_id: str, title: str, author: str) -> Tuple[bool, str]:
        """Registers a new book in the system."""
        if self.find_book(book_id) is not None:
            return False, f"Book with ID '{book_id}' already exists."

        new_book = Book(book_id=book_id, title=title, author=author)
        self.books.append(new_book)
        self.storage.save_books(self.books)
        return True, "Book added successfully!"

    def get_all_books(self) -> List[Book]:
        """Returns all books stored in the library."""
        return self.books

    def find_book(self, book_id: str) -> Optional[Book]:
        """Retrieves a book by its unique ID."""
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def issue_book(self, book_id: str) -> Tuple[bool, str]:
        """Changes a book's availability status to Issued."""
        book = self.find_book(book_id)
        if not book:
            return False, "Book not found."
        if not book.available:
            return False, "Book is already issued."

        book.available = False
        self.storage.save_books(self.books)
        return True, "Book issued successfully!"

    def return_book(self, book_id: str) -> Tuple[bool, str]:
        """Changes a book's availability status to Available."""
        book = self.find_book(book_id)
        if not book:
            return False, "Book not found."
        if book.available:
            return False, "This book was not issued."

        book.available = True
        self.storage.save_books(self.books)
        return True, "Book returned successfully!"