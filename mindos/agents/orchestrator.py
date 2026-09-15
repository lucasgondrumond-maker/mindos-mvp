import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

orchestrator_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

def orchestrator_node(state):
    # Pega a pergunta vinda do estado
    user_input = state.get("objective", "")

    if not user_input:
        return {"response": "Não recebi nenhuma instrução."}

    # Faz a chamada para a IA
    response = orchestrator_llm.invoke([HumanMessage(content=user_input)])
    
    # Retorna o texto direto no dicionário de estado
    return {
        "response": response.content
    }
