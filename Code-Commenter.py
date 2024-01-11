# load libraries

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

basedirectory = os.path.dirname(__file__)

# load OPENAI API key
load_dotenv(os.path.join(os.path.dirname(__file__), "env.txt"))
openai_api_key = os.getenv('OPENAI_API_KEY')

# initialise ChatModel with API key
llm = ChatOpenAI(
    openai_api_key=openai_api_key,
    temperature=1
)

print("initialized successfully")

def add_comments_to_code(input_code, language, frequency):
    if frequency == 'Add comments to code':
        query = "Add comments to the following " + language + " code while preserving the structure of the original code and leaving all of the original content inside the response: " + input_code
    elif frequency == 'Add comments to every line of code':
        query = "Add comments to every line of the following" + language + "code while preserving the structure of the original code and leaving all of the original content inside the response: " + input_code
    else:
        query = "Remove all comments from the following code: " + input_code 
    message = [HumanMessage(content=query)]
    return llm.invoke(message).content

def explain_code(input_code, language, temperature):
    llm.temperature = temperature
    query = "Explain the following " + language + " code: " + input_code
    message = [HumanMessage(content=query)]
    return llm.invoke(message).content 

def insult_code(input_code, language, temperature):
    llm.temperature = temperature
    query = "Say some funny insults to the following " + language + "code: " + input_code
    message = [HumanMessage(content=query)]
    return llm.invoke(message).content

# Streamlit app layout
def main():
    #Main screen
    st.title("Codementator")
    st.write("The only app you'll ever need to write code comments")
    st.write("Documentation: [GitHub](https://github.com/lukeskywalker22/Codementator/tree/main)")

    with st.expander("Advanced options", expanded=False):
        temp = st.slider(label="Temperature (randomness of text generation: 0 is least, 2 is most)", min_value=0.0, max_value=2.0, value=1.0)      
        frequency = st.selectbox('Frequency', ('Add comments to code', 'Add comments to every line of code', 'Remove all comments'))

    option = st.selectbox('Select programming language',('Python', 'Javascript', 'C', 'Java', 'Swift', 'Typescript', 'Rust', 'Ruby', 'CSS', 'HTML', 'C++'))
    explaintoggle = st.toggle("Explain mode")
    insulttoggle = st.toggle("Insult my code")
    code_input = st.text_area("Enter your code snippet:", height=300)

    # Button to trigger code commenting (not functional in this template)
    if st.button("Add Comments"):
        # Perform code commenting (replace with actual logic)
        commented_code = add_comments_to_code(code_input, option, frequency)
        explained_code = explain_code(code_input, option, temp)
        insulted_code = insult_code(code_input, option, temp)

        # Display the commented code in a separate text widget
        st.write("Commented code:")
        st.code(commented_code)
        if explaintoggle:
            st.write("Explanation: ")
            st.write(explained_code)
        if insulttoggle:
            st.write("Insults to code:")
            st.write()
    
main()
