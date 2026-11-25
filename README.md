
# 🎯 JobFit AI - Smart Resume Analyzer

An NLP-powered resume analyzer that compares a candidate's
resume with a job description.

## Features

- Resume and job description comparison
- TF-IDF text vectorization
- Cosine similarity score
- Matching skills detection
- Missing skills identification
- Improvement suggestions
- Interactive web interface

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- Natural Language Processing
- TF-IDF
- Cosine Similarity

## How It Works

1. User enters a resume and job description.
2. TF-IDF converts text into numerical vectors.
3. Cosine similarity calculates document similarity.
4. A predefined skill database identifies matching
   and missing skills.
5. Improvement suggestions are generated.

## Installation

Clone the repository:

git clone YOUR_REPOSITORY_URL

Navigate to the folder:

cd JobFit-AI

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## Limitations

- Similarity score is not hiring probability.
- Skill extraction uses a predefined dictionary.
- The system does not verify actual skill proficiency.

## Author

Akshat Gaur
