import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(page_title="pdfchat", page_icon='📝')  # page title
st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1.0">', unsafe_allow_html=True)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(input)
        return response.text

    # Define function to extract text from PDF
def input_pdf_text(uploaded_file):
            reader = pdf.PdfReader(uploaded_file)
            text = ""
            for page in range(len(reader.pages)):
                page = reader.pages[page]
                text += str(page.extract_text())
            return text

input_prompt = """
      Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
        provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
        Context:\n {text}?\n
        Question: \n{user_question}\n

        Answer:
    
        """
    
st.title("Chat with YOUR PDFS")

uploaded_files = st.file_uploader("Upload Your PDFS", type="pdf", help="please upload the pdf", accept_multiple_files=True)

    
user_question = st.text_input("HAVE a NICE chat with your PDFS")


if st.button("submit"):
        with st.spinner("Processing..."):
            if uploaded_files is not None:
                for uploaded_file in uploaded_files:
                    text = input_pdf_text(uploaded_file)
                    response = get_gemini_response(text)  # Pass text instead of input_prompt
                    output_Text = response
                    if(output_Text):
                        st.write(response)
                        st.balloons()
                    else:
                          st.write("upload another file")
                    
st.warning("clear the cache at the top left side by clicking --->  ⋮  ")
   