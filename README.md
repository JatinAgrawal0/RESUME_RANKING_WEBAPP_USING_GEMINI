# Smart ATS for Resumes 📄🔍

This Smart Application Tracking System (ATS) is designed to evaluate resumes against a given job description. It provides insights on match percentage, missing keywords, and profile summaries to assist in resume screening.

## Features

✨ **Streamlit Interface**: User-friendly interface created using Streamlit for easy interaction.

🔍 **GenerativeAI Integration**: Utilizes Google's GenerativeAI API for analyzing resumes and providing feedback.

📄 **PDF Resume Support**: Supports uploading resumes in PDF format, processed using PyPDF2.

## Setup

1. **Install Dependencies**: Ensure you have Python installed. Install required Python packages using pip:

2. **Set up Google API Key**: Obtain a Google API key and set it as an environment variable named `GOOGLE_API_KEY`. You can also directly set it in the script.

3. **Run the Application**: Start the Streamlit application by running:

## Usage

1. **Paste Job Description**: Enter the job description in the provided text area.

2. **Upload Resumes**: Upload resumes in PDF format using the file uploader.

3. **Submit**: Click the submit button to evaluate the resumes against the job description.

4. **Review Results**: View the ranked resumes, match percentages, and descriptions in the table format.

## Feedback and Contributions

Contributions and feedback are welcome! Feel free to open an issue or submit a pull request to enhance the functionality or address any issues.

## License

This project is licensed under the [MIT License](LICENSE).
