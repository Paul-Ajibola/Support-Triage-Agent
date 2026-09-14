"""
generate synthetic labelled ticket data for LoRA fine-tuning,
using templated variations per category so we get volume without
needing real customer data. Output is separate from and never 
overlaps with eval/test_tickets.py (the held-out evaluation set).
"""


import json
import random
from eval.category import CATEGORIES, URGENCY_LEVELS


TEMPLATES = {
    "auth": [
        "Can't log in after {event}, getting {error} error.",
        "My password reset link {problem}.",
        "Two-factor authentication {problem} on my account.",
    ],
    "billing": [
        "I was charged {amount} but my plan should cost {expected}.",
        "Invoice for {month} looks incorrect.",
        "Need to update my payment method, current card {problem}.",
    ],
    "integration": [
        "Webhook stopped firing after {event}.",
        "API returns {error} when calling {endpoint}.",
        "Our Zapier integration {problem} since yesterday.",
    ],
    "bug_report": [
        "{feature} crashes every time I click {button}.",
        "Getting a blank screen when I try to {action}.",
        "{feature} is completely broken after the last update.",
    ],
    "feature_request": [
        "Would love to see {feature} added to the product.",
        "Any plans to support {feature}?",
        "Please consider adding {feature}, would help a lot.",
    ],
    "account_management": [
        "Need to change the email on my account.",
        "How do I transfer ownership of the account to a teammate?",
        "Please deactivate my account.",
    ],
    "performance": [
        "{feature} takes over {seconds} seconds to load.",
        "App has been really slow since {event}.",
        "Dashboard {problem} under normal usage.",
    ],
    "general": [
        "Just wanted to say thanks, {feature} works great.",
        "Quick question about how {feature} works.",
        "Is there documentation for {feature}?",
    ],
}


FILLERS = {
    "event": ["a password reset", "the last update", "changing my email", "enabling 2FA"],
    "error": ["401", "403", "500", "timeout"],
    "problem": ["isn't working", "keeps failing", "times out", "is broken"],
    "amount": ["$49", "$99", "$199"],
    "expected": ["$29", "$79", "$149"],
    "month": ["March", "April", "May"],
    "endpoint": ["/api/v1/users", "/api/v1/tickets", "/api/v1/webhooks"],
    "feature": ["the dashboard", "dark mode", "SSO login", "bulk export", "the search bar"],
    "button": ["save", "submit", "export"],
    "action": ["export a report", "load the dashboard", "save changes"],
    "seconds": ["15", "20", "30"],
}




def fill(template: str) -> str:
    for key, options in FILLERS.items():
        if f"{{{key}}}" in template:
            template = template.replace(f"{{{key}}}", random.choice(options))
    return template



def generate(n_per_category: int = 40):
    data = []
    for category, templates in TEMPLATES.items():
        for _ in range(n_per_category):
            template = random.choice(templates)
            body = fill(template)
            urgency = random.choices(
                URGENCY_LEVELS, weights=[0.2, 0.4, 0.3, 0.1]
            )[0]
            data.append({"body": body, "category": category, "urgency": urgency})
    random.shuffle(data)
    return data


if __name__ == "__main__":
    dataset = generate(n_per_category=40)
    with open("finetune/training_data.jsonl", "w") as f:
        for row in dataset:
            f.write(json.dumps(row) + "\n")
    print(f"Generated {len(dataset)} training examples -> finetune/training_data.jsonl")

