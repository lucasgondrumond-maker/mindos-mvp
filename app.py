import os
import streamlit as st
from dotenv import load_dotenv

# 1. Carrega as variáveis de ambiente e configura a chave da Groq
load_dotenv()
if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

# 2. Importa a estrutura do agente
from mindos.graph import create_mindos_graph

# 3. Configuração da interface do Streamlit
st.set_page_config(page_title="MINDOS AI", page_icon="🤖", layout="centered")
st.title("🤖 MINDOS - Agente Autônomo")

@st.cache_resource
def load_agent():
    return create_mindos_graph()

graph = load_agent()

# 4. Inicialização do histórico de mensagens na sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Renderiza o histórico de chat na tela
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 6. Campo de entrada para o usuário
if user_input := st.chat_input("Digite sua mensagem aqui..."):
    # Exibe a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Processa a resposta do agente
    with st.chat_message("assistant"):
        with st.spinner("MINDOS está pensando..."):
            result = graph.invoke({"objective": user_input})
            
            # Extrai o conteúdo em texto da resposta
            if isinstance(result, dict) and "response" in result:
                resposta = result["response"]
            elif isinstance(result, dict) and "messages" in result and len(result["messages"]) > 0:
                last_msg = result["messages"][-1]
                resposta = getattr(last_msg, 'content', str(last_msg))
            else:
                resposta = str(result)
                
            st.markdown(resposta)

    st.session_state.messages.append({"role": "assistant", "content": resposta})
