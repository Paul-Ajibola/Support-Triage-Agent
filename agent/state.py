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
    turn_count: int
    conversation_history: List[str]
    is_flagged: bool
    flag_reason: Optional[str]
<<<<<<< HEAD
=======

>>>>>>> e63ef1d9fe61735c17d6a79f924785a2707a1644
    

    
    


