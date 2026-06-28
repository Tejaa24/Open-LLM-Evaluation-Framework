# Conclusions

## Key Findings

### Finding 1 — Instruction Tuning is Critical
- DistilGPT2 (82M, Base): 0% accuracy
- GPT2-Medium (345M, Base): 0% accuracy
- TinyLlama (1.1B, Instruction Tuned): 30% accuracy

Base models completely failed on math reasoning.
Only instruction-tuned model showed meaningful performance.

### Finding 2 — Model Size Alone is Not Enough
GPT2-Medium (345M) scored same as DistilGPT2 (82M) — both 0%.
This proves that model size without instruction tuning
does not improve reasoning ability.

### Finding 3 — Simple vs Multi-Step Reasoning
TinyLlama succeeded on simple single-step problems
but failed on multi-step reasoning questions.

## Answer to Research Question
> "Does instruction tuning impact reasoning accuracy
> in open-source LLMs of varying sizes?"

YES — instruction tuning is more important than model
size for mathematical reasoning tasks.

## Limitations
- Only 10 sample questions used
- CPU only evaluation — no GPU
- Limited to 3 models

## Future Work
- Evaluate Mistral-7B (instruction tuned, 7B)
- Add TruthfulQA for hallucination analysis
- GPU evaluation for larger models
- Increase sample size to 100 questions