import streamlit as st
from dotenv import load_dotenv
from mindos.graph import create_mindos_graph

load_dotenv()

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
            resposta = result.get("next_node", str(result))
            st.markdown(resposta)

    st.session_state.messages.append({"role": "assistant", "content": resposta})
