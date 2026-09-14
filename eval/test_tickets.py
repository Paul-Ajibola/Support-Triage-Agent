"""
test_tickets.py

Labled ticket set used to evaluate classification models (baseline vs fine-tuned)
against a shared ground truth.

Curated sample evaluation set
"""

TEST_TICKETS = [
{"body": "User can't log in after password reset, getting 401 error.", "category": "auth", "urgency": "normal"},
{"body": "System is completely down, no one can access the app!", "category": "bug_report", "urgency": "critical"},
{"body": "Customer was charged twice for the same invoice.", "category": "billing", "urgency": "high"},
{"body": "Webhook stopped firing after we changed our endpoint URL", "category": "integration", "urgency": "normal"},
{"body": "Can you add dark mode to the dashboard?", "category": "feature_request", "urgency": "low"},
{"body": "I need to update the billing email on my account", "category": "account_management", "urgency": "low"},
{"body": "Dashboard takes over 30 seconds to load every time.", "category": "performance", "urgency": "high"},
{"body": "Just wanted to say thanks, everything's working great.", "category": "general", "urgency": "low"},
{"body": "API rate limit hit unexpectedly despite low usage.", "category": "integration", "urgency": "normal"},
{"body": "My account got locked out and I can't reset the password.", "category": "auth", "urgency": "high"},

 # --- auth ---
    {"body": "Two-factor authentication codes aren't arriving via SMS.", "category": "auth", "urgency": "high"},
    {"body": "I forgot my password and the reset email never showed up.", "category": "auth", "urgency": "normal"},
    {"body": "Someone else may have accessed my account without permission.", "category": "auth", "urgency": "critical"},

    # --- billing ---
    {"body": "My subscription renewed at the wrong price this month.", "category": "billing", "urgency": "normal"},
    {"body": "Can I get a copy of last year's invoices for tax purposes?", "category": "billing", "urgency": "low"},
    {"body": "Payment failed three times and now my account is suspended.", "category": "billing", "urgency": "critical"},

    # --- integration ---
    {"body": "Our Slack integration hasn't posted any updates in two days.", "category": "integration", "urgency": "high"},
    {"body": "Is there a way to connect this to our internal CRM via API?", "category": "integration", "urgency": "low"},
    {"body": "OAuth token keeps expiring every hour instead of every month.", "category": "integration", "urgency": "normal"},

    # --- bug_report ---
    {"body": "Clicking export crashes the whole browser tab.", "category": "bug_report", "urgency": "high"},
    {"body": "Search results show duplicate entries sometimes.", "category": "bug_report", "urgency": "normal"},
    {"body": "All uploaded files from last week have disappeared entirely.", "category": "bug_report", "urgency": "critical"},

    # --- feature_request ---
    {"body": "Would be great to have keyboard shortcuts for common actions.", "category": "feature_request", "urgency": "low"},
    {"body": "Any roadmap plans for a mobile app version?", "category": "feature_request", "urgency": "low"},

    # --- account_management ---
    {"body": "How do I add a new team member to our workspace?", "category": "account_management", "urgency": "normal"},
    {"body": "Please permanently delete my account and all associated data.", "category": "account_management", "urgency": "normal"},

    # --- performance ---
    {"body": "Reports have been timing out for the past hour, this is blocking our team.", "category": "performance", "urgency": "critical"},
    {"body": "Page load feels a little slower than usual lately.", "category": "performance", "urgency": "low"},

    # --- general ---
    {"body": "Do you have a status page I can check for outages?", "category": "general", "urgency": "low"},
    {"body": "Quick question, not urgent: where can I find your changelog?", "category": "general", "urgency": "low"},
]
]


