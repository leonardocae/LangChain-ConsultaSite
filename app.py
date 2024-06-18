import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_response(user_input):
    return "Eu não sei"

def get_factorstore_from_url(url):
    # Pegar o texto no HTML
    loader = WebBaseLoader(url)
    documents = loader.load()
    
    # Divide o documento em pedaçõs para leitura
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(documents)
    
    return document_chunks

# Configuração do aplicativo
st.set_page_config(page_title="Chat com Sites", page_icon="")
st.title("Chat com Site")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Oi, sou seu assistente virtual. Como posso te ajudar?")
]


# Sidebar         
with st.sidebar:
    st.header("Configurações")
    website_url = st.text_input("URL do site")

if website_url is None or website_url == "":
    st.info("Por favor, coloque a URL aqui")

else:       
    document_chunks = get_factorstore_from_url(website_url)
    with st.sidebar:
        st.write(document_chunks)
        
    # User Input           
    user_query = st.chat_input("Coloque sua mensagem aqui...")
    if user_query is not None and user_query != "":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))
    
    
# Conversa
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)
        