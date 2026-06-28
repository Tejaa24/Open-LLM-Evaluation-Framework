from transformers import pipeline

print("Loading GPT2-Medium...")

generator = pipeline(
    "text-generation",
    model="gpt2-medium"
)

print("GPT2-Medium Loaded Successfully")

def generate_answer(question):
    prompt = f"Question: {question}\nAnswer:"
    result = generator(
        prompt,
        max_new_tokens=30,
        do_sample=False,
        pad_token_id=50256
    )
    generated = result[0]["generated_text"]
    answer_part = generated.split("Answer:")[-1].strip()
    return answer_part