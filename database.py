import sqlite3

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        pages INTEGER,
        current_page INTEGER
    )
""")
