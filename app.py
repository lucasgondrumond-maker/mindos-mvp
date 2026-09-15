import os
import streamlit as st
from dotenv import load_dotenv

# 1. Injeta a chave no sistema ANTES de importar o MINDOS
load_dotenv()
if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

# 2. Importa o módulo do agente somente após a chave estar visível no ambiente
from mindos.graph import create_mindos_graph

st.set_page_config(page_title="MINDOS AI", page_icon="🤖", layout="centered")
st.title("🤖 MINDOS - Agente Autônomo")

@st.cache_resource
def load_agent():
    return create_mindos_graph()

graph = load_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Digite sua mensagem aqui..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("MINDOS está pensando..."):
            result = graph.invoke({"objective": user_input})

# Extrai a resposta tratada do dicionário de estado
if isinstance(result, dict):
    # Tenta pegar da lista de mensagens (padrão LangGraph)
    if "messages" in result and len(result["messages"]) > 0:
        resposta = result["messages"][-1].content
    # Se houver outra chave de saída específica
    elif "response" in result:
        resposta = result["response"]
    else:
        resposta = str(result)
else:
    resposta = str(result)

st.markdown(resposta)

  
