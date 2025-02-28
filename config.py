import os
from pathlib import Path
import streamlit as st


# Base paths
ROOT_DIR = Path(__file__).parent
FRONTEND_DIR = ROOT_DIR / "frontend"
BACKEND_DIR = ROOT_DIR / "backend"

# API Configuration
API_URL = "http://127.0.0.1:8000"

# App Configuration
APP_NAME = "Chemistry Learning Hub"
APP_ICON = "🧪"

# Available Topics
CHEMISTRY_TOPICS = [
    "Atomic Structure",
    "Chemical Bonds",
    "Periodic Table",
    "Acids and Bases",
    "Thermodynamics"
]

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

