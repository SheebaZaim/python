import streamlit as st
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from config import APP_NAME, APP_ICON
from frontend.auth.login import login_page
from frontend.auth.signup import signup_page
from frontend.pages.concept import concept_page
from frontend.pages.quiz import generate_quiz

# Page config
st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'

    # Sidebar navigation
    with st.sidebar:
        st.title(f"{APP_NAME} 🧪")
        
        if st.session_state.logged_in:
            st.success(f"Welcome back, {st.session_state.username}!")
            selected = st.radio(
                "Navigation",
                ["Home", "Learn Concepts", "Take Quiz", "Progress"]
            )
            
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.experimental_rerun()
        else:
            selected = st.radio("Navigation", ["Home", "Login", "Sign Up"])

    # Main content
    if not st.session_state.logged_in:
        if selected == "Login":
            login_page()
        elif selected == "Sign Up":
            signup_page()
        else:
            st.title("Welcome to Chemistry Learning Hub! 🧪")
            st.write("Please login or sign up to start learning.")
            
            # Welcome content
            col1, col2 = st.columns(2)
            with col1:
                st.info("👋 New to Chemistry Learning Hub?")
                st.write("Sign up to access:")
                st.write("- Interactive Chemistry Lessons")
                st.write("- Practice Quizzes")
                st.write("- Progress Tracking")
            with col2:
                st.warning("Already have an account?")
                st.write("Login to continue your learning journey!")
    else:
        if selected == "Learn Concepts":
            concept_page()
        elif selected == "Take Quiz":
            st.title("Chemistry Quiz")
            topic = st.selectbox(
                "Select Topic",
                ["Atomic Structure", "Chemical Bonds", "Periodic Table"]
            )
            if topic:
                generate_quiz(topic)
        elif selected == "Progress":
            st.title("Your Progress")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Topics Completed", "5")
            with col2:
                st.metric("Average Score", "85%")
            with col3:
                st.metric("Study Streak", "3 days")
        else:
            st.title(f"Welcome {st.session_state.username}!")
            st.write("Choose an option from the sidebar to get started.")

if __name__ == "__main__":
    main()

