"""
graph.py

Defines and compiles the LangGraph state machine for the support triage
agent. Wires the node functions (intent_routing, context_enrichment,
tool_execution, safety_verification, draft_generation) into a linear
pipeline: a ticket comes in, gets classified, relevant tools are called,
outputs are sanity-checked, and a draft resolution is produced.
It has a redis-backed checkpointing for multi-turn conversations.

Flow:
    intent_routing -> context_enrichment -> tool_execution ->
    safety_verification -> draft_generation -> END

Requires: agent/state.py (AgentState schema), agent/nodes/* (node logic).
"""

# import libraries
from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.state import AgentState
from agent.nodes.intent_routing import intent_routing
from agent.nodes.context_enrichment import context_enrichment
from agent.nodes.tool_execution import tool_execution
from agent.nodes.safety_verification import safety_verification
from agent.nodes.draft_generation import draft_generation
from agent.checkpointing import get_checkpointer


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


checkpointer = get_checkpointer()
graph = builder.compile(checkpointer=checkpointer)

