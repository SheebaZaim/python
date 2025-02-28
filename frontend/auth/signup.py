# # # import streamlit as st

# # # def signup_page():
# # #     st.title("Signup Page")
# # #     st.write("Welcome to signup page.")

# # # if __name__ == "__main__":
# # #     signup_page()

# # import streamlit as st
# # import requests
# # from frontend.config import API_URL

# # def login_page():
# #     st.title("Login")
    
# #     with st.form("login_form"):
# #         username = st.text_input("Username")
# #         password = st.text_input("Password", type="password")
# #         submit = st.form_submit_button("Login")

# #         if submit:
# #             try:
# #                 response = requests.post(
# #                     f"{API_URL}/login", 
# #                     json={"username": username, "password": password}
# #                 )
                
# #                 if response.status_code == 200:
# #                     st.session_state.logged_in = True
# #                     st.session_state.username = username
# #                     st.success("Successfully logged in!")
# #                     st.experimental_rerun()
# #                 else:
# #                     st.error("Invalid username or password")
# #             except requests.ConnectionError:
# #                 st.error("Cannot connect to server. Please make sure the API is running.")


# import streamlit as st
# import json
# from pathlib import Path

# def signup_page():
#     st.title("Create Your Account")
    
#     with st.form("signup_form"):
#         col1, col2 = st.columns(2)
        
#         with col1:
#             first_name = st.text_input("First Name")
#             email = st.text_input("Email")
#             username = st.text_input("Username")
        
#         with col2:
#             last_name = st.text_input("Last Name")
#             password = st.text_input("Password", type="password")
#             confirm_password = st.text_input("Confirm Password", type="password")
        
#         # Additional fields
#         grade_level = st.selectbox(
#             "Grade Level",
#             ["High School", "College", "Graduate", "Professional"]
#         )
        
#         interests = st.multiselect(
#             "Areas of Interest",
#             ["Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", 
#              "Analytical Chemistry", "Biochemistry"]
#         )
        
#         terms = st.checkbox("I agree to the Terms and Conditions")
#         submit = st.form_submit_button("Sign Up")

#         if submit:
#             if not all([first_name, last_name, email, username, password, confirm_password]):
#                 st.error("Please fill in all required fields")
#             elif password != confirm_password:
#                 st.error("Passwords do not match")
#             elif not terms:
#                 st.error("Please accept the Terms and Conditions")
#             else:
#                 # Save user data (replace with API call when backend is ready)
#                 user_data = {
#                     "username": username,
#                     "email": email,
#                     "first_name": first_name,
#                     "last_name": last_name,
#                     "grade_level": grade_level,
#                     "interests": interests
#                 }
                
#                 # For testing without backend
#                 st.success("Account created successfully! Please login.")
#                 st.balloons()


import streamlit as st
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from config import API_URL

def signup_page():
    st.title("Create Your Account")
    
    with st.form("signup_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name")
            email = st.text_input("Email")
            username = st.text_input("Username")
        
        with col2:
            last_name = st.text_input("Last Name")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
        
        # Additional fields
        grade_level = st.selectbox(
            "Grade Level",
            ["High School", "College", "Graduate", "Professional"]
        )
        
        interests = st.multiselect(
            "Areas of Interest",
            ["Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", 
             "Analytical Chemistry", "Biochemistry"]
        )
        
        terms = st.checkbox("I agree to the Terms and Conditions")
        submit = st.form_submit_button("Sign Up")

        if submit:
            if not all([first_name, last_name, email, username, password, confirm_password]):
                st.error("Please fill in all required fields")
            elif password != confirm_password:
                st.error("Passwords do not match")
            elif not terms:
                st.error("Please accept the Terms and Conditions")
            else:
                try:
                    # For testing without backend
                    st.success("Account created successfully! Please login.")
                    st.balloons()
                except Exception as e:
                    st.error("Cannot connect to server. Please try again later.")

