import warnings
warnings.filterwarnings('ignore')

import os
from dotenv import load_dotenv

# load OPENAI API key
load_dotenv('env.txt')
openai_api_key = os.getenv('OPENAI_API_KEY')

# load langchain libraries

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate

import gradio as gr

# initialise ChatModel with API key
chat_model = ChatOpenAI(
    model_name = 'gpt-3.5-turbo',
    temperature=0,
    openai_api_key=openai_api_key
)
