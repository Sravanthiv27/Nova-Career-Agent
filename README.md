# 🚀 Nova Career Agent
**AI-powered Career Copilot built using Amazon Nova via AWS Bedrock**

Nova Career Agent is an intelligent AI assistant that analyzes resumes, compares them with job descriptions, calculates match scores using semantic similarity, identifies skill gaps, and generates personalized interview questions.

---

## 💡 Problem Statement

Job seekers struggle with:
- Understanding how well their resume matches a job
- Identifying missing skills
- Preparing for interviews effectively

Nova Career Agent solves this using Amazon Nova's reasoning capabilities and ML-based similarity scoring.

---

## 🧠 How It Works

1. User pastes Resume
2. User pastes Job Description
3. System calculates semantic similarity score
4. Amazon Nova generates:
   - Match Analysis
   - Missing Skills
   - Resume Improvement Suggestions
   - Personalized Interview Questions

Similarity is calculated using cosine similarity:

\[
Similarity = \frac{A \cdot B}{||A|| \, ||B||}
\]

---

## 🛠 Tech Stack

### AI & Cloud
- Amazon Nova (via AWS Bedrock)
- AWS

### Backend
- Python
- Boto3

### Machine Learning
- Sentence Transformers
- FAISS
- Cosine Similarity

### Frontend
- Streamlit

---

## 📦 Installation & Setup

```bash
git clone https://github.com/Sravanthiv27/Nova-Career-Agent.git
cd Nova-Career-Agent
pip install -r requirements.txt
streamlit run app.py
