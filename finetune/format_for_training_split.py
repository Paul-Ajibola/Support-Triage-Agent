"""
Converts raw labeled tickets into TWO separate instruction-tuning
examples per ticket: one asking only for category, one asking only
for urgency. This gives urgency its own dedicated training signal,
rather than being jointly predicted alongside category in one output
(which earlier experiments suggested was underweighting urgency).
"""


import json

CATEGORY_SYSTEM_PROMPT = """You are a support ticket classifier
Classify the ticket into exactly one category from: ["auth", "billing", "integration", "bug_report",
"feature_request", "account_management", "performance", "general"]
Respond ONLY with JSON in this exact format, no other text:
{"category": "..."}
"""


URGENCY_SYSTEM_PROMPT = """
You are a support ticket urgency classifier.
Classify the ticket's urgency into exactly one level from: 
["low", "normal", "high", "critical"]
Respond ONLY with JSON in this exact format, no other text:
{"urgency": "..."}
"""


def format_dataset(input_path: str, output_path: str):
    with open(input_path) as f_in, open(output_path, "w") as f_out:
        for line in f_in:
            row = json.loads(line)

            # Task 1: category-only example
            category_example = {
                "messages": [
                    {"role": "system", "content": CATEGORY_SYSTEM_PROMPT},
                    {"role": "user", "content": row["body"]},
                    {"role": "assistant", "content": json.dumps({"category": row["category"]})},
                ]
            }
            f_out.write(json.dumps(category_example) + "\n")

            # Task 2: urgency-only example
            urgency_example = {
                "messages": [
                    {"role": "system", "content": URGENCY_SYSTEM_PROMPT},
                    {"role": "user", "content": row["body"]},
                    {"role": "assistant", "content": json.dumps({"urgency": row["urgency"]})},
                ]
            }
            f_out.write(json.dumps(urgency_example) + "\n")


if __name__ == "__main__":
    format_dataset("finetune/training_data.jsonl", "finetune/training_data_split_formatted.jsonl")
    print("Formatted split training data -> finetune/training_data_split_formatted.jsonl")


