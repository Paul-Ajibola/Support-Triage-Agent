from typing import TypedDict, List, Optional


class AgentState(TypedDict):
    ticket_id: str
    body: str
    category: Optional[str]
    urgency: Optional[str]
    tools_to_call: List[str]
    tool_results: dict
    safety_flags: List[str]
    draft_response: Optional[str]


