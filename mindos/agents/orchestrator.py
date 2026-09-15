import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from mindos.state import MindosState

# Carrega as variáveis de ambiente (.env) antes da inicialização do modelo
load_dotenv()

# Inicializa o modelo da Groq
orchestrator_llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

def orchestrator_node(state: MindosState):
    """
    Nó do Orquestrador: analisa o estado atual do projeto
    e decide a próxima ação do sistema.
    """
    objective = state.get("objective", "Objetivo não especificado")
    
    system_prompt = (
        "Você é o agente Orquestrador do MINDOS. "
        "Sua função é analisar o objetivo atual e determinar a próxima etapa."
    )
    prompt = f"Objetivo do projeto: {objective}"
    
    response = orchestrator_llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=prompt)
    ]).content.strip().lower()
    
    return {"next_node": response}