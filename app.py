from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


def get_books():
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Books')
    books = cursor.fetchall()
    conn.close()
    return books


def get_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    conn.close()
    return users


cart = []


@app.route('/')
def home():
    books = get_books()
    return render_template('index.html', books=books, cart=cart, user=current_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = get_users()
        for user in users:
            if user[1] == username and user[2] == password:
                login_user(User(user[1]))
                current_user.id = user[0]
                current_user.username = user[1]
                return redirect(url_for('home'))
        return 'Login failed', 401
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search_term')
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books WHERE title LIKE ?",
                   ('%' + search_term + '%',))
    books = cursor.fetchall()
    conn.close()
    return render_template('index.html', books=books, cart=cart, user=current_user)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    book_id = request.form.get('book_id')
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()

    cursor.execute("SELECT title, price FROM Books WHERE id = ?", (book_id,))
    book_details = cursor.fetchone()
    conn.close()

    if book_details:
        title, price = book_details
        found = False
        for item in cart:
            if item['id'] == book_id:
                item['count'] += 1
                found = True
                break

        if not found:
            cart.append({'id': book_id, 'title': title,
                        'price': price, 'count': 1})

    books = get_books()
    return render_template('index.html', books=books, cart=cart, user=current_user)


if __name__ == '__main__':
    app.run(debug=True)
