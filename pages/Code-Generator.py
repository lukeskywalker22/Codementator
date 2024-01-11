import warnings
warnings.filterwarnings('ignore')

import os
from dotenv import load_dotenv, find_dotenv

# load libraries
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import HumanMessage

import streamlit as st
from streamlit_modal import Modal

basedirectory = os.path.dirname(__file__)

# load OPENAI API key
load_dotenv(os.path.join(os.path.dirname(__file__), "env.txt"))
openai_api_key = os.getenv('OPENAI_API_KEY')

# initialise ChatModel with API key
llm = ChatOpenAI(
    openai_api_key=openai_api_key,
    temperature=1
)

def generate_code(language, length, question):
    query = "Generate a snippet of code in the " + language + " programming language that performs " + question + "with a maximum length of " + length + ". Do not include any explanations, just generate the code snippet only."  
    message = [HumanMessage(content=query)]
    return llm.invoke(message).content 

st.set_page_config(page_title="Code generator")

st.markdown("# Code generator")
st.write(
    "Stuck on a coding project? Fear not, because we have the perfect tool for you! Enter a prompt below, and our AI model will generate code that fits your needs!"
)
    
option = st.selectbox('Select programming language',('Python', 'Javascript', 'C', 'Java', 'Swift', 'Typescript', 'Rust', 'Ruby', 'CSS', 'HTML', 'C++'))
code_input = st.text_area("Enter your query:", height=100)
length_input = st.text_area("Enter max length of code generated in characters")
if st.button("Generate code"):
    generated_code = generate_code(option, length_input, code_input)
    st.code(generated_code)
