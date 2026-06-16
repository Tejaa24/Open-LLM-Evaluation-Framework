from transformers import pipeline

print("Loading model...")

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

response = generator(
    "Machine learning is",
    max_new_tokens=50,
    do_sample=True
)

print("\nGenerated Output:\n")
print(response[0]["generated_text"])