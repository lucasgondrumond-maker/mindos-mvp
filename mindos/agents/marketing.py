from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from mindos.state import MindosState
from mindos.config import logger

marketing_llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

def marketing_node(state: MindosState):
    logger.info("📢 [Marketing] Desenvolvendo estratégia de GTM...")

    system_prompt = (
        "Você é o Especialista em Marketing do MINDOS. Crie uma estratégia de entrada no mercado "
        "(Go-To-Market) baseada EXCLUSIVAMENTE no Plano de Negócio fornecido.\n"
        "Inclua: Posicionamento de Marca, Canais de Aquisição e Exemplo de Copy de Lançamento."
    )

    prompt = (
        f"Objetivo do Usuário: {state['user_objective']}\n\n"
        f"Plano de Negócio: {state['business_plan']}"
    )

    try:
        response = marketing_llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=prompt)
        ]).content

        history_entry = {"agent": "marketing", "output": "Estratégia de marketing gerada."}
        return {
            "marketing_strategy": response,
            "history": state.get("history", []) + [history_entry]
        }
    except Exception as e:
        logger.error(f"❌ [Marketing] Erro: {str(e)}")
        return {"errors": state.get("errors", []) + [f"Marketing Error: {str(e)}"]}