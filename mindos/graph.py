from langgraph.graph import StateGraph, END
from mindos.state import AgentState
from mindos.agents.orchestrator import orchestrator_node

def create_mindos_graph():
    workflow = StateGraph(AgentState)

    # Adiciona o nó principal
    workflow.add_node("orchestrator", orchestrator_node)

    # Define a entrada e saída do fluxo
    workflow.set_entry_point("orchestrator")
    workflow.add_edge("orchestrator", END)

    return workflow.compile()
