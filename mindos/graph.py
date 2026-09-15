from langgraph.graph import StateGraph, START, END
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