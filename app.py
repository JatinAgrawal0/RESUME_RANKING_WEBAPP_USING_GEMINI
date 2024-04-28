import streamlit as st
import PyPDF2 as pdf
import os
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

os.environ['GOOGLE_API_KEY'] = st.secrets["API_KEY"]  # Set your Google API key here
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Add a function to extract a brief description from the response
def extract_description(response):
    # Split the response into lines and take the first few lines as the description
    lines = response.split("\n")
    description = " ".join(lines[:2])  # Adjust the number of lines for the description
    return description

input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of the tech field, software engineering, data science,
data analysis, and big data engineering. Your task is to evaluate the resumes based
on the given job description. You must consider the job market is very competitive
and you should provide the best assistance for improving the resumes. Assign the
percentage matching based on JD and the missing keywords with high accuracy.
resume:{text}
description:{jd}

I want the response as per below structure
{{"JD Match": "%", "MissingKeywords": [], "Profile Summary": ""}}
"""

st.set_page_config(page_title="Smart ATS for Resumes", layout="wide")

st.title("Smart Application Tracking System")

jd = st.text_area("Paste the Job Description")
uploaded_files = st.file_uploader("Upload Your Resumes", type="pdf", accept_multiple_files=True,
                                  help="Please upload the resumes in PDF format")

submit = st.button("Submit")

if submit:
    if uploaded_files and jd:
        ranked_resumes = []
        for uploaded_file in uploaded_files:
            text = input_pdf_text(uploaded_file)
            input_text = input_prompt.format(text=text, jd=jd)
            response = get_gemini_response(input_text)
            if len(text) > 0:
                match_percentage = min(len(jd) / len(text) * 100, 100)
            else:
                match_percentage = 0
            description = extract_description(response)  # Extract description
            ranked_resumes.append({"name": uploaded_file.name, "match_percentage": match_percentage, "response": response, "description": description})  # Include description

        ranked_resumes = sorted(ranked_resumes, key=lambda x: x["match_percentage"], reverse=True)
        df = pd.DataFrame(ranked_resumes)
        df["Rank"] = range(1, len(df) + 1)

        # Display ranked resumes in a table format
        st.table(df[["name", "Rank", "match_percentage","description"]].rename(columns={"name": "RESUME_NAME", "match_percentage": "MATCH_PERCENTAGE", "description": "DESCRIPTION"}))

       
