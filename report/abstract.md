# Abstract

## Project Title
Open-LLM Evaluation Framework: Benchmarking Open-Source 
Large Language Models on Mathematical Reasoning Tasks

## Research Question
Does instruction tuning impact reasoning accuracy in 
open-source LLMs of varying sizes?

## Objective
This study evaluates and compares three open-source Large 
Language Models on the GSM8K mathematical reasoning benchmark 
to analyze the impact of instruction tuning on model performance.

## Models Evaluated
- DistilGPT2 (82M parameters) — Base Model
- GPT2-Medium (345M parameters) — Base Model
- TinyLlama-1.1B-Chat (1.1B parameters) — Instruction Tuned

## Benchmark Used
- GSM8K (Grade School Math 8K) — Mathematical Reasoning

## Key Results
| Model | Accuracy |
|---|---|
| DistilGPT2 | 0% |
| GPT2-Medium | 0% |
| TinyLlama-1.1B | 30% |

## Key Finding
Instruction-tuned models significantly outperform base models 
on mathematical reasoning tasks. TinyLlama achieved 30% accuracy 
while base GPT2 variants scored 0%, confirming that instruction 
tuning is more critical than model size for reasoning ability.

## Technologies Used
Python, HuggingFace Transformers, PyTorch, Pandas, Matplotlib

## Author
Adi Lakshamma Bonam — Computer Science Undergraduate