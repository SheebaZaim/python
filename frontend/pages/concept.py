# import streamlit as st
# import requests

# API_URL = "http://127.0.0.1:8000"

# def concept_page():
#     st.title("Search for Chemistry Concepts")
    
#     topic = st.text_input("Enter a chemistry topic:")
#     if st.button("Search"):
#         response = requests.get(f"{API_URL}/concept/{topic}")
        
#         if response.status_code == 200:
#             st.write(response.json()["summary"])
#         else:
#             st.error("Concept not found. Try another topic.")

# if __name__ == "__main__":
#     concept_page()
import sys
from pathlib import Path

# Ensure the frontend config.py is correctly imported
from ..config import config

API_URL = config.API_URL  # ✅ Access API_URL properly

import streamlit as st
import requests


def concept_page():
    st.title("Interactive Chemistry Learning 🧪")
    
    # Create tabs for different learning modes
    tab1, tab2, tab3 = st.tabs(["Learn", "Quiz", "Practice"])
    
    with tab1:
        st.subheader("Search Chemistry Concepts")
        
        # Add a search bar with autocomplete
        topics = ["Atomic Structure", "Chemical Bonds", "Periodic Table", 
                 "Acids and Bases", "Thermodynamics"]
        
        topic = st.selectbox(
            "What would you like to learn about?",
            topics,
            index=None,
            placeholder="Select a topic..."
        )
        
        if topic:
            try:
                with st.spinner("Loading concept..."):
                    response = requests.get(f"{API_URL}/concept/{topic}")
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Create an expandable section for the concept
                    with st.expander("📚 Concept Overview", expanded=True):
                        st.markdown(data["summary"])
                    
                    # Add interactive elements
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if st.button("📝 Take a Quiz"):
                            st.session_state.current_page = "quiz"
                            st.session_state.quiz_topic = topic
                            st.experimental_rerun()
                    
                    with col2:
                        if st.button("🎯 Practice Problems"):
                            st.session_state.current_page = "practice"
                            st.experimental_rerun()
                    
                    # Add a visual representation
                    st.subheader("Visual Learning")
                    if "image_url" in data:
                        st.image(data["image_url"], caption=f"{topic} Visualization")
                    
                    # Add interactive examples
                    if "examples" in data:
                        st.subheader("Interactive Examples")
                        for i, example in enumerate(data["examples"], 1):
                            with st.expander(f"Example {i}"):
                                st.write(example)
                                st.button(
                                    "Show Solution", 
                                    key=f"sol_{i}",
                                    on_click=lambda: st.info("Solution explanation here")
                                )
            
            except requests.ConnectionError:
                st.error("Cannot connect to server. Please try again later.")
    
    with tab2:
        if st.session_state.get("quiz_topic"):
            generate_quiz(st.session_state.quiz_topic)
        else:
            st.info("Select a topic in the Learn tab to take a quiz!")
    
    with tab3:
        st.subheader("Practice Problems")
        st.info("Coming soon! Practice problems will be available here.")

