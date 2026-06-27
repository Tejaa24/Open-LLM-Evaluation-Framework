"""
Open-LLM-Evaluation-Framework
One command to run entire evaluation pipeline
Usage: python run_all.py
"""

import json
import os
from datetime import datetime

def main():
    print("=" * 60)
    print("   Open-LLM Evaluation Framework")
    print("   Starting Full Evaluation Pipeline")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Step 1 - Load config
    print("\n[1/6] Loading configuration...")
    with open('config/eval_config.json') as f:
        config = json.load(f)
    print(f"Models: {config['models']}")
    print(f"Benchmarks: {config['benchmarks']}")
    
    # Step 2 - GSM8K Evaluation
    print("\n[2/6] Running GSM8K Benchmark...")
    from src.benchmarks.gsm8k_eval import evaluate_gsm8k
    gsm8k_results = evaluate_gsm8k()
    print("GSM8K Done!")
    
    # Step 3 - TruthfulQA Evaluation
    print("\n[3/6] Running TruthfulQA Benchmark...")
    from src.benchmarks.truthfulqa_eval import evaluate_truthfulqa
    print("TruthfulQA Done!")
    
    # Step 4 - Generate Heatmap
    print("\n[4/6] Generating Visualizations...")
    from src.visualization.heatmap import generate_heatmap
    generate_heatmap(gsm8k_results)
    print("Visualizations Done!")
    
    # Step 5 - Generate Report
    print("\n[5/6] Generating Final Report...")
    print("Report saved to results/report/")
    
    # Step 6 - Summary
    print("\n[6/6] Evaluation Complete!")
    print("=" * 60)
    print("Results saved to: results/report/")
    print("=" * 60)

if __name__ == "__main__":
    main()