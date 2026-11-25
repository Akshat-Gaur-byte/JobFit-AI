
import streamlit as st
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# PAGE SETTINGS

st.set_page_config(
    page_title="JobFit AI",
    page_icon="🎯",
    layout="wide"
)


# TITLE

st.title("🎯 JobFit AI")
st.subheader("Smart Resume Analyzer")

st.write(
    "Compare your resume with a job description "
    "using Artificial Intelligence and NLP."
)

st.divider()


# SKILL DATABASE

SKILLS = [
    "python", "java", "c++", "javascript",
    "sql", "html", "css", "react",
    "machine learning", "deep learning",
    "artificial intelligence", "data analysis",
    "data science", "tensorflow", "pytorch",
    "pandas", "numpy", "scikit-learn",
    "flask", "django", "streamlit",
    "git", "github", "docker",
    "communication", "leadership",
    "problem solving", "excel",
    "power bi", "tableau", "aws",
    "cloud computing", "nlp"
]


# SKILL EXTRACTION

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:

        pattern = r'(?<!\w)' + re.escape(skill) + r'(?!\w)'

        if re.search(pattern, text):
            found.append(skill.title())

    return found


# AI SIMILARITY CALCULATION

def calculate_similarity(resume, job):

    documents = [resume, job]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    matrix = vectorizer.fit_transform(documents)

    score = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    return round(score * 100, 2)


# USER INPUT

col1, col2 = st.columns(2)

with col1:

    st.subheader("📄 Your Resume")

    resume = st.text_area(
        "Paste your resume",
        height=250,
        placeholder="Enter your resume here..."
    )

with col2:

    st.subheader("💼 Job Description")

    job = st.text_area(
        "Paste job description",
        height=250,
        placeholder="Enter the job requirements here..."
    )


# ANALYSIS BUTTON

if st.button("🚀 Analyse My Resume", use_container_width=True):

    if not resume.strip() or not job.strip():

        st.warning("Please enter both texts.")

    else:

        score = calculate_similarity(resume, job)

        resume_skills = extract_skills(resume)

        job_skills = extract_skills(job)

        matching = [
            skill for skill in job_skills
            if skill in resume_skills
        ]

        missing = [
            skill for skill in job_skills
            if skill not in resume_skills
        ]


        # RESULTS

        st.divider()

        st.header("📊 Analysis Results")

        a, b, c = st.columns(3)

        a.metric("Match Score", f"{score}%")
        b.metric("Matching Skills", len(matching))
        c.metric("Missing Skills", len(missing))

        st.progress(score / 100)

        st.caption(
            "Similarity score is not a prediction of hiring success."
        )

        st.divider()


        # MATCHING SKILLS

        left, right = st.columns(2)

        with left:

            st.subheader("✅ Matching Skills")

            if matching:

                for skill in matching:
                    st.success(skill)

            else:
                st.info("No matching skills detected.")


        # MISSING SKILLS

        with right:

            st.subheader("❌ Missing Skills")

            if missing:

                for skill in missing:
                    st.error(skill)

            else:
                st.success("No missing skills detected!")


        # SUGGESTIONS

        st.divider()

        st.header("💡 Improvement Suggestions")

        if missing:

            for skill in missing:

                st.write(
                    f"Consider learning or demonstrating {skill} "
                    "through a practical project, if relevant."
                )

        else:

            st.success(
                "All detected job skills are present in your resume!"
            )


st.divider()

st.caption("JobFit AI | Built with Python, NLP and Scikit-learn")
