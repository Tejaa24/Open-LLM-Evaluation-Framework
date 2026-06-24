from transformers import pipeline

print("Loading TinyLlama...")

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

def generate_answer(prompt):

    messages = f"""
<|system|>
You are a helpful AI assistant.
<|user|>
{prompt}
<|assistant|>
"""

    result = generator(
        messages,
        max_new_tokens=30,
        do_sample=False
    )

    return result[0]["generated_text"]