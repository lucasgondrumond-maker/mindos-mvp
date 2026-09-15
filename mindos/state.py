from typing import TypedDict, List

class MindosState(TypedDict):
    objective: str
    response: str
    messages: List[str]
