from agent.state import AgentState
from tools.ticket_lookup import ticket_lookup
from tools.sandbox_runner import sandbox_runner
from tools.account_context_db import account_context_db


def tool_execution(state: AgentState) -> AgentState:
    results = {}

    if "ticket_lookup" in state["tools_to_call"]:
        results["ticket_lookup"] = ticket_lookup(state["body"])

    if "sandbox_runner" in state["tools_to_call"]:
        results["sandbox_runner"] = sandbox_runner("print('reproduction stub')")

    if "account_context_db" in state["tools_to_call"]:
        # placeholder account_id until real ticket -> account mapping exists
        results["account_context_db"] = account_context_db("ACC-001")

    
    state["tool_results"] = results
    return state

    
