import warnings
warnings.filterwarnings('ignore')

import os
from dotenv import load_dotenv

# load langchain libraries
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate

import streamlit as st

# load OPENAI API key
load_dotenv('env.txt')
openai_api_key = os.getenv('OPENAI_API_KEY')
print(openai_api_key)

# initialise ChatModel with API key
chat_model = ChatOpenAI(
    model_name = 'gpt-3.5-turbo',
    temperature=0.5,
    openai_api_key=openai_api_key
)

def add_comments_to_code(input_code):
    # Function to add comments to the input code (replace with your logic)
    # Currently, it simply adds a comment prefix to each line.
    commented_code = "\n".join(["# " + line for line in input_code.split("\n")])
    return commented_code

# Streamlit app layout
def main():
    st.title("Code Commenter App")

    # Input textarea for code snippet
    code_input = st.text_area("Enter your code snippet:", height=200)

    # Button to trigger code commenting (not functional in this template)
    if st.button("Add Comments"):
        # Perform code commenting (replace with actual logic)
        commented_code = add_comments_to_code(code_input)

        # Display the commented code in a separate text widget
        st.text_area("Code with Comments:", value=commented_code, height=200)

main()

