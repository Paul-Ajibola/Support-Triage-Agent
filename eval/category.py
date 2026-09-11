"""
Defines the fixed category and urgency labels used for ticket
classification, shared by my baseline and fine-tuned models
so that both are scored against the same naming conventions
"""


CATEGORIES = [
    "auth",
    "billing",
    "integration",
    "bug_report",
    "feature_request",
    "account_management",
    "performance",
    "general"
]


URGENCY_LEVELS = ["low", "normal", "high", "critical"]