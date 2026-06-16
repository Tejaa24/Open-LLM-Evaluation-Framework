from transformers import pipeline

print("Loading DistilGPT2...")

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

def generate_answer(prompt):
    result = generator(
        prompt,
        max_new_tokens=30,
        do_sample=True
    )

    return result[0]["generated_text"]