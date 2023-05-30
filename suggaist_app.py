import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

st.set_page_config(page_title="suggAIst - An LLM-powered Streamlit app")

# Sidebar contents
with st.sidebar:
    st.title('suggAIst')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](<https://streamlit.io/>)
    - [HugChat](<https://github.com/Soulter/hugging-chat-api>)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](<https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor>) LLM model)

    💡 Note: No API key required!
    ''')
    add_vertical_space(5)
    st.write('With so many choices out there, let us offer some suggAIstions!')

# Generate empty lists for generated and past.
## generated stores AI generated responses

if 'generated' not in st.session_state: # bot's response
    st.session_state['generated'] = ["Don't know what to watch? May I make some suggAIstions?"]

if 'past' not in st.session_state: # human user's input
    st.session_state['past'] = ['Hi!!']

# App's general layout
input_container = st.container() # human user
colored_header(label=' ', description=' ', color_name='blue-30')
response_container = st.container() # bot response

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", " ", key="input")
    return input_text

## Applying the user input box
with input_container:
    user_input = get_text()

# Bot response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = hugchat.ChatBot() # This LLM model can be swapped with any other one
    response = chatbot.chat(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
# Populate the response_container with the AI-generated response with the two underlying if statements:
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))
