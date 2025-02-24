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

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Sample User Database
fake_users_db = {
    "admin": {"username": "admin", "password": pwd_context.hash("admin123")}
}

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or not pwd_context.verify(password, user["password"]):
        return {"error": "Invalid username or password"}
    return {"message": "Login successful"}
