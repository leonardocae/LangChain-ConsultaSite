import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def get_response(user_input):
    return "Eu não sei"

# Configuração do aplicativo
st.set_page_config(page_title="Chat com Sites", page_icon="")
st.title("Chat com Site")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
    AIMessage(content="Oi, sou seu assistente virtual, como posso te ajudar?")
]


# Sidebar         
with st.sidebar:
    st.header("Configurações")
    website_url = st.text_input("URL do site")

# User Input    
user_query = st.chat_input("Coloque sua mensagem aquii...")
if user_query is not None and user_query != "":
    response = get_response(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=response))
    with st.chat_message("Human"):
        st.write(user_query)
    with st.chat_message("AI"):
        st.write(response)

with st.sidebar:
    st.write(st.session_state.chat_history)
    
    
# Conversa
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)
        