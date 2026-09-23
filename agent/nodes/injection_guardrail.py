"""
Injection_guardrail.py

Node: the first step in the pipeline. Screens the raw ticket body for
prompt-injection attempts before any other node processes it. Flagged
tickets are marked in state and routed to human escalation
"""

from agent.state import AgentState
from agent.security.guardrail import scan_for_injection


def injection_guardrail(state: AgentState) -> AgentState:
    result = scan_for_injection(state["body"])
    state["is_flagged"] = result["is_injection"]
    state["flag_reason"] = result["reason"] if result["is_injection"] else None
    return state