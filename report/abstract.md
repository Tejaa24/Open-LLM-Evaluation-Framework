# Abstract

This study presents an open-source evaluation framework 
for benchmarking Large Language Models (LLMs) on reasoning 
and factuality tasks.

## Research Question
Does increasing model size in open-source LLMs lead to 
improved reasoning accuracy and reduced hallucination rates?

## Models Evaluated
- DistilGPT2 (82M parameters)
- TinyLlama-1.1B (1.1B parameters)  
- Phi-2 (2.7B parameters)

## Benchmarks Used
- GSM8K (Mathematical Reasoning)
- TruthfulQA (Factual Accuracy)

## Key Finding
Phi-2 achieved 14x higher accuracy than DistilGPT2 on GSM8K,
confirming positive correlation between model size and 
reasoning capability.