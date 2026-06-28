"""
DistilGPT2 Model Runner
"""
from transformers import pipeline

print("Loading DistilGPT2...")
generator = pipeline("text-generation", model="distilgpt2")
print("Model Loaded Successfully")

def generate_answer(question):
    print("Generating answer...")
    prompt = f"Question: {question}\nAnswer:"
    output = generator(
        prompt,
        max_new_tokens=50,
        do_sample=False,
        temperature=1.0
    )
    generated = output[0]["generated_text"]
    answer_part = generated.split("Answer:")[-1].strip()
    print("Generation Complete")
    return answer_part