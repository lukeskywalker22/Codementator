import warnings
warnings.filterwarnings('ignore')

import os
from dotenv import load_dotenv, find_dotenv

# load langchain libraries
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import HumanMessage

import streamlit as st

basedirectory = os.path.dirname(__file__)

# load OPENAI API key
load_dotenv(os.path.join(os.path.dirname(__file__), "env.txt"))
openai_api_key = os.getenv('OPENAI_API_KEY')
print(openai_api_key)

# initialise ChatModel with API key
llm = ChatOpenAI(
    openai_api_key=openai_api_key
)
print("initialized successfully")

def add_comments_to_code(input_code):
    query = "Add comments to the following python code: " + input_code
    message = [HumanMessage(content=query)]
    return llm.invoke(message).content

# Streamlit app layout
def main():
    st.title("Code Commenter App")
    code_input = st.text_area("Enter your code snippet:", height=200)

    # Button to trigger code commenting (not functional in this template)
    if st.button("Add Comments"):
        # Perform code commenting (replace with actual logic)
        commented_code = add_comments_to_code(code_input)

        # Display the commented code in a separate text widget
        st.text_area("Code with Comments:", value=commented_code, height=200)

main()
