"""
test_tickets.py

Labled ticket set used to evaluate classification models (baseline vs fine-tuned)
against a shared ground truth.
"""

TEST_TICKETS = [
{"body": "User can't log in after password reset, getting 401 error.", "category": "auth", "urgency": "normal"},
{"body": "System is completely down, no one can access the app!", "category": "bug", "urgency": "critical"},
{"body": "Customer was charged twice for the same invoice.", "category": "billing", "urgency": "high"},
{"body": "Webhook stopped firing after we changed our endpoint URL", "category": "integration", "urgency": "normal"},
{"body": "Can you add dark mode to the dashboard?", "category": "feature_request", "urgency": "low"},
{"body": "I need to update the billing email on my account", "category": "account_management", "urgency": "low"},
{"body": "Dashboard takes over 30 seconds to load every time.", "category": "performance", "urgency": "high"},
{"body": "Just wanted to say thanks, everything's working great.", "category": "general", "urgency": "low"},
{"body": "API rate limit hit unexpectedly despite low usage.", "category": "integration", "urgency": "normal"},
{"body": "My account got locked out and I can't reset the password.", "category": "auth", "urgency": "high"}
]


