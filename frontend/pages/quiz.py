import streamlit as st
import random
import json
from pathlib import Path

def load_questions(topic):
    # In production, this would come from a database
    questions = {
        "Atomic Structure": [
            {
                "question": "What is the charge of an electron?",
                "options": ["-1", "+1", "0", "+2"],
                "correct": "-1"
            },
            {
                "question": "What particle has no charge?",
                "options": ["Proton", "Electron", "Neutron", "Ion"],
                "correct": "Neutron"
            }
        ],
        "Chemical Bonds": [
            {
                "question": "What type of bond involves sharing electrons?",
                "options": ["Ionic", "Covalent", "Metallic", "Hydrogen"],
                "correct": "Covalent"
            }
        ]
    }
    return questions.get(topic, [])

def generate_quiz(topic):
    st.subheader(f"Quiz: {topic}")
    
    questions = load_questions(topic)
    if not questions:
        st.warning("No questions available for this topic yet.")
        return
    
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    
    # Progress bar
    progress = st.progress(st.session_state.current_question / len(questions))
    
    if st.session_state.current_question < len(questions):
        question = questions[st.session_state.current_question]
        
        # Display question with nice formatting
        with st.container():
            st.write(f"**Question {st.session_state.current_question + 1}:**")
            st.write(question["question"])
            
            # Create radio buttons for options
            answer = st.radio(
                "Choose your answer:",
                question["options"],
                key=f"q_{st.session_state.current_question}"
            )
            
            col1, col2 = st.columns([1, 5])
            with col1:
                if st.button("Submit Answer"):
                    st.session_state.answers[st.session_state.current_question] = answer
                    
                    if answer == question["correct"]:
                        st.success("Correct! 🎉")
                        st.session_state.quiz_score += 1
                    else:
                        st.error(f"Wrong! The correct answer is {question['correct']}")
                    
                    st.session_state.current_question += 1
                    st.experimental_rerun()
    else:
        # Quiz completed
        final_score = (st.session_state.quiz_score / len(questions)) * 100
        st.success(f"Quiz completed! Your score: {final_score:.1f}%")
        
        # Display results breakdown
        st.subheader("Results Breakdown")
        for i, question in enumerate(questions):
            with st.expander(f"Question {i + 1}"):
                st.write(f"**Q:** {question['question']}")
                st.write(f"**Your answer:** {st.session_state.answers.get(i, 'Not answered')}")
                st.write(f"**Correct answer:** {question['correct']}")
                
                if st.session_state.answers.get(i) == question['correct']:
                    st.success("Correct ✅")
                else:
                    st.error("Incorrect ❌")
        
        if st.button("Try Again"):
            st.session_state.quiz_score = 0
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.experimental_rerun()

