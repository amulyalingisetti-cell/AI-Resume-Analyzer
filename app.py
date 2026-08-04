from roadmap import generate_roadmap
import streamlit as st
import plotly.express as px
import pandas as pd
from text_cleaner import clean_text
from report_generator import generate_pdf_report
from resume_parser import extract_pdf, extract_docx
from skill_extractor import extract_skills
from matcher import match_jobs

# ===============================
# Page Configuration
# ===============================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# ===============================
# Custom CSS
# ===============================

st.markdown("""
<style>

.main{
    background-color:#f7f9fc;
}

h1,h2,h3{
    color:#003366;
}

.stButton>button{
    background:#0066cc;
    color:white;
    border-radius:10px;
}

div[data-testid="metric-container"]{
    background:#f0f8ff;
    padding:15px;
    border-radius:12px;
    border:1px solid #ddd;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# Header
# ===============================

st.markdown("""
<div style='background:linear-gradient(90deg,#0066cc,#00b4d8);
padding:25px;
border-radius:15px;
text-align:center;
color:white;'>

<h1>🤖 AI Resume Analyzer & Job Recommendation System</h1>

<h4>
Upload Resume • Extract Skills • Match Jobs • Learning Roadmap
</h4>

</div>

""", unsafe_allow_html=True)

st.write("")

uploaded_file = st.file_uploader(
    "📂 Upload Resume",
    type=["pdf", "docx"],
    key="resume_upload_unique"
)

import io


if uploaded_file is not None:

    st.success(f"Uploaded Successfully: {uploaded_file.name}")

    file_name = uploaded_file.name.lower()
    file_bytes = uploaded_file.read()

    if file_name.endswith(".pdf"):
        resume_text = extract_pdf(io.BytesIO(file_bytes))

    elif file_name.endswith(".docx"):
        resume_text = extract_docx(io.BytesIO(file_bytes))

    else:
        st.error("Unsupported file type")
        st.stop()

    resume_text = clean_text(resume_text)
    
    st.write("Text length extracted:", len(resume_text)) # Debug
    
    if len(resume_text) < 10:
        st.warning("Could not extract text. File might be image-based PDF or empty docx")
    
    st.text_area("Resume Content", resume_text, height=300, key="resume1")

    resume_text = clean_text(resume_text) 

    import re

st.subheader("📄 Extracted Resume Summary")

# ---------- Name ----------
lines = [line.strip() for line in resume_text.split("\n") if line.strip()]
name = lines[0].title() if lines else "Not Found"

# ---------- Email ----------
email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', resume_text)
email = email_match.group() if email_match else "Not Found"

# ---------- Phone ----------
phone_match = re.search(r'(\+91[\s-]?)?[6-9]\d{9}', resume_text)
phone = phone_match.group() if phone_match else "Not Found"

# ---------- Skills ----------
skills = extract_skills(resume_text)
skills_text = ", ".join(skills[:10])

# ---------- Education ----------
education = "B.Tech (AI & ML)" if "btech" in resume_text.lower() else "Not Found"

# ---------- Projects ----------
projects = []

project_list = [
    "TravelSphere Management System",
    "PocketWise Fintech Application",
    "Global AI Job Salaries Analysis",
    "NYC Airbnb Price Prediction",
    "Smart Crop Advisory System",
    "AI Resume Analyzer"
]

for project in project_list:
    if project.lower() in resume_text.lower():
        projects.append(project)

# ---------- Display ----------
col1, col2 = st.columns(2)

with col1:
    st.success(f"👤 Name\n\n{name}")
    st.success(f"📧 Email\n\n{email}")
    st.success(f"📱 Phone\n\n{phone}")

with col2:
    st.success(f"🎓 Education\n\n{education}")
    st.success(f"💻 Skills\n\n{len(skills)} Skills Found")
    st.success(f"📂 Projects\n\n{len(projects)} Projects")

st.markdown("---")

st.subheader("📂 Project Names")

for project in projects:
    st.info(project)

st.markdown("---")

with st.expander("📄 View Full Extracted Resume"):
    st.text_area(
        "Resume Text",
        resume_text,
        height=250,
        key="resume_preview"
    )

    skills = extract_skills(resume_text)
    st.subheader("🎯 Skills Found")
    st.write(", ".join(skills))

    st.subheader("🎯 Skills Found")
    col1,col2,col3 = st.columns(3)

    for i,skill in enumerate(skills):

        if i%3==0:
            col1.success(skill)

        elif i%3==1:
            col2.success(skill)

        else:
            col3.success(skill)

    # ===============================
    # Skill Categories
    # ===============================

    st.subheader("📚 Skill Categories")

    categories = {
        "Programming":[],
        "Web Development":[],
        "AI / ML":[],
        "Database":[],
        "Cloud":[],
        "Tools":[]
    }

    for skill in skills:

        s = skill.lower()

        if s in ["python","java","c","c++"]:
            categories["Programming"].append(skill)

        elif s in ["html","css","javascript","react"]:
            categories["Web Development"].append(skill)

        elif s in [
            "machine learning",
            "linear regression",
            "scikit-learn",
            "pandas",
            "numpy",
            "matplotlib",
            "tensorflow",
            "pytorch"
        ]:
            categories["AI / ML"].append(skill)

        elif s in [
            "sql",
            "sqlite",
            "mysql",
            "postgresql"
        ]:
            categories["Database"].append(skill)

        elif s in [
            "aws cloud",
            "ibm cloud"
        ]:
            categories["Cloud"].append(skill)

        else:
            categories["Tools"].append(skill)

    for category,items in categories.items():

        if items:

            st.info(
                f"**{category}** : {', '.join(items)}"
            )

    # ===============================
    # Job Matching
    # ===============================

    results = match_jobs(skills)

    st.subheader("📊 Job Match Scores")

    chart_df = pd.DataFrame({

        "Role":[job["Role"] for job in results],

        "Match Score":[job["Score"] for job in results]

    })

    fig = px.bar(

        chart_df,

        x="Role",

        y="Match Score",

        text="Match Score",

        color="Match Score"

    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(
        fig,
        use_container_width=True
    )    # ===============================
    # Select Target Role
    # ===============================

    st.subheader("💼 Job Recommendation")

    roles = [job["Role"] for job in results]

    selected_role = st.selectbox(
        "🎯 Select Your Target Role",
        roles
    )

    selected_job = next(
        job for job in results
        if job["Role"] == selected_role
    )

    # ===============================
    # Resume Analysis
    # ===============================

    st.subheader("📊 Resume Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Resume Score",
            f"{selected_job['Score']}/100"
        )

        st.progress(selected_job["Score"] / 100)

    with col2:

        if selected_job["Score"] >= 90:

            st.success("🏆 Excellent Resume")

            st.write(
                "Your resume is highly suitable for this role."
            )

        elif selected_job["Score"] >= 70:

            st.info("👍 Good Resume")

            st.write(
                "A few more skills will make you job ready."
            )

        elif selected_job["Score"] >= 50:

            st.warning("⚠ Average Resume")

            st.write(
                "Improve your skills using the roadmap."
            )

        else:

            st.error("❌ Needs Improvement")

            st.write(
                "You need to learn several important skills."
            )

    # ===============================
    # Matched Skills
    # ===============================

    st.subheader("✅ Skills You Already Have")

    if selected_job["Matched"]:

        cols = st.columns(3)

        for i, skill in enumerate(selected_job["Matched"]):

            cols[i % 3].success(skill.title())

    else:

        st.warning("No matching skills found.")

    # ===============================
    # Missing Skills
    # ===============================

    st.subheader("❌ Skills You Need")

    if selected_job["Missing"]:

        cols = st.columns(3)

        for i, skill in enumerate(selected_job["Missing"]):

            cols[i % 3].error(skill)

    else:

        st.success("🎉 No Missing Skills")

    # ===============================
    # Learning Roadmap
    # ===============================

    st.subheader("📚 Personalized Learning Roadmap")

    roadmap = generate_roadmap(
        selected_job["Missing"]
    )
    roadmap = generate_roadmap(selected_job["Missing"])

    for step in roadmap:
         st.info(step)

    # ===============================
    # Career Suggestion
    # ===============================

    st.subheader("🚀 Career Suggestion")

    if selected_job["Score"] >= 90:

        st.success(
            f"You are ready to apply for **{selected_job['Role']}** internships."
        )

    elif selected_job["Score"] >= 70:

        st.info(
            f"Learn the remaining skills and apply for **{selected_job['Role']}** positions."
        )

    else:

        st.warning(
            f"Complete the roadmap before applying for **{selected_job['Role']}** jobs."
        )    # ===============================
    # Download Resume Report
    # ===============================

    st.subheader("📥 Download Resume Report")

    report = f"""
===============================
AI Resume Analysis Report
===============================

Target Role:
{selected_job['Role']}

Resume Match Score:
{selected_job['Score']}%

--------------------------------
Skills You Have
--------------------------------

"""

    if selected_job["Matched"]:
        for skill in selected_job["Matched"]:
            report += f"• {skill}\n"
    else:
        report += "None\n"

    report += """

--------------------------------
Missing Skills
--------------------------------

"""

    if selected_job["Missing"]:
        for skill in selected_job["Missing"]:
            report += f"• {skill}\n"
    else:
        report += "None\n"

    report += """

--------------------------------
Learning Roadmap
--------------------------------

"""

    for step in roadmap:
        report += f"• {step}\n"

    report += """

--------------------------------
Career Suggestion
--------------------------------

"""

    if selected_job["Score"] >= 90:
        report += f"You are ready to apply for {selected_job['Role']} roles.\n"

    elif selected_job["Score"] >= 70:
        report += f"Learn the missing skills and start applying for {selected_job['Role']} roles.\n"

    else:
        report += f"Complete the roadmap before applying for {selected_job['Role']} jobs.\n"

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="Resume_Analysis_Report.txt",
        mime="text/plain"
    )

    # ===============================
    # Skill Distribution Chart
    # ===============================

    st.subheader("📈 Skill Distribution")

    category_count = {}

    for category, items in categories.items():
        if len(items) > 0:
            category_count[category] = len(items)

    pie_df = pd.DataFrame({
        "Category": list(category_count.keys()),
        "Skills": list(category_count.values())
    })

    if not pie_df.empty:
        fig2 = px.pie(
            pie_df,
            names="Category",
            values="Skills",
            title="Resume Skill Distribution"
        )

        st.plotly_chart(fig2, use_container_width=True)

    # ===============================
    # Final Summary
    # ===============================

    st.subheader("📝 Final Summary")

    st.success(f"🎯 Target Role : {selected_job['Role']}")

    st.info(f"📊 Resume Match Score : {selected_job['Score']}%")

    st.write(f"✅ Total Skills Found : **{len(skills)}**")

    st.write(f"✅ Matched Skills : **{len(selected_job['Matched'])}**")

    st.write(f"❌ Missing Skills : **{len(selected_job['Missing'])}**")

    # ===============================
    # Responsible AI Notice
    # ===============================

    st.divider()

    st.warning("""
### 🤖 Responsible AI Notice

• Match scores are estimates based on extracted skills.

• This system ignores personal information like age, gender,
religion, caste, nationality, or address.

• Recommendations are generated only from technical skills.

• Final hiring decisions should always be made by recruiters.

• This project is intended for educational and portfolio purposes.
""")

    # ===============================
    # Footer
    # ===============================

    st.markdown("---")

    st.markdown(
        """
        <div style="text-align:center; color:gray;">
        <h4>🤖 AI Resume Analyzer & Job Recommendation System</h4>
        <p>Developed using Python • Streamlit • Plotly • Machine Learning</p>
        </div>
        """,
        unsafe_allow_html=True
    )
