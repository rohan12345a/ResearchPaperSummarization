import requests
import streamlit as st
from nltk import sent_tokenize
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import fitz
import re
import string
from io import BytesIO
import json
import streamlit_lottie
from  streamlit_lottie import st_lottie


def load_lottieurl(url):
     r= requests.get(url)
     if r.status_code !=200:
         return None
     return r.json()
# 600 600
st.set_page_config(page_title="Research Paper Summarizer",page_icon=":books:",layout="wide", initial_sidebar_state="expanded",)
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

lottie1= load_lottieurl ("https://lottie.host/af254202-9552-40db-957e-e8ccb5833ef2/FHv4IZYl4e.json")
if lottie1 is not None:
    st_lottie(lottie1, speed=1, width=500, height=500)
# lottie_coding2= load_lottieurl ("https://assets3.lottiefiles.com/temp/lf20_nXwOJj.json")
# lottie_coding3= load_lottieurl ("https://assets3.lottiefiles.com/packages/lf20_TmewUx.json")
# lottie_coding4= load_lottieurl ("https://assets10.lottiefiles.com/packages/lf20_GxMZME.json")


# Load your custom T5 model and tokenizer
model_path = "C:\\Users\\Lenovo\\Downloads\\Nlp_model"
model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = T5Tokenizer.from_pretrained(model_path)

# Define the preprocessing function
def preprocess_text(text):
    # Sentence Tokenization
    sentences = sent_tokenize(text)

    # Initialize an empty list to store preprocessed sentences
    preprocessed_sentences = []

    for sentence in sentences:
        # Use regular expressions to remove tables and formulas (customize as needed)
        table_pattern = r"(?i)(?:Table|Tab\.|Fig\.)\s+\d+\s*[:\s-]*\s*(.*?)\s*(?=(?:Table|Tab\.|Fig\.|\n|\Z))"
        sentence = re.sub(table_pattern, "", sentence)

        formula_pattern = r"(\$\$[\s\S]*?\$\$|\$[\s\S]*?\$)"
        sentence = re.sub(formula_pattern, "", sentence)

        # Removing E-mails
        email_pattern = r'\S+@\S+\.\S+'
        sentence = re.sub(email_pattern, '', sentence)

        # Remove Urls
        url_pattern = r'https?://\S+|www\.\S+'
        sentence = re.sub(url_pattern, '', sentence)

        # Lowercasing
        sentence = sentence.lower()

        # Remove Special Characters
        pattern = r'[^\w\s]'
        sentence = re.sub(pattern, ' ', sentence)

        # Remove single alphabets
        sentence = re.sub(r'\s+[a-zA-Z]\s+', ' ', sentence)

        # Removing Numbers
        sentence = re.sub(r'\d+', '', sentence)

        # Removing Punctuations
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))

        # Removing Extra Spaces
        sentence = " ".join(sentence.split())

        # Append the preprocessed sentence to the list
        preprocessed_sentences.append(sentence)

    # Join the preprocessed sentences back into a single string with a space as delimiter
    preprocessed_text = '. '.join(preprocessed_sentences)

    return preprocessed_text

def generate_summary(text):
    input_ids = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(input_ids, num_beams=4, min_length=30, max_length=150, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def convert_pdf_to_text(pdf_bytes):
    pdf_document = fitz.open("temp.pdf", pdf_bytes)
    text = ""
    for page in pdf_document:
        text += page.get_text()
    return text









import streamlit as st

# Add custom CSS to create a gradient background


# Rest of your Streamlit code here






def main():
    st.title("PDF Summarizer")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Convert uploaded file to text
        pdf_bytes = uploaded_file.read()
        pdf_text = convert_pdf_to_text(pdf_bytes)
        preprocessed_text = preprocess_text(pdf_text)

        # Generate summary
        if st.button("Summarize"):
            summary = generate_summary(preprocessed_text)

            st.subheader("Summary")
            st.text_area("Summary Text", value=summary, height=200, max_chars=None)


# Header section
st.subheader("Hello, Welcome to the Research Paper Summarizer!")
st.title("Research Paper Summarizer")



# Use st.markdown with HTML to create a two-column layout
st.markdown("""
<style>
    body {
        background-color: #f0f0f0; /* Light gray color */
    }

    .container {
        display: flex;
        flex-direction: row;
    }
    .column {
        flex: 50%;
        padding: 10px;
    }
</style>
<div class="container">
    <div class="column">
        <h3>Our Aim:</h3>
        <p>Our NLP application is centered around the task of research paper summarization. When a user uploads a PDF document, our system processes the content and generates a concise and coherent summary of the research paper's text. This tool aims to streamline the process of extracting key insights and findings from scholarly documents.
        The core of our project lies in the implementation of a fine-tuned T5 model, which has been customized using our proprietary dataset. This fine-tuning process has significantly enhanced the model's performance, resulting in commendable accuracy levels. This means that users can rely on our application to provide accurate and informative summaries that capture the essence of complex research papers.
        With our NLP research paper summarization application, we hope to empower users in their quest for knowledge by simplifying the often daunting task of digesting intricate academic literature.</p>
    </div>
    <div class="column">
        <!-- Add content for the right column if needed -->
    </div>
</div>
""", unsafe_allow_html=True)

if __name__ == '__main__':
    main()

with st.container():
    with st.sidebar:
        members = [
            {"name": "Saksham Jain", "email": "sakshamgr8online@gmail.com",
             "linkedin": "https://www.linkedin.com/in/saksham-jain-59b2241a4/"},

            {"name": "Rohan Saraswat", "email": "rohan.saraswat2003@gmail.com", "linkedin": "https://www.linkedin.com/in/rohan-saraswat-a70a2b225/"},
            {"name": "Amisha Borana ", "email": "amishaborana200326@gmail.com", "linkedin": "https://www.linkedin.com/in/amisha-borana-4a598a200/"}
        ]

        st.markdown("<h1 style='font-size:28px'>Team Members</h1>", unsafe_allow_html=True)

        for member in members:
            st.write(f"Name: {member['name']}")
            st.write(f"Email: {member['email']}")
            st.write(f"LinkedIn: {member['linkedin']}")
            st.write("")



with st.container():
    st.write("---")
    st.header("Your Valuable feedback appricable!")
    st.write("##")

    # Adding some vertical space
    st.write("\n\n\n")

    contact_form = """
    <form action="https://formsubmit.co/rohan.saraswat2003@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px; border-radius: 10px; margin-bottom: 10px;"><br>
        <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 10px; border-radius: 10px; margin-bottom: 10px;"><br>
        <textarea name="message" placeholder="Your message here" required style="width: 100%; padding: 10px; border-radius: 10px; margin-bottom: 10px;"></textarea><br>
        <button type="submit" style="width: 100%; padding: 10px; border-radius: 10px; background-color: #4CAF50; color: white;">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st.empty()










