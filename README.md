# Online Bookstore Simulator using Flask & SQLite

# Created by: Vaishnavi Dornala

## Project Overview

This project is an **Online Bookstore** built using **Flask**, a micro web framework for Python. The app allows users to browse a collection of books, search for books by title, add books to their shopping cart, and manage user authentication (login/logout). The data is stored in **SQLite** databases, which are used for storing books and user information.

The project also demonstrates the basics of web development, database interaction, and session management with **Flask-Login**.

---

## Features

1. **User Authentication:**

   - User login functionality.
   - Session management using Flask-Login.
   - Login state displayed in the navbar.
   - Logout functionality.

2. **Book Browsing:**

   - View available books.
   - Search books by title.
   - Add books to the cart.

3. **Shopping Cart:**

   - Add items to the cart.
   - Update cart with book quantities.
   - View cart items in a modal.

4. **Database Interaction:**

   - SQLite database used for storing books and users.
   - Books table holds information about book ID, title, author, price, and stock.
   - Users table stores user credentials (username, password).

---

## Technologies Used

- **Flask**: Python web framework for routing and managing web pages.
- **SQLite**: Lightweight database used for storing books and user data.
- **Flask-Login**: For user session management.
- **HTML**: For creating the web pages.
- **Bootstrap**: CSS framework.

---

## Database Setup

### 1. Books Database (`bookstore.db`)

The database stores all the books in the bookstore. The books table contains the following columns:

- **id**: Integer (Primary Key)
- **title**: Text
- **author**: Text
- **price**: Real (Price of the book)
- **stock**: Integer (Number of copies available)

Sample SQL query to create the `Books` table:

```sql
CREATE TABLE Books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
);
```

### 2. Users Database (`users.db`)

This database stores user data for authentication purposes. The users table contains the following columns:

- **id**: Integer (Primary Key)
- **username**: Text
- **password**: Text (hashed password for security)

Sample SQL query to create the `Users` table:

```sql
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
```

---

## Project Setup and Installation

### Prerequisites

- **Python 3.7+**: Make sure you have Python installed on your system.
- **SQLite**: SQLite should be available by default with Python.

### Steps to Set Up

1. **Install Required Libraries:**

   Install the required Python libraries using `pip`:

   ```bash
   pip install Flask Flask-Login
   ```

2. **Project Structure:**

   The project structure should look like this:

   ```
   project/
   ├── app.py
   ├── templates/
   │   ├── index.html
   │   ├── login.html
   ├── bookstore.db
   ├── users.db
   └── README.md
   ```

   - `app.py`: Main Flask application file.
   - `static/`: Folder for static files (CSS, images).
   - `templates/`: Folder for HTML templates.
   - `bookstore.db`: SQLite database for storing books.
   - `users.db`: SQLite database for storing user data.

3. **Set Up the Databases:**

   Create and populate the `bookstore.db` and `users.db` databases.

   - You can use SQLite commands to create and insert data into these tables.
   - Example to insert books:

     ```sql
     INSERT INTO Books (title, author, price, stock)
     VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 10.99, 20);
     ```

   - Example to insert a user:

     ```sql
     INSERT INTO Users (username, password)
     VALUES ('user1', 'password123');
     ```

4. **Run the Flask App:**

   After setting up the databases, you can run the Flask app:

   ```bash
   python app.py
   ```

   The app will be hosted locally at `http://127.0.0.1:5000/`.

---

## How to Use the Application

1. **Home Page:**

   - On the homepage, you will see a list of available books.
   - You can search for books by title using the search bar.

2. **Login:**

   - You can log in by clicking the "Login" button in the navbar.
   - Enter a username and password (you can use the predefined users in the database).
   - Once logged in, the navbar will show a personalized greeting and a logout option.

3. **Adding to Cart:**

   - To add a book to your shopping cart, click the "Add to Cart" button next to the book.
   - The cart will track the quantity of books added (if you add the same book multiple times, the count will increase).

4. **Viewing the Cart:**

   - Click on the "Cart" link in the navbar to view the items in your cart.
   - A modal will display the books you added to the cart, along with their quantities and prices.

5. **Logout:**
   - You can log out by clicking the "Logout" button in the navbar. This will end the session and redirect you to the homepage.

---

## Code Explanation

### Main Application Flow

1. **Routing:**

   - The `home()` route handles the home page and loads all books from the database.
   - The `login()` route handles the login process and authenticates the user.
   - The `logout()` route logs out the current user and redirects them to the home page.
   - The `add_to_cart()` route adds a book to the cart and stores the count of books if the same book is added again.
   - The `search()` route searches for books based on the title.

2. **User Authentication:**

   - `Flask-Login` manages user sessions. If the user is logged in, `current_user.is_authenticated` returns `True`, which can be used to display personalized content on the UI.
   - The `login_manager.user_loader` function loads the user based on the user ID.

3. **Database Interaction:**
   - SQLite is used to interact with both the `Books` and `Users` databases.
   - SQL queries are used to fetch data, check for matching usernames and passwords, and retrieve book details.

### Frontend (HTML):

- **Home Page (`index.html`)**:

  - Displays available books in a table format with options to add books to the cart.
  - Displays the user status (whether logged in or not).
  - Displays the shopping cart in a modal.

- **Login Page (`login.html`)**:
  - A simple login form where users can input their credentials.

## Acknowledgments

- **Flask Documentation**: For the great documentation that helped build this project.
- **SQLite Documentation**: For the easy-to-use SQLite database.
- **Bootstrap**: For the responsive design components.

---
