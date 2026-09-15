from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from mindos.state import MindosState
from mindos.config import logger

strategist_llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

def strategist_node(state: MindosState):
    logger.info("🎯 [Estrategista] Criando plano de negócios...")

    system_prompt = (
        "Você é o Estrategista do MINDOS. Sua missão é transformar o objetivo do usuário "
        "em um plano de negócios sucinto e acionável com: "
        "Proposta de Valor, Público-Alvo e Modelo de Monetização."
    )

    try:
        response = strategist_llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Objetivo: {state['user_objective']}")
        ]).content

        history_entry = {"agent": "strategist", "output": "Plano gerado com sucesso."}
        return {
            "business_plan": response,
            "history": state.get("history", []) + [history_entry]
        }
    except Exception as e:
        logger.error(f"❌ [Estrategista] Erro: {str(e)}")
        return {"errors": state.get("errors", []) + [f"Strategist Error: {str(e)}"]}