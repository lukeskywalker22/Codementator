# Codementator
Codementator is a helpful AI assistant to assist you while you code, either with friends or solo. The AI helps you add important comments to aid other collaborators in understanding your ~~incomprehensible~~ code. It can also be used to explain the code indepthly.

<ins>To run the code</ins>:
1. In the same folder, add a text file with your OpenAI API Key (OPENAI_API_KEY="sk-1234..") and name it `env.txt`.
2. Run the file and then type `streamlit run [file_name].py` in terminal.


## Utilising it:
<ins>Normal mode vs Advanced mode</ins>:

![image](https://github.com/lukeskywalker22/Codementator/assets/145328729/67f9dd3e-243d-4a84-8d7e-7d01dec12cbc)

Copy and paste your code into the textbox, and select a coding language, and choose whether to get the AI to explain or comment your code.

Advanced mode allows you to tweak the temperature and the frequency of comment appearing in the code.

![image](https://github.com/lukeskywalker22/Codementator/assets/145328729/e21ded6e-d15a-41bd-bb5c-e4ca05ec73e1)

## How it works:
Our code commentator makes use of GPT-3.5 to indepthly explain and annotate code. We access GPT-3.5 using Langchain.
