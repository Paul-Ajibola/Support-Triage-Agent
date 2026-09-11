from agent.state import AgentState

def draft_generation(state: AgentState) -> AgentState:
    similar = state["tool_results"].get("ticket_lookup", [])
    if similar:
        suggestion = f"Similar past ticket {similar[0]['ticket_id']} was resolved by: {similar[0]['resolution']}"
    else:
        suggestion = "No similar past tickets found - recommend manual review."
    
    state["draft response"] = (
        f"[category={state['category']}, urgency={state['urgency']}] {suggestion}"
    )
    return state

    