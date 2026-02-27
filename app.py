import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Nova Career Agent", layout="wide")

st.title("🚀 Nova Career Agent")
st.subheader("AI-powered Resume Analyzer & Interview Coach")

resume = st.text_area("📄 Paste Your Resume")
job = st.text_area("💼 Paste Job Description")

if st.button("Analyze"):

    if resume and job:

        text = [resume, job]
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(text)

        match_percentage = cosine_similarity(count_matrix)[0][1] * 100
        match_percentage = round(match_percentage, 2)

        st.success(f"✅ Match Score: {match_percentage}%")

        st.subheader("🔍 Skill Gap Insights")

        if match_percentage < 50:
            st.write("Your resume needs major improvement for this role.")
        elif match_percentage < 75:
            st.write("Your resume partially matches the job. Add missing keywords.")
        else:
            st.write("Strong match! Minor improvements needed.")

        st.subheader("🎯 Suggested Improvements")
        st.write("- Add measurable achievements")
        st.write("- Highlight stakeholder collaboration")
        st.write("- Include KPIs and business impact")

        st.subheader("🎤 Sample Interview Question")
        st.write("How would you prioritize features in a roadmap?")

    else:
        st.warning("Please enter both resume and job description.")
