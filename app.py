import streamlit as st

st.title("🚀 Nova Career Agent")

st.write("AI-powered Resume Analyzer & Interview Coach")

resume = st.text_area("Paste Your Resume")
job = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume and job:
        st.subheader("Match Score: 75%")
        st.write("Skill Gaps: Stakeholder Management, KPI Tracking")
        st.write("Suggested Improvements: Add measurable achievements.")
        st.write("Interview Question: How would you define KPIs for this role?")
    else:
        st.warning("Please enter both resume and job description.")
