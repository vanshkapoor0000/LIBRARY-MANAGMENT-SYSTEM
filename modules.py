"""
Data model definitions for the Library Management System.
"""
from typing import Dict, Any


class Book:
    """Represents an individual book entity in the system."""

    def __init__(self, book_id: str, title: str, author: str, available: bool = True):
        self.id = book_id
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self) -> Dict[str, Any]:
        """Serializes the Book object into a dictionary for storage."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "available": self.available,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Book":
        """Deserializes a dictionary into a Book instance."""
        return cls(
            book_id=str(data["id"]),
            title=data["title"],
            author=data["author"],
            available=data.get("available", True),
        )

    def status_string(self) -> str:
        """Returns human-readable availability status."""
        return "Available" if self.available else "Issued"