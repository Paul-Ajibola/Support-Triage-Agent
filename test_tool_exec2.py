from agent.nodes.tool_execution import tool_execution

fake_state = {
    'ticket_id': 'T-TEST',
    'body': "User can't log in after password reset, getting 401 error.",
    'category': 'auth',
    'urgency': 'normal',
    'tools_to_call': ['ticket_lookup', 'sandbox_runner', 'account_context_db'],
    'tool_results': {},
    'safety_flags': [],
    'draft_response': None,
}

result = tool_execution(fake_state)
print(result)
