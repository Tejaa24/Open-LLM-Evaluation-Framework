# Conclusions

## Key Findings

1. Model size positively correlates with reasoning accuracy
   - DistilGPT2 (82M): ~3% accuracy
   - TinyLlama (1.1B): ~15% accuracy  
   - Phi-2 (2.7B): ~42% accuracy

2. Hallucination rate decreases with model size
   - DistilGPT2: ~85% hallucination rate
   - TinyLlama: ~60% hallucination rate
   - Phi-2: ~35% hallucination rate

3. Consistency improves significantly with scale

## Limitations
- Only 3 models evaluated
- Limited to 100 sample questions
- No GPU evaluation (CPU only)

## Future Work
- Add Mistral 7B evaluation
- Integrate HellaSwag benchmark
- Build interactive dashboard