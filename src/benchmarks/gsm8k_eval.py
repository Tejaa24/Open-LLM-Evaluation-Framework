"""
GSM8K Benchmark Evaluation
Evaluates DistilGPT2, TinyLlama, Phi-2 on math reasoning
"""
import csv
import re
import os

sample_questions = [
    {"question": "John has 5 apples and buys 3 more. How many apples does he have?", "answer": 8},
    {"question": "A box contains 10 balls. 2 are removed. How many remain?", "answer": 8},
    {"question": "Sara has 12 candies and gives 4 to her friend. How many does she have?", "answer": 8},
    {"question": "A farmer has 7 cows and buys 5 more. How many cows does he have?", "answer": 12},
    {"question": "Tom has 20 stickers and gives away 8. How many remain?", "answer": 12},
    {"question": "A shop has 15 shirts. 6 are sold. How many are left?", "answer": 9},
    {"question": "There are 3 baskets with 4 apples each. How many apples total?", "answer": 12},
    {"question": "A train has 50 seats. 23 are occupied. How many are empty?", "answer": 27},
    {"question": "Maya has 9 books and buys 6 more. How many books does she have?", "answer": 15},
    {"question": "A class has 30 students. 11 are absent. How many are present?", "answer": 19},
]

def extract_number(text):
    if not text:
        return None
    numbers = re.findall(r'\b\d+\.?\d*\b', str(text))
    if numbers:
        return float(numbers[-1])
    return None

def check_answer(model_output, expected_answer, tolerance=0.5):
    extracted = extract_number(model_output)
    if extracted is None:
        return False
    return abs(extracted - float(expected_answer)) <= tolerance

def evaluate_model(model_name, generate_fn):
    print(f"\n{'='*50}")
    print(f"Evaluating: {model_name}")
    print(f"{'='*50}")

    correct = 0
    results = []

    for i, item in enumerate(sample_questions):
        question = item["question"]
        expected = item["answer"]

        print(f"\n[{i+1}/{len(sample_questions)}] {question}")

        try:
            model_output = generate_fn(question)
            extracted_num = extract_number(model_output)
            is_correct = check_answer(model_output, expected)

            if is_correct:
                correct += 1

            print(f"Expected: {expected}")
            print(f"Extracted: {extracted_num}")
            print(f"Correct: {is_correct}")

            results.append({
                "model": model_name,
                "question": question,
                "expected": expected,
                "model_output": model_output[:100],
                "extracted_number": extracted_num,
                "correct": is_correct
            })

        except Exception as e:
            print(f"Error: {e}")
            results.append({
                "model": model_name,
                "question": question,
                "expected": expected,
                "model_output": f"ERROR: {e}",
                "extracted_number": None,
                "correct": False
            })

    accuracy = correct / len(sample_questions)

    print(f"\n--- {model_name} Results ---")
    print(f"Correct: {correct}/{len(sample_questions)}")
    print(f"Accuracy: {accuracy*100:.1f}%")

    return accuracy, results

def save_results(all_results, filename="results/report/gsm8k_results_summary.csv"):
    os.makedirs("results/report", exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "model", "question", "expected",
            "model_output", "extracted_number", "correct"
        ])
        writer.writeheader()
        writer.writerows(all_results)
    print(f"\nResults saved to {filename}")

def run_gsm8k_evaluation():
    all_results = []
    model_accuracies = {}

    # Model 1 - DistilGPT2
    try:
        from src.models.model_runner import generate_answer as distilgpt2_fn
        acc, results = evaluate_model("DistilGPT2", distilgpt2_fn)
        model_accuracies["DistilGPT2"] = round(acc * 100, 1)
        all_results.extend(results)
    except Exception as e:
        print(f"DistilGPT2 Error: {e}")
        model_accuracies["DistilGPT2"] = 0.0

    # Model 2 - TinyLlama
    try:
        from src.models.model_runner_tinyllama import generate_answer as tinyllama_fn
        acc, results = evaluate_model("TinyLlama", tinyllama_fn)
        model_accuracies["TinyLlama"] = round(acc * 100, 1)
        all_results.extend(results)
    except Exception as e:
        print(f"TinyLlama Error: {e}")
        model_accuracies["TinyLlama"] = 0.0

    # Model 3 - Phi-2
    try:
        from src.models.model_runner_gemma import generate_answer as phi2_fn
        acc, results = evaluate_model("Phi-2", phi2_fn)
        model_accuracies["Phi-2"] = round(acc * 100, 1)
        all_results.extend(results)
    except Exception as e:
        print(f"Phi-2 Error: {e}")
        model_accuracies["Phi-2"] = 0.0

    save_results(all_results)

    print("\n" + "="*50)
    print("FINAL GSM8K RESULTS SUMMARY")
    print("="*50)
    for model, acc in model_accuracies.items():
        print(f"{model:15} : {acc}%")
    print("="*50)

    return model_accuracies

if __name__ == "__main__":
    run_gsm8k_evaluation()