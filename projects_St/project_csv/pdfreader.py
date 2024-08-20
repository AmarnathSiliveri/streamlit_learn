import streamlit as st #framework
import google.generativeai as genai #google generative ai
import os #importing the api keys from another file folders
import PyPDF2 as pdf #pdf parse -text -> chunks->vectors(text_vectors)
from dotenv import load_dotenv 
load_dotenv()


st.set_page_config(page_title="pdfchat", page_icon='📝')  # page title
st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1.0">', unsafe_allow_html=True)

#access to the gemini api
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to genereate response

def get_gemini_response(input):
        model = genai.GenerativeModel('gemini-1.5-pro')#geinipro-gemini flash1.5,gemini viion -pro,gemini1.0
        response = model.generate_content(input)
        return response.text



# Define function to extract text from PDF
def input_pdf_text(uploaded_file):
            reader = pdf.PdfReader(uploaded_file)
            text = ""
            for page in range(len(reader.pages)):
                page = reader.pages[page]
                text += str(page.extract_text())
                text = text+input_prompt
            return text

# input prompt 

input_prompt = """
      Answer the question as detailed as possible from the provided context, make sure to provide all the details, consider the given variables and generate the content 
        Context:{text}
        Question:{user_question}

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
                    response1 = get_gemini_response(text)  # Pass text instead of input_prompt
                    output_Text = response1
                    if(output_Text):
                        st.write(response1)
                        st.balloons()
                    else:
                          st.write("upload another file")
                    
st.warning("clear the cache at the top left side by clicking --->  ⋮  ")


