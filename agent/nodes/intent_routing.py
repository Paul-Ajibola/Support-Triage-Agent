from agent.state import AgentState


def intent_routing(state: AgentState) -> AgentState:
    "Determines what is the intent of the ticket and classifies its urgency"
    body = state["body"].lower()

    if "login" in body or "password" in body or "auth" in body:
        category = "auth"
    elif "rate limit" in body or "billing" in body or "charge" in body:
        category = "billing"
    elif "webhook" in body or "intention" in body or "api" in body:
        category = "general"

    
    urgency = "high" if any(
        w in body for w in ["down", "broken", "urgent", "critical"]
        ) else "normal"

    # add the decision back into the state
    state["category"] = category
    state["urgency"] = urgency
    return state


