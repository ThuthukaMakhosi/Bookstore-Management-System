# Bookstore Management System

## Description
This Python program helps a bookstore clerk efficiently manage the store’s book inventory using **SQLite** for persistent storage. It provides a console-based interface to perform key operations, including adding, updating, deleting, and searching for books.

## Features
- **Add new books**: Store details such as title, author, ISBN, price, and quantity.  
- **Update book information**: Modify existing book details to keep inventory accurate.  
- **Delete books**: Remove books from the inventory when they are no longer available.  
- **Search for books**: Quickly locate books by title, author, or ISBN.  
- **SQLite integration**: All book data is stored in a SQLite database, allowing persistent storage and easy querying.  

## Requirements
- Python 3.x  
- VS Code or any Python IDE  
- `sqlite3` module (built-in with Python)  

## How to Run
1. Open the project folder in VS Code or any IDE.  
2. Ensure `books.db` (or your database file) is in the same directory as `bookstore.py`.  
3. Run the program:
   ```bash
   python bookstore.py
