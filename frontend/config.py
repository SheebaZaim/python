# import os

# API_URL = "http://127.0.0.1:8000"
# # Add session state initialization
# import streamlit as st

# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False
# if 'username' not in st.session_state:
#     st.session_state.username = None
import streamlit as st
from pathlib import Path
import os


# API Configuration
API_URL = "http://127.0.0.1:8000"  # FastAPI backend URL

# App Configuration
APP_NAME = "Chemistry Learning Hub"
APP_ICON = "🧪"
APP_DESCRIPTION = "Interactive Chemistry Learning Platform"

# Session State initialization
def init_session_state():
    """Initialize session state variables"""
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'
    if 'quiz_topic' not in st.session_state:
        st.session_state.quiz_topic = None
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0

# Page Configuration
PAGE_CONFIG = {
    "page_title": APP_NAME,
    "page_icon": APP_ICON,
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Available Topics
CHEMISTRY_TOPICS = [
    "Atomic Structure",
    "Chemical Bonds",
    "Periodic Table",
    "Acids and Bases",
    "Chemical Reactions",
    "Thermodynamics",
    "Organic Chemistry",
    "Nuclear Chemistry"
]

# Grade Levels
GRADE_LEVELS = [
    "High School",
    "College",
    "Graduate",
    "Professional"
]

# UI Theme Colors
COLORS = {
    "primary": "#4CAF50",
    "secondary": "#45a049",
    "accent": "#2196F3",
    "error": "#f44336",
    "warning": "#ff9800",
    "success": "#4CAF50"
}

# File Paths
ASSETS_DIR = Path(__file__).parent / "assets"
DATA_DIR = Path(__file__).parent / "data"

# Ensure directories exist
ASSETS_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

# Custom CSS
CUSTOM_CSS = """
    <style>
    .stButton > button {
        background-color: %s;
        color: white;
        border-radius: 20px;
        padding: 10px 24px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: %s;
        transform: translateY(-2px);
    }
    .quiz-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stProgress > div > div > div {
        background-color: %s;
    }
    .success-message {
        color: %s;
    }
    .error-message {
        color: %s;
    }
    </style>
""" % (
    COLORS["primary"],
    COLORS["secondary"],
    COLORS["primary"],
    COLORS["success"],
    COLORS["error"]
)

# API Endpoints
class APIEndpoints:
    BASE = API_URL
    LOGIN = f"{API_URL}/login"
    SIGNUP = f"{API_URL}/signup"
    CONCEPT = f"{API_URL}/concept"
    USER_PROGRESS = f"{API_URL}/progress"
    USER_PROFILE = f"{API_URL}/user"

# Error Messages
ERROR_MESSAGES = {
    "connection": "Cannot connect to server. Please try again later.",
    "login_failed": "Invalid username or password",
    "signup_failed": "Failed to create account",
    "concept_not_found": "Concept not found. Try another topic.",
    "session_expired": "Your session has expired. Please login again."
}

def apply_config():
    """Apply configuration to Streamlit"""
    st.set_page_config(**PAGE_CONFIG)
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    init_session_state()