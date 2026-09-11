"""
manual_test_multiturn.py

Manual test proving checkpointing works: sends an initial ticket, then
a follow-up the same thread_id, and confirms the second turn can see
state (conversation_history, category, etc.) from the first turn.
"""

from agent.graph import graph

config = {"configurable": {"thread_id": "ticket_-T-3001"}}

# first turn - initial ticket
turn1 = graph.invoke({
    "ticket_id": "T-3001",
    "body": "Login fails after password reset",
    "category":  None,
    "urgency": None,
    "tools_to_call": [],
    "tool_results": {},
    "safety_flags": [],
    "draft_response": None,
    "turn_count": 0,
    "conversation_history": [],
}, config=config)

print("----Turn 1 -----")
print(turn1)


# turn 2 - follow-up, same thread_id, minimal new input
turn2 = graph.invoke({
    "body": "The fix failed, what's next?",
}, config=config)


print("\n--- Turn 2 ---")
print(turn2)
print("\nConversation history so far:", turn2["conversation_history"])
print("Turn count:", turn2["turn_count"])


# turn 3 - follow-up, same thread_id, minimal new input
turn3 = graph.invoke({
    "body": "This also failed, what is the next thing to do?",
}, config=config)


print("\n--- Turn 3 ---")
print(turn3)
print("\nConversation history so far:", turn3["conversation_history"])
print("Turn count:", turn3["turn_count"])
