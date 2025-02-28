# # # # import streamlit as st
# # # # import requests

# # # # API_URL = "http://127.0.0.1:8000"

# # # # def login_page():
# # # #     st.title("Login Page")
    
# # # #     username = st.text_input("Username")
# # # #     password = st.text_input("Password", type="password")

# # # #     if st.button("Login"):
# # # #         response = requests.post(f"{API_URL}/login", params={"username": username, "password": password})
        
# # # #         if "error" in response.json():
# # # #             st.error(response.json()["error"])
# # # #         else:
# # # #             st.success(response.json()["message"])

# # # # if __name__ == "__main__":
# # # #     login_page()

# # # import streamlit as st
# # # import requests
# # # from ..config import API_URL

# # # from config import APIEndpoints, ERROR_MESSAGES

# # # def login_page():
# # #     # ...
# # #     response = requests.post(APIEndpoints.LOGIN, json={"username": username, "password": password})

# # #     st.title("Login")
    
# # #     with st.form("login_form"):
# # #         username = st.text_input("Username")
# # #         password = st.text_input("Password", type="password")
# # #         submit = st.form_submit_button("Login")

# # #         if submit:
# # #             try:
# # #                 response = requests.post(
# # #                     f"{API_URL}/login", 
# # #                     json={"username": username, "password": password}
# # #                 )
                
# # #                 if response.status_code == 200:
# # #                     st.session_state.logged_in = True
# # #                     st.session_state.username = username
# # #                     st.success("Successfully logged in!")
# # #                     st.experimental_rerun()
# # #                 else:
# # #                     st.error("Invalid username or password")
# # #             except requests.ConnectionError:
# # #                 st.error("Cannot connect to server. Please make sure the API is running.")


# # import streamlit as st
# # import requests
# # import sys
# # from pathlib import Path

# # # Get the current directory
# # current_dir = Path(__file__).parent
# # # Add the project root to the Python path
# # project_root = current_dir.parent.parent
# # sys.path.append(str(project_root))

# # from config import API_URL

# # def login_page():
# #     st.title("Login")
    
# #     with st.form("login_form"):
# #         username = st.text_input("Username")
# #         password = st.text_input("Password", type="password")
# #         submit = st.form_submit_button("Login")

# #         if submit:
# #             try:
# #                 # For testing without backend
# #                 if username == "test" and password == "test":
# #                     st.session_state.logged_in = True
# #                     st.session_state.username = username
# #                     st.success("Login successful!")
# #                     st.experimental_rerun()
# #                 else:
# #                     response = requests.post(
# #                         f"{API_URL}/login",
# #                         json={"username": username, "password": password}
# #                     )
# #                     if response.status_code == 200:
# #                         st.session_state.logged_in = True
# #                         st.session_state.username = username
# #                         st.success("Login successful!")
# #                         st.experimental_rerun()
# #                     else:
# #                         st.error("Invalid username or password")
# #             except Exception as e:
# #                 st.error(f"An error occurred: {str(e)}")

# # #
# import streamlit as st
# import requests
# import sys
# from pathlib import Path

# # Get the current directory
# current_dir = Path(__file__).parent
# # Add the frontend directory to the Python path
# frontend_dir = current_dir.parent
# sys.path.append(str(frontend_dir))

# from config import API_URL

# def login_page():
#     st.title("Login")
    
#     with st.form("login_form"):
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         submit = st.form_submit_button("Login")

#         if submit:
#             try:
#                 # For testing without backend
#                 if username == "test" and password == "test":
#                     st.session_state.logged_in = True
#                     st.session_state.username = username
#                     st.success("Login successful!")
#                     st.experimental_rerun()
#                 else:
#                     response = requests.post(
#                         f"{API_URL}/login",
#                         json={"username": username, "password": password}
#                     )
#                     if response.status_code == 200:
#                         st.session_state.logged_in = True
#                         st.session_state.username = username
#                         st.success("Login successful!")
#                         st.experimental_rerun()
#                     else:
#                         st.error("Invalid username or password")
#             except Exception as e:
#                 st.error(f"An error occurred: {str(e)}")


import streamlit as st
import requests
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from config import API_URL

def login_page():
    st.title("Login to Your Account")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            try:
                # For testing without backend
                if username == "test" and password == "test":
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Login successful!")
                    st.experimental_rerun()
                else:
                    response = requests.post(
                        f"{API_URL}/login",
                        json={"username": username, "password": password}
                    )
                    if response.status_code == 200:
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.success("Login successful!")
                        st.experimental_rerun()
                    else:
                        st.error("Invalid username or password")
            except Exception as e:
                st.error("Cannot connect to server. Please try again later.")

