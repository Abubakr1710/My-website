from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.docx"
profile_pic = current_dir / "assets" / "picture.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Abubakr Mamajonov"
PAGE_ICON = ":wave:"
NAME = "Abubakr Mamajonov"
DESCRIPTION = """
Computer Vision | Deep Learning | Machine Learning | Data Science
"""
EMAIL = "mamajonov1710@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/abubakrmamajonov",
    "GitHub": "https://github.com/Abubakr1710",
    "Twitter": "https://twitter.com/Abubakr1710",
    "Facebook": "https://www.facebook.com/abubakr.mamajonov.75",
}
PROJECTS = {
    "🏆 Fire Detection": "https://github.com/Abubakr1710/Fire-Detection",
    "🏆 Garbage classification": "https://github.com/Abubakr1710/Garbage-Classificator",
    "🏆 Fashion Project": "https://github.com/Abubakr1710/Fashion-project",
    "🏆 MNIST Digit classification": "https://github.com/Abubakr1710/CNN-MNIST",
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
st.subheader("Work Experience")
st.write(
    """
- ✔️ **Volunteer**
- 🏢 **Volunteer** in **Mentoring Program** at [**Vistula University in Warsaw**](https://www.vistula.edu.pl/en) (2022 - present)
- 🔍 Help for new students from arrivig to start their study.
- 🔍 Help to new students for documents and legalizetion.
- ✔️ **Accountant** 
- 🏢 **Metal Decor Business Ltd, Kokand, Uzbekistan, 2018 - 2019** 
- 🔍 Responsible for pricing new products and organizing night shift of the company. 
- 🔍 Social responsibility. I have experience working in team.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, PostgreSQL.
- 📊 Data Analysis: NumPy, Pandas, Matplotlib, Seaborn, 
- 📚 Machine Learning: Scikit-Learn, Spacy, 
- 📈 Deep Learning: Pytorch
- 🌐 Web application: HTML, CSS, Bootstrap, Streamlit, Flask, Docker
"""
)


# --- Education ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- 🏢 **Bachelor in Computer Engineering**
- 🏢 [**Vistula University in Warsaw**](https://www.vistula.edu.pl/en) (2020 - present)
- ✔️ **Certification of Bootcamp** 
- 🏢 [**Epicode Global**](https://epicode.com/en/) (Feb, 2022 - Nov, 2022)
- ✔️ **Upper Secondary Diploma in Exact Science**
- 🏢 [**Kokand State University**](https://kdu.uz/en/) (2015 - 2019)
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")