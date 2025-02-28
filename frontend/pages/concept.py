import streamlit as st
import requests
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from config import API_URL
CHEMISTRY_TOPICS = ["Atomic Structure", "Chemical Bonds", "Periodic Table", "Acids and Bases", "Thermodynamics"]

def concept_page():
    st.title("Interactive Chemistry Learning 🧪")
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Learn", "Quiz", "Practice"])
    
    with tab1:
        st.subheader("Search Chemistry Concepts")
        
        topic = st.selectbox(
            "What would you like to learn about?",
            CHEMISTRY_TOPICS,
            index=None,
            placeholder="Select a topic..."
        )
        
        if topic:
            try:
                with st.spinner("Loading concept..."):
                    response = requests.get(f"{API_URL}/concept/{topic.replace(' ', '_')}")
                    st.write(f"API URL: {API_URL}/concept/{topic.replace(' ', '_')}")
                    st.write(f"Response Status Code: {response.status_code}")
                    st.write(f"Response Text: {response.text}")
                
                if response.status_code == 200:
                    data = response.json()
                    
                    with st.expander("📚 Concept Overview", expanded=True):
                        st.markdown(data["summary"])
                    
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
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            
            except requests.ConnectionError:
                st.error("Cannot connect to server. Please try again later.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

