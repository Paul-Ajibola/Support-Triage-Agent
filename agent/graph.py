# import libraries
from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.state import AgentState
from agent.nodes.intent_routing import intent_routing
from agent.nodes.context_enrichment import context_enrichment
from agent.nodes.tool_execution import tool_execution
from agent.nodes.safety_verification import safety_verification
from agent.nodes.draft_generation import draft_generation



builder = StateGraph(AgentState)

builder.add_node("intent_routing", intent_routing)
builder.add_node("context_enrichment", context_enrichment)
builder.add_node("tool_execution", tool_execution)
builder.add_node("safety_verification", safety_verification)
builder.add_node("draft_generation", draft_generation)


builder.set_entry_point("intent_routing")
builder.add_edge("intent_routing", "context_enrichment")
builder.add_edge("context_enrichment", "tool_execution")
builder.add_edge("tool_execution", "safety_verification")
builder.add_edge("safety_verification", "draft_generation")
builder.add_edge("draft_generation", END)


graph = builder.compile()

