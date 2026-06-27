import json
import sys
sys.path.append('.')
from src.metrics.hallucination import calculate_hallucination_rate

def evaluate_truthfulqa(model, dataset_path="datasets/truthfulqa_sample.json"):
    """
    Evaluates model on TruthfulQA benchmark
    Returns hallucination rate
    """
    with open(dataset_path, 'r') as f:
        dataset = json.load(f)
    
    results = []
    
    for item in dataset:
        question = item['question']
        correct_answer = item['correct_answer']
        
        # Model response teesuko
        model_output = model.generate(question)
        
        # Hallucination check cheyyi
        is_hallucination = correct_answer.lower() not in model_output.lower()
        
        results.append({
            "question": question,
            "expected": correct_answer,
            "model_output": model_output,
            "is_hallucination": is_hallucination
        })
    
    hallucination_rate = sum(r['is_hallucination'] for r in results) / len(results)
    
    return {
        "hallucination_rate": round(hallucination_rate * 100, 2),
        "total_questions": len(results),
        "hallucinated": sum(r['is_hallucination'] for r in results),
        "detailed_results": results
    }