# import the agent state schema
from agent.state import AgentState


def context_enrichment(state: AgentState) -> AgentState:
    """decides which tools are relevant based on the classification"""
    tools = ["ticket_lookup"]    # always check historical tickets

    if state["category"] in ("integration", "auth"):
        tools.append("sandbox_runner")   # bug reproduction likely relevant

    tools.append("account_context_db")     # always pull acount context

    state["tools_in_call"] = tools
    return state