from transformers import pipeline

print("Loading Phi-2...")

generator = pipeline(
    "text-generation",
    model="microsoft/phi-2"
)

def generate_answer(prompt):

    result = generator(
        prompt,
        max_new_tokens=30,
        do_sample=False
    )

    return result[0]["generated_text"]