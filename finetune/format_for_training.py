# finetune/format_for_training.py
"""
format_for_training.py

Converts raw labeled tickets into instruction-tuning format (prompt +
expected JSON completion) for LoRA fine-tuning with Unsloth.
"""

import json

SYSTEM_PROMPT = """You are a support ticket classifier.
Classify the ticket into exactly one category from: ['auth', 'billing', 'integration', 'bug_report', 'feature_request', 'account_management', 'performance', 'general']
And exactly one urgency level from: ['low', 'normal', 'high', 'critical']
Respond ONLY with JSON in this exact format, no other text:
{"category": "...", "urgency": "..."}"""


def format_dataset(input_path: str, output_path: str):
    with open(input_path) as f_in, open(output_path, "w") as f_out:
        for line in f_in:
            # load the JSON line and convert to python object
            row = json.loads(line)
            # convert string to json
            completion = json.dumps({"category": row["category"], "urgency": row["urgency"]})
            formatted = {
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": row["body"]},
                    {"role": "assistant", "content": completion},
                ]
            }
            f_out.write(json.dumps(formatted) + "\n")


if __name__ == "__main__":
    format_dataset("finetune/training_data.jsonl", "finetune/training_data_formatted.jsonl")
    print("Formatted training data -> finetune/training_data_formatted.jsonl")

    