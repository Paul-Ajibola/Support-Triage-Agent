from agent.graph import graph


result = graph.invoke({
    "ticket_id": "T-2001",
    "body": "User can't log in after password reset, getting 401 error.",
    "category": None,
    "urgency": None,
    "tools_to_call": None,
    "tools_results": [],
    "safety_flags": {},
    "safety_flags": [],
    "draft_response": None,
})


print(result)

