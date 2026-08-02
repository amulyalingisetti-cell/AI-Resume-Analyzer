# 📄 AI Resume Analyzer and Job Recommendation System

An AI-powered Resume Analyzer built using **Python**, **Streamlit**, and **Natural Language Processing (NLP)** that analyzes resumes, matches them with predefined job roles, identifies missing skills, and generates a personalized learning roadmap.

---

# 🚀 Project Overview

The AI Resume Analyzer helps students and job seekers evaluate how well their resumes match different technical job roles. The application extracts resume content from PDF and DOCX files, detects technical skills, compares them with job requirements, and recommends suitable career paths.

This project aims to assist users in improving their resumes and learning the skills required for their desired job roles.

---

# ✨ Features

- Upload Resume (PDF & DOCX)
- Automatic Resume Text Extraction
- Resume Text Cleaning
- Technical Skill Extraction
- Resume-to-Job Matching
- Match Score Calculation
- Top 3 Job Recommendations
- Skill Gap Analysis
- Personalized Learning Roadmap
- Interactive Charts
- Downloadable PDF Report
- Simple and User-Friendly Streamlit Interface

---

# 🛠️ Technologies Used

### Programming Language
- Python

### Frontend
- Streamlit

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Plotly
- PyPDF
- python-docx
- ReportLab
- Regular Expressions (re)

### Machine Learning & NLP
- TF-IDF Vectorizer
- Cosine Similarity
- Keyword-Based Skill Extraction

---

# 📁 Project Structure

```
AI_Resume_Analyzer/
│
├── app.py
├── resume_parser.py
├── text_cleaner.py
├── skill_extractor.py
├── matcher.py
├── roadmap.py
├── report_generator.py
├── utils.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── job_roles.csv
│   ├── skills.csv
│
├── sample_resumes/
│
├── reports/
│
└── tests/
```

---

# ⚙️ How It Works

### Step 1
Upload a resume in PDF or DOCX format.

↓

### Step 2
Extract resume text.

↓

### Step 3
Clean and preprocess the extracted text.

↓

### Step 4
Identify technical skills from the resume.

↓

### Step 5
Compare the resume with predefined job roles.

↓

### Step 6
Calculate the Resume Match Score using TF-IDF and Cosine Similarity.

↓

### Step 7
Recommend the Top 3 matching job roles.

↓

### Step 8
Identify missing skills.

↓

### Step 9
Generate a personalized learning roadmap.

↓

### Step 10
Download the Resume Analysis Report.

---

# 📊 Supported Job Roles

- AI Engineer
- Machine Learning Engineer
- Data Analyst
- Data Scientist
- Python Developer
- NLP Engineer
- Computer Vision Engineer
- Java Backend Developer
- Full Stack Developer
- Cloud Engineer

---

# 📌 Match Score Calculation

The application converts resumes and job descriptions into TF-IDF vectors.

Cosine Similarity is then used to calculate how similar the resume is to each job role.

Higher similarity indicates a better match.

---

# 📚 Learning Roadmap

If important skills are missing, the system generates a roadmap such as:

### Week 1
Learn FastAPI

### Week 2
Learn Docker

### Week 3
Learn AWS Cloud

### Week 4
Deploy an ML Model

---

# 📈 Outputs

The application provides:

- Resume Information
- Extracted Skills
- Match Score
- Recommended Job Roles
- Missing Skills
- Learning Roadmap
- PDF Analysis Report

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI_Resume_Analyzer.git
```

Move into the project folder

```bash
cd AI_Resume_Analyzer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 📦 Requirements

- Python 3.10+
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- PyPDF
- python-docx
- ReportLab

---

# 🧪 Testing

The project has been tested with multiple resumes for different job roles.

Test Cases:

- Data Analyst Resume
- AI Engineer Resume
- Python Developer Resume
- Machine Learning Resume

The extracted skills, recommendations, and match scores were verified for consistency.

---

# 📸 Screenshots

Add screenshots here:

- Home Page
- Resume Upload
- Match Score
- Job Recommendations
- Skill Gap Analysis
- Learning Roadmap
- PDF Report

---

# 🔮 Future Enhancements

- Sentence Transformers for semantic matching
- LLM-based Resume Feedback
- Resume Improvement Suggestions
- FastAPI Backend
- Docker Deployment
- PostgreSQL Database
- User Login System
- Resume History
- Cloud Deployment
- Job Description Upload

---

# ⚠️ Responsible AI

- This tool is designed for educational purposes only.
- Match scores are estimates and should not be used for hiring decisions.
- Protected personal information such as gender, age, religion, nationality, or disability is not used in scoring.
- Uploaded resumes are processed only for analysis.

---

# 👩‍💻 Author

**Amulya Lingisetti**

B.Tech – Computer Science and Engineering (Artificial Intelligence & Machine Learning)

VIT-AP University

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

- Streamlit
- Scikit-learn
- Pandas
- Plotly
- PyPDF
- Python-Docx
- Open Source Community
