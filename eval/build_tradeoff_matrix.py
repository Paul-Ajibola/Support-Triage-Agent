"""
Combines baseline and finetuned results into the
before and after tradeoff table
"""
import json


with open("eval/results/baseline_results.json") as f:
    baseline = json.load(f)["summary"]

with open("eval/results/finetuned_results.json") as f:
    finetuned = json.load(f)["summary"]


print(f"{'Metric':<30}{'Baseline (Prompted)':<25}{'Fine-Tuned (LoRA)':<25}")
print("-" * 80)
print(f"{'Category Accuracy':<30}{baseline['category_accuracy']:<25}{finetuned['category_accuracy']:<25}")
print(f"{'Urgency Accuracy':<30}{baseline['urgency_accuracy']:<25}{finetuned['urgency_accuracy']:<25}")
print(f"{'Avg Latency (ms)':<30}{baseline['avg_latency_ms']:<25}{finetuned['average_latency_ms']:<25}")
print(f"{'Cost / 1k requests ($)':<30}{baseline['estimated_cost_per_1k_requests_usd']:<25}{finetuned['estimated_cost_per_1k_request_usd']:<25}")


savings_pct = (
    (baseline['estimated_cost_per_1k_requests_usd'] - finetuned['estimated_cost_per_1k_request_usd'])
    / baseline['estimated_cost_per_1k_requests_usd'] * 100
)


print(f"\nCost savings: {savings_pct:.1f}%")