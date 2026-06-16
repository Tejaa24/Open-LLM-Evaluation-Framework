"""
GSM8K Benchmark Evaluation
"""

import csv
from src.models.model_runner import generate_answer

sample_questions = [
    {
        "question": "John has 5 apples and buys 3 more. How many apples does he have?",
        "answer": 8
    },
    {
        "question": "A box contains 10 balls. 2 are removed. How many remain?",
        "answer": 8
    }
]

correct = 0
results = []

for item in sample_questions:
    question = item["question"]
    expected = item["answer"]

    print("\nQuestion:", question)

    # Generate answer using DistilGPT2
    user_answer = generate_answer(question)

    print("\nGenerated Answer:")
    print(user_answer)

    print("\nExpected Answer:")
    print(expected)

    # Simple correctness check
    is_correct = str(expected) in user_answer

    if is_correct:
        correct += 1

    results.append([
        question,
        user_answer,
        expected,
        is_correct
    ])

accuracy = correct / len(sample_questions)

with open(
    "results/report/gsm8k_mini_results.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "question",
        "generated_answer",
        "expected_answer",
        "correct"
    ])

    writer.writerows(results)

print("\n===================================")
print("Evaluation Complete")
print("Accuracy:", accuracy)
print("Results saved successfully")
print("===================================")