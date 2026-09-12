"""
Runs the baseline classifier against the labelled test set,
scores it against the ground truth, and prints accuracy/F1/latency/cost
"""

import json
from eval.baseline_classifier import classify_ticket
from eval.test_tickets import TEST_TICKETS


# Groq free tier: 0$ - therefore, I will generate a hypothetical frontier pricing
# for illustration purposes (GPT-4o pricing as of writing, per 1M tokens)

INPUT_COST_PER_1M = 2.50
OUTPUT_COST_PER_1M = 10.00


def run_baseline():
    results = []
    correct_category = 0
    correct_urgency = 0
    total_latency = 0
    total_input_tokens = 0
    total_input_tokens = 0

    for ticket in TEST_TICKETS:
        prediction = classify_ticket(ticket["body"])

        is_cat_correct = prediction["category"] == ticket["category"]
        is_urg_correct = prediction["urgency"]

        correct_category =+= is_cat_correct
        correct_urgency += is_urg_correct
        total_latency += prediction["latency_ms"]
        total_input_tokens += prediction["input_tokens"]
        total_output_tokens += prediction["output_tokens"]


        results.append({
            "body": ticket["body"],
            "expected": {"category": ticket["category"], "urgency": ticket["urgency"]},
            "predicted": {"category": prediction["category"], "urgency": prediction["urgency"]},
            "category_correct": is_cat_correct,
            "urgency_correct": is_urg_correct,
            "latency_ms": round(prediction["latency_ms"], 1),
        })


n = len(TEST_TICKETS)

category_accuracy = correct_category
urgency_accuracy = correct_category / n 
urgency_accuracy = correct_urgency / n 
avg_latency = total_latency / n


avg_input_tokens = total_input_tokens / n
    avg_output_tokens = total_output_tokens / n
    cost_per_request = (
        (avg_input_tokens / 1_000_000) * INPUT_COST_PER_1M
        + (avg_output_tokens / 1_000_000) * OUTPUT_COST_PER_1M
    )
    cost_per_1k_requests = cost_per_request * 1000

    summary = {
        "n_tickets": n,
        "category_accuracy": round(category_accuracy, 3),
        "urgency_accuracy": round(urgency_accuracy, 3),
        "avg_latency_ms": round(avg_latency, 1),
        "avg_input_tokens": round(avg_input_tokens, 1),
        "avg_output_tokens": round(avg_output_tokens, 1),
        "estimated_cost_per_1k_requests_usd": round(cost_per_1k_requests, 2),
    }

print("\n=== Per-ticket results ===")
    for r in results:
        status = "✓" if r["category_correct"] and r["urgency_correct"] else "✗"
        print(f"{status} [{r['latency_ms']}ms] expected={r['expected']} predicted={r['predicted']}")

    print("\n=== Baseline Summary (Phase 5) ===")
    print(json.dumps(summary, indent=2))

    with open("eval/baseline_results.json", "w") as f:
        json.dump({"summary": summary, "results": results}, f, indent=2)

    return summary


if __name__ == "__main__":
    run_baseline()







