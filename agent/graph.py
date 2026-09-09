from langgraph.graph import StateGraph, END
from typing import TypedDict



class AgentState(TypedDict):
    ticket_id: str
    body: str
    output: str


def stub_node(state: AgentState) -> AgentState:
    state["output"] = f"processed ticket {state['ticket_id']}"
    return state


builder = StateGraph(AgentState)
builder.add_node("stub", stub_node)
builder.set_entry_point("stub")
builder.add_edge("stub", END)

graph = builder.compile()

