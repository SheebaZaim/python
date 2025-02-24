# import sqlite3

# def create_users_table():
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT UNIQUE,
#         password TEXT
#     )''')
#     conn.commit()
#     conn.close()

# def add_user(username, password):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#     conn.commit()
#     conn.close()

# def get_user(username):
#     conn = sqlite3.connect("users.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE username=?", (username,))
#     user = cursor.fetchone()
#     conn.close()
#     return user
import sqlite3

def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn
