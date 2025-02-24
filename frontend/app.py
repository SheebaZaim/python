# # import streamlit as st
# # import requests

# # API_URL = "http://127.0.0.1:8000/concept/"

# # st.title("Your Chemistry Tutor")

# # topic = st.text_input("Enter a Chemistry Topic:", "Periodic Table")

# # if st.button("Fetch Explanation"):
# #     response = requests.get(API_URL + topic.replace(" ", "_"))
    
# #     if response.status_code == 200:
# #         data = response.json()
# #         if "error" in data:
# #             st.error(data["error"])
# #         else:
# #             st.write(f"**{data['topic']}**")
# #             st.write(data["summary"])
# #     else:
# #         st.error("Error fetching data. Please try again.")
# # import streamlit as st
# # import requests

# # API_URL = "http://127.0.0.1:8000/auth/"

# # st.title("Your Chemistry Tutor")

# # # Session state for authentication
# # if "token" not in st.session_state:
# #     st.session_state.token = None

# # # Authentication Tabs
# # tab1, tab2 = st.tabs(["Login", "Signup"])

# # with tab1:
# #     st.subheader("Login")
# #     username = st.text_input("Username")
# #     password = st.text_input("Password", type="password")

# #     if st.button("Login"):
# #         response = requests.post(API_URL + "login", params={"username": username, "password": password})

# #         if response.status_code == 200:
# #             st.session_state.token = response.json()["token"]
# #             st.success("Login successful!")
# #             st.experimental_rerun()
# #         else:
# #             st.error("Invalid credentials!")

# # with tab2:
# #     st.subheader("Signup")
# #     new_username = st.text_input("New Username")
# #     new_password = st.text_input("New Password", type="password")

# #     if st.button("Signup"):
# #         response = requests.post(API_URL + "signup", params={"username": new_username, "password": new_password})

# #         if response.status_code == 200:
# #             st.success("Signup successful! You can now login.")
# #         else:
# #             st.error(response.json()["detail"])

# import streamlit as st
# import requests
# from pages.welcome import welcome_page

# from auth.signup import signup_page
# from auth.login import login_page
# from pages.concept import concept_page  # Check if this is the correct pat



# API_URL = "http://127.0.0.1:8000"  # FastAPI server URL

# st.title("Welcome to Your Chemistry Tutor")

# page = st.sidebar.selectbox("Choose a page", ["Welcome", "Concept Search", "Login", "Signup"])

# if page == "Welcome":
#     st.subheader("Welcome Page")
#     st.write("Use the sidebar to navigate.")

# elif page == "Concept Search":
#     st.subheader("Search for Chemistry Concepts")
#     topic = st.text_input("Enter a chemistry topic:")
    
#     if st.button("Search"):
#         response = requests.get(f"{API_URL}/concept/{topic}")
        
#         if response.status_code == 200:
#             st.write(response.json()["summary"])
#         else:
#             st.error("Concept not found. Try another topic.")

# elif page == "Login":
#     import auth.login

# elif page == "Signup":
#     import auth.signup


import streamlit as st
from auth.login import login_page
from auth.signup import signup_page
from pages.concept import concept_page
from pages.quiz import generate_quiz
from style.custom import apply_custom_style

# Apply custom styling
apply_custom_style()

# Page config
st.set_page_config(
    page_title="Interactive Chemistry Learning",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'

    # Sidebar navigation
    with st.sidebar:
        st.title("Chemistry Learning Hub 🧪")
        
        if st.session_state.logged_in:
            st.success(f"Welcome back, {st.session_state.username}!")
            
            # Navigation menu
            selected = st.radio(
                "Navigation",
                ["Home", "Learn Concepts", "Take Quiz", "Progress", "Settings"]
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
    else:
        if selected == "Learn Concepts":
            concept_page()
        elif selected == "Take Quiz":
            st.title("Chemistry Quiz")
            topic = st.selectbox("Select Topic", ["Atomic Structure", "Chemical Bonds"])
            if topic:
                generate_quiz(topic)
        elif selected == "Progress":
            st.title("Your Learning Progress")
            # Add progress tracking features here
        elif selected == "Settings":
            st.title("Settings")
            # Add settings options here
        else:
            st.title("Welcome to Your Dashboard")
            
            # Quick stats
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Topics Completed", "5")
            with col2:
                st.metric("Quiz Score", "85%")
            with col3:
                st.metric("Study Streak", "3 days")

if __name__ == "__main__":
    main()

