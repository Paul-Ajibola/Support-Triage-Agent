"""
routing.py

conditional routing logic ussed by the graph to decide the next node
based on state. Currently placed after the injection guardrail: flagged
tickets skip the normal pipeline and go straight to human escalation.
"""


from agent.state import AgentState


def route_after_guardrail(state: AgentState) -> str:
    return "human_escalation" if state.get("is_flagged") else "intent_routing"


