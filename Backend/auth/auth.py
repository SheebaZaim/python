# # # import sqlite3

# # # def create_users_table():
# # #     conn = sqlite3.connect("users.db")
# # #     cursor = conn.cursor()
# # #     cursor.execute('''CREATE TABLE IF NOT EXISTS users (
# # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #         username TEXT UNIQUE,
# # #         password TEXT
# # #     )''')
# # #     conn.commit()
# # #     conn.close()

# # # def add_user(username, password):
# # #     conn = sqlite3.connect("users.db")
# # #     cursor = conn.cursor()
# # #     cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
# # #     conn.commit()
# # #     conn.close()

# # # def get_user(username):
# # #     conn = sqlite3.connect("users.db")
# # #     cursor = conn.cursor()
# # #     cursor.execute("SELECT * FROM users WHERE username=?", (username,))
# # #     user = cursor.fetchone()
# # #     conn.close()
# # #     return user

# # from passlib.context import CryptContext

# # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # # Sample User Database
# # fake_users_db = {
# #     "admin": {"username": "admin", "password": pwd_context.hash("admin123")}
# # }

# # def authenticate_user(username: str, password: str):
# #     user = fake_users_db.get(username)
# #     if not user or not pwd_context.verify(password, user["password"]):
# #         return {"error": "Invalid username or password"}
# #     return {"message": "Login successful"}
# from passlib.context import CryptContext
# import json
# from pathlib import Path

# # Password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # User database file
# USERS_FILE = Path(__file__).parent.parent / "data" / "users.json"
# USERS_FILE.parent.mkdir(exist_ok=True)

# def load_users():
#     """Load users from JSON file"""
#     if USERS_FILE.exists():
#         return json.loads(USERS_FILE.read_text())
#     return {}

# def save_users(users):
#     """Save users to JSON file"""
#     USERS_FILE.write_text(json.dumps(users, indent=2))

# def create_user(username: str, password: str, email: str = None):
#     """Create a new user"""
#     users = load_users()
    
#     if username in users:
#         return {"error": "Username already exists"}
    
#     hashed_password = pwd_context.hash(password)
#     users[username] = {
#         "username": username,
#         "password": hashed_password,
#         "email": email
#     }
    
#     save_users(users)
#     return {"message": "User created successfully"}

# def authenticate_user(username: str, password: str):
#     """Authenticate a user"""
#     users = load_users()
#     user = users.get(username)
    
#     if not user:
#         return {"error": "User not found"}
    
#     if not pwd_context.verify(password, user["password"]):
#         return {"error": "Invalid password"}
    
#     return {"message": "Login successful"}

# # Initialize with a test user
# if not USERS_FILE.exists():
#     create_user("test", "test")

from passlib.context import CryptContext
import json
from pathlib import Path
from typing import Dict, Optional

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User database file
USERS_FILE = Path(__file__).parent.parent / "data" / "users.json"
USERS_FILE.parent.mkdir(exist_ok=True)

def load_users() -> Dict:
    """Load users from JSON file"""
    if USERS_FILE.exists():
        return json.loads(USERS_FILE.read_text())
    return {}

def save_users(users: Dict) -> None:
    """Save users to JSON file"""
    USERS_FILE.write_text(json.dumps(users, indent=2))

def create_user(username: str, password: str, email: Optional[str] = None) -> Dict:
    """Create a new user"""
    users = load_users()
    
    if username in users:
        return {"error": "Username already exists"}
    
    hashed_password = pwd_context.hash(password)
    users[username] = {
        "username": username,
        "password": hashed_password,
        "email": email
    }
    
    save_users(users)
    return {"message": "User created successfully"}

def authenticate_user(username: str, password: str) -> Dict:
    """Authenticate a user"""
    users = load_users()
    user = users.get(username)
    
    if not user:
        return {"error": "User not found"}
    
    if not pwd_context.verify(password, user["password"]):
        return {"error": "Invalid password"}
    
    return {"message": "Login successful"}

# Initialize with a test user if no users exist
if not USERS_FILE.exists():
    create_user("test", "test")

