from src.models.model_runner import generate_answer

print("Testing Phi-2...")

answer = generate_answer("What is 10 + 5?")

print(answer)