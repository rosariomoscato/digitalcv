from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Rosario Moscato"
PAGE_ICON = "📜"
NAME = "Rosario Moscato"
DESCRIPTION = """
Artificial intelligence Scientist, Developer, Evangelist and Ethicist
"""
EMAIL = "rosario.moscato@outlook.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/rosariomoscato",
    "GitHub": "https://github.com/rosariomoscato",
    "Replit": "https://replit.com/@rosariomoscato",
    "Udemy": "https://www.udemy.com/user/rosario-moscato/",
}
PROJECTS = {    
    "🏆 Introduction to Natural Language Processing - NLP Course with 3 Universities": "https://powerlearning.anahuaconline.com/course/nlp",
    "🏆 Covid19 Detection Tool - Web app for Covid19 diagnosis": "https://rosariomoscato-covid19detectiontool.streamlit.app/",
    "🏆 Web Applications from Scratch with Streamlit - Best Seller Course": "https://www.udemy.com/course/web-app-from-scratch-with-streamlit/",
    "🏆 Time Series Wizard - Web app to make forecasts with Time Series": "https://rosariomoscato-time-series-wizard.streamlit.app/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Ai enthusiastic, Head of Ai and Data Science teams
- ✔️ 20+ years worldwide experience (Europe, Asia, America)
- ✔️ Conference Speaker and Technical/Scientific Consultant
- ✔️ Author of two books about Ai and future
- ✔️ Teacher (Udemy and Universities)
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👨‍💻 Programming: Python (sklearn, keras, Generative Ai), SQL, HTML
- 📊 Data Visulization: Matplotlib, Plotly, Seaborn, Streamlit, Gradio
- 📚 Modeling: Classic ML, Neural Networks, Time Series, NLP, LLM, Generative AI
- 🗄️ Databases: Relational DBs, Postgres, NoSQL Data Bases, Airtable
- 💾 Operating Systems: Linux, macOS, Windows
- 🏭 MLOps: Git, DVC, mlflow, Docker, BentoML, Evidently AI
- 🔗 No-code: Glide, Bubble
- 🤖 Automation: Make
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Technical Director | Live Tech**")
st.write("12/2022 - Present")
st.write(
    """
- ► Define technical direction, group competencies and technologies, best practices and MLOps guidelines
- ► Lead a team of 20+ Data Scientists, Data Engineers, Programmers, Back&Front End Specialists in order to deliver on-time and on-budget quality Ai solution to clients
- ► Design/implementation of Ai business solutions and architectures for many of the most relevant enterprises in Italy and abroad
- ► Very involved in networking and branding activities, partecipating to conferences, events and speaches
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Senior Data Scientist | NTT Data**")
st.write("03/2022 - 11/2022")
st.write(
    """
- ► Design/implementation of Ai business solutions and architectures for many of the most relevant public and private companies
- ► Manage a team of ~10 Data Scientists and Data Engineers
- ► Strongly involved in networking activities with universities and research groups
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Senior Technical Account Manager | Almawave**")
st.write("02/2020 - 02/2022")
st.write(
    """
- ► Design/customize Ai business solutions and architectures for company's clients
- ► Estimate projects' costs and risks from implementation and conduction point of view
- ► Coach and teacher of Ai solutions and tools for many public and private clients 
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Owner of an Artificial intelligence Studio | Self employed**")
st.write("08/2018 - 02/2020")
st.write(
    """
- ► Design, training, evaluation and deployment of Ai models (PoC and Web Apps)
- ► Deep know-how about features treatment (engineering and selection) especially in case of imbalanced datasets 
- ► Ai educator and teacher for companies, universities and on-line platforms
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
