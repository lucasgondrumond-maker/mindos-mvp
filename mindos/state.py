from typing import List, Optional
from typing_extensions import TypedDict

class MindosState(TypedDict):
    user_goal: str
    active_agents: List[str]
    strategic_plan: Optional[str]
    marketing_strategy: Optional[str]
    execution_status: str
    logs: List[str]
    errors: List[str]
