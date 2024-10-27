import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain_community.callbacks.manager import get_openai_callback
from helper_functions.utility import check_password 


import os
from dotenv import load_dotenv

load_dotenv('.env')

# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Load PDF and prepare for querying
loader = PyPDFLoader("data/GuideToFilming040321.pdf")
pages = loader.load_and_split()

text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=500,
    chunk_overlap=50,
    length_function=len
)

chunks = text_splitter.split_documents(pages)

# create embeddings
embeddings = OpenAIEmbeddings()
knowledge_base = FAISS.from_documents(chunks, embeddings)

# Initialize the LLM
llm = OpenAI() 

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="SFC's Chatbot"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("🤖 Understand Location Filming in SG - Chatbot 🤖")

# Check if the password is correct.  
if not check_password():  
    st.stop()

st.markdown(
    """
    Please use this 🤖 Chatbot only for queries relating to location filming in Singapore. 
    """
    )

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")

if user_prompt:
        docs = knowledge_base.similarity_search(user_prompt)
        
        chain = load_qa_chain(llm, chain_type="stuff")
        
        with get_openai_callback() as cb:
          response = chain.run(input_documents=docs, question=user_prompt)
          print(cb)
           
        st.write(response)


        st.divider()


with st.expander("Disclaimer"):
    st.write('''
    IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

    Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

    Always consult with qualified professionals for accurate and personalised advice.

    ''')