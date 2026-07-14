import streamlit as st
from backend.resume_parser import extract_resume_text
from backend.granite_api import generate_interview
from backend.evaluation_agent import evaluate_answer
from backend.recommendation_agent import recommend

st.set_page_config(
    page_title="AI Interview Trainer Agent",
    page_icon="🎤",
    layout="wide"
)

st.sidebar.title("AI Interview Trainer")

page = st.sidebar.selectbox(
    "Select Page",
    [
        "🏠 Home",
        "📄 Upload Resume",
        "🎤 Mock Interview",
        "📝 Answer Evaluation",
        "💡 Recommendations"
    ]
)

# -------------------- HOME --------------------

if page == "🏠 Home":

    st.title("🎤 AI Interview Trainer Agent")

    st.markdown("""
### Welcome!

This AI-powered application helps job seekers prepare for technical interviews.

### Features
- 📄 Upload Resume
- 🤖 AI Resume Analysis
- 🎤 AI Mock Interview
- 📝 AI Answer Evaluation
- 💡 Personalized Recommendations

### Technologies Used
- Python
- Streamlit
- IBM watsonx.ai
- IBM Granite Foundation Model

""")

# -------------------- RESUME UPLOAD --------------------

elif page == "📄 Upload Resume":

    st.title("📄 Resume Upload")

    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        with open("resume.pdf", "wb") as f:
            f.write(uploaded_file.read())

        resume_text = extract_resume_text("resume.pdf")

        st.success("Resume uploaded successfully!")

        st.subheader("Extracted Resume Text")

        st.text_area(
            "Resume",
            resume_text,
            height=300
        )

# -------------------- MOCK INTERVIEW --------------------

elif page == "🎤 Mock Interview":

    st.title("🎤 AI Mock Interview")

    job_role = st.text_input(
        "Enter Job Role",
        placeholder="Example: Python Developer"
    )
    experience = st.selectbox(
    "Experience Level",
    ["Fresher", "1-3 Years", "3-5 Years", "5+ Years"]
    )

    if st.button("Generate Interview Questions"):

        if job_role.strip() == "":
            st.warning("Please enter a job role.")
        else:

            with st.spinner("Generating interview questions..."):

                questions = generate_interview(job_role, experience)

            st.success("Interview Questions Generated!")

            st.write(questions)

# -------------------- ANSWER EVALUATION --------------------

elif page == "📝 Answer Evaluation":

    st.title("📝 AI Answer Evaluation")

    question = st.text_area("Interview Question")

    answer = st.text_area("Your Answer")

    if st.button("Evaluate Answer"):

        if question.strip() == "" or answer.strip() == "":
            st.warning("Please enter both the question and your answer.")
        else:
            with st.spinner("Evaluating your answer..."):
                result = evaluate_answer(question, answer)

            st.success("Evaluation Completed!")
            st.write(result)


# -------------------- RECOMMENDATIONS --------------------

elif page == "💡 Recommendations":

    st.title("💡 AI Career Recommendations")

    answer = st.text_area("Paste your Answer")

    if st.button("Get Recommendations"):

        if answer.strip() == "":
            st.warning("Please enter your answer.")
        else:
            with st.spinner("Generating recommendations..."):
                tips = recommend(answer)

            st.success("Recommendations Generated!")
            st.write(tips)


# -------------------- FOOTER --------------------

st.sidebar.markdown("---")
st.sidebar.info(
    "AI Interview Trainer Agent\n\n"
    "Powered by IBM watsonx.ai Granite"
)