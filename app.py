import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-pro")

st.title("Gemini Career Copilot 🚀")

resume = st.text_area("📄 Paste Your Resume")
job_desc = st.text_area("💼 Paste Job Description")

if st.button("Analyze"):
    prompt = f"""
    Compare the following resume and job description.
    Identify:
    1. Matching skills
    2. Missing skills
    3. Skill gap summary
    4. Generate interview questions

    Resume:
    {resume}

    Job Description:
    {job_desc}
    """

    response = model.generate_content(prompt)
    st.write(response.text)
