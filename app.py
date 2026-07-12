from backend.granite_api import generate_interview
from backend.resume_parser import extract_skills
from backend.evaluation_agent import evaluate_answer
from backend.recommendation_agent import recommend
from backend.granite_api import generate_interview
import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="InterviewGenius AI",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🤖 InterviewGenius AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📄 Upload Resume",
        "💼 Select Job Role",
        "🎤 Mock Interview",
        "📊 Evaluation",
        "📚 Learning Resources",
        "ℹ About"
    ]
)

# -----------------------------
# Dashboard
# -----------------------------

if page == "🏠 Dashboard":

    st.title("🤖 InterviewGenius AI")

    st.subheader(
        "Agentic AI Interview Coach using IBM Granite"
    )

    st.markdown("---")

    c1,c2,c3,c4=st.columns(4)
    c1.metric("AI Agents","5")
    
    c2.metric("IBM Granite","Connected")
    
    c3.metric("Interview Score","--")
    
    c4.metric("RAG","Enabled")

    st.markdown("---")

    st.header("Project Overview")

    st.write("""
InterviewGenius AI is an Agentic AI application developed using
IBM Granite Foundation Models.

The system consists of multiple AI agents that work together.

### AI Agents

• Resume Analysis Agent

• Skill Extraction Agent

• Interview Generation Agent

• Evaluation Agent

• Learning Recommendation Agent
""")

    st.success("Select any module from the sidebar.")

# -----------------------------
# Resume Upload
# -----------------------------

elif page=="📄 Upload Resume":

    st.header("📄 Resume Upload")

    uploaded=st.file_uploader(
        "Upload Resume",
        type=["pdf","docx"]
    )

    if uploaded:

        if not os.path.exists("uploads"):
            os.mkdir("uploads")

        with open(
            os.path.join("uploads",uploaded.name),
            "wb"
        ) as f:

            f.write(uploaded.getbuffer())

        st.success("Resume Uploaded Successfully!")
        resume_text = uploaded.getvalue().decode("latin-1", errors="ignore")
        
        skills = extract_skills(resume_text)

        st.subheader("Detected Skills")

        st.write(skills)

        st.write("Filename :",uploaded.name)

        st.info(
            "Resume parsing will be performed by Resume Agent."
        )

# -----------------------------
# Job Role
# -----------------------------

elif page=="💼 Select Job Role":

    st.header("Select Job Role")

    role=st.selectbox(

        "Choose Role",

        [

            "Data Scientist",

            "Machine Learning Engineer",

            "Data Analyst",

            "AI Engineer",

            "Python Developer",

            "Software Engineer"

        ]

    )

    st.success(f"Selected Role : {role}")

    if st.button("Generate Questions"):
        with st.spinner("IBM Granite is generating interview questions..."):
            questions = generate_interview(role)
        
        st.success("Questions Generated Successfully!")
        
        st.write(questions)
    # -----------------------------
# Mock Interview
# -----------------------------

elif page == "🎤 Mock Interview":

    st.header("🎤 AI Mock Interview")

    role = st.selectbox(
        "Select Interview Role",
        [
            "Data Scientist",
            "Machine Learning Engineer",
            "Data Analyst",
            "Python Developer"
        ]
    )

    if st.button("Generate Questions"):
        questions = generate_interview(role)
        
        st.success("IBM Granite Generated Questions")
        
        st.markdown(questions)
         
# -----------------------------
# Evaluation
# -----------------------------

if st.button("Evaluate"):

    score,feedback = evaluate_answer(answer)

    st.metric("Interview Score",f"{score}/10")

    st.subheader("Feedback")

    for i in feedback:

        st.success(i)

    st.subheader("Recommended Learning")

    rec = recommend(score)

    for r in rec:

        st.write("•",r)

# -----------------------------
# Learning Resources
# -----------------------------

elif page == "📚 Learning Resources":

    st.header("📚 Personalized Learning")

    skill = st.selectbox(
        "Select Skill",
        [
            "Python",
            "Machine Learning",
            "SQL",
            "Deep Learning",
            "Data Science"
        ]
    )

    if st.button("Show Resources"):

        st.write("### Recommended Resources")

        st.write("• IBM SkillsBuild")

        st.write("• Coursera")

        st.write("• Kaggle Learn")

        st.write("• freeCodeCamp")

        st.write("• GeeksforGeeks")

# -----------------------------
# About
# -----------------------------

elif page == "ℹ About":

    st.header("About Project")

    st.write("""
InterviewGenius AI is an Agentic AI Interview Coach.

Developed using:

• IBM Granite

• IBM watsonx.ai

• IBM Cloud Lite

• Streamlit

• Python

This project demonstrates Agentic AI using
multiple intelligent agents.
""")