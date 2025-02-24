# import streamlit as st

# def signup_page():
#     st.title("Signup Page")
#     st.write("Welcome to signup page.")

# if __name__ == "__main__":
#     signup_page()

import streamlit as st
import requests
from frontend.config import API_URL

def login_page():
    st.title("Login")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            try:
                response = requests.post(
                    f"{API_URL}/login", 
                    json={"username": username, "password": password}
                )
                
                if response.status_code == 200:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Successfully logged in!")
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password")
            except requests.ConnectionError:
                st.error("Cannot connect to server. Please make sure the API is running.")

