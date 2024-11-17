import sqlite3

book_conn = sqlite3.connect('bookstore.db')
user_conn = sqlite3.connect('users.db')

book_cursor = book_conn.cursor()
user_cursor = user_conn.cursor()

# book_cursor.executemany('''
#     INSERT INTO Books (title, author, genre, price, stock) VALUES (?, ?, ?, ?, ?)
# ''', [
#     ("Pride and Prejudice", "Jane Austen", "Romance", 9.99, 5),
#     ("To Kill a Mockingbird", "Harper Lee", "Fiction", 7.99, 3),
#     ("1984", "George Orwell", "Science Fiction", 11.99, 8),
#     ("Harry Potter and the Philosopher's Stone",
#      "J.K. Rowling", "Fantasy", 12.99, 6),
#     ("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 10.99, 4),
#     ("The Catcher in the Rye", "J.D. Salinger", "Fiction", 6.99, 2),
#     ("War and Peace", "Leo Tolstoy", "Historical Fiction", 14.99, 7),
#     ("The Hobbit", "J.R.R. Tolkien", "Fantasy", 8.99, 5),
#     ("The Da Vinci Code", "Dan Brown", "Thriller", 9.99, 3),
#     ("The Lion, the Witch and the Wardrobe", "C.S. Lewis", "Fantasy", 7.99, 1),
#     ("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy", 19.99, 10),
#     ("The Kite Runner", "Khaled Hosseini", "Historical Fiction", 11.99, 6),
#     ("The Landing Place", "Chad Ganske", "Fiction", 9.99, 4),
# ])

user_cursor.execute('''
    CREATE TABLE Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
''')

user_cursor.executemany('''
    INSERT INTO Users (username, password) VALUES (?, ?)
''', [
    ("vaishnavi", "password"),
])


user_conn.commit()
user_conn.close()

book_conn.commit()
book_conn.close()
