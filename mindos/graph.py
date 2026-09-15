from langgraph.graph import StateGraph, START, END
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
from mindos.state import MindosState
from mindos.agents.orchestrator import orchestrator_node
from mindos.agents.strategist import strategist_node
from mindos.agents.marketing import marketing_node

def route_next(state: MindosState) -> str:
    next_agent = state.get("next_agent")
    if next_agent == "strategist":
        return "strategist"
    elif next_agent == "marketing":
        return "marketing"
    return END

def create_mindos_graph():
    builder = StateGraph(MindosState)

    builder.add_node("orchestrator", orchestrator_node)
    builder.add_node("strategist", strategist_node)
    builder.add_node("marketing", marketing_node)

    builder.add_edge(START, "orchestrator")

    builder.add_conditional_edges(
        "orchestrator",
        route_next,
        {
            "strategist": "strategist",
            "marketing": "marketing",
            END: END
        }
    )

    builder.add_edge("strategist", "orchestrator")
    builder.add_edge("marketing", "orchestrator")

    return builder.compile()

mindos_graph = create_mindos_graph()
