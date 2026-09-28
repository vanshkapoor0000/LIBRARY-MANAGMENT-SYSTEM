"""
Configuration settings for the Library Management System.
"""
from pathlib import Path

# Base paths for the application
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "books.json"