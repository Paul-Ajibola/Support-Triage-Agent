"""
context_enrichment.py

Node: decides which tools are relevant for this ticket based on its
category. Always includes ticket_lookup and account_context_db; adds
sandbox_runner for auth/integration tickets. Sets tools_to_call.
"""

# import the agent state schema
from agent.state import AgentState


def context_enrichment(state: AgentState) -> AgentState:
    """decides which tools are relevant based on the classification
    by the previous node--the context enrichment node"""
    tools = ["ticket_lookup"]    # always check historical tickets

    if state["category"] in ("integration", "auth"):
        tools.append("sandbox_runner")   # bug reproduction likely relevant

    tools.append("account_context_db")     # always pull acount context

    state["tools_to_call"] = tools
    return state