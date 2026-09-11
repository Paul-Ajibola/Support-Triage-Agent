"""
draft_generation.py

Node: produces a draft resolution using tool_results — references a
similar past ticket if ticket_lookup found one, otherwise recommends
manual review. Final node before END.
"""

# import libraries
from agent.state import AgentState

def draft_generation(state: AgentState) -> AgentState:
    similar = state["tool_results"].get("ticket_lookup", [])
    if similar:
        suggestion = f"Similar past ticket {similar[0]['ticket_id']} was resolved by: {similar[0]['resolution']}"
    else:
        suggestion = "No similar past tickets found - recommend manual review."
    
    state["draft_response"] = (
        f"[category={state['category']}, urgency={state['urgency']}] {suggestion}"
    )
    return state

    