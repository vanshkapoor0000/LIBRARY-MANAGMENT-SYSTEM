"""
Data persistence handler for reading and writing JSON files.
"""
import json
from pathlib import Path
from typing import List
from models import Book


class StorageManager:
    """Manages file storage operations for book records."""

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        """Ensures the target directory and data file exist."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.save_books([])

    def load_books(self) -> List[Book]:
        """Loads and deserializes book records from disk."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_books(self, books: List[Book]) -> None:
        """Serializes and saves book records to disk."""
        data = [book.to_dict() for book in books]
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)