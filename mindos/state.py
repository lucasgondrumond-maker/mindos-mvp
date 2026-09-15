from typing import TypedDict, List, Annotated
import operator

class AgentState(TypedDict):
    objective: str
    response: str
    messages: List[str]
