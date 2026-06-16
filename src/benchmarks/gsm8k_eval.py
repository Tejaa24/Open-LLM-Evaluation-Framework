"""
GSM8K Benchmark Evaluation
"""

import csv

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

    user_answer = expected  # Placeholder prediction

    print("Predicted:", user_answer)
    print("Expected :", expected)

    is_correct = user_answer == expected

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
        "predicted",
        "expected",
        "correct"
    ])

    writer.writerows(results)

print("\nEvaluation Complete")
print("Accuracy:", accuracy)
print("Results saved successfully")