# Open LLM Evaluation Framework - Final Report

## Introduction
The Open LLM Evaluation Framework is a research-oriented 
project designed to evaluate the performance and reasoning 
capability of open-source Large Language Models (LLMs) 
using standardized benchmarks and evaluation metrics.

---

## Research Question
Does instruction tuning impact reasoning accuracy in 
open-source LLMs of varying sizes?

---

## Objectives
- Evaluate mathematical reasoning capabilities of open-source LLMs
- Compare base models vs instruction-tuned models
- Measure accuracy, consistency, and reliability
- Analyze failure patterns through error analysis
- Build a reproducible evaluation pipeline

---

## Models Evaluated

| Model | Parameters | Type |
|---|---|---|
| DistilGPT2 | 82M | Base Model |
| GPT2-Medium | 345M | Base Model |
| TinyLlama-1.1B-Chat | 1.1B | Instruction Tuned |

---

## Methodology
1. Dataset loading — GSM8K 10 sample questions
2. Model loading — HuggingFace Transformers
3. Answer generation — each model answers each question
4. Number extraction — regex based extraction from output
5. Accuracy calculation — extracted vs expected answer
6. Consistency check — same results across multiple runs
7. Error analysis — failure pattern identification
8. Visualization — charts and heatmaps generated
9. Report generation — CSV and markdown reports

---

## Benchmark Used

### GSM8K (Grade School Math 8K)
Mathematical reasoning benchmark with arithmetic 
word problems. Tests model ability to understand 
questions and compute correct numerical answers.

---

## Evaluation Metrics

| Metric | Description |
|---|---|
| Accuracy | Correct answers / Total questions |
| Consistency | Same output across multiple runs |
| Reliability | Overall dependability of responses |
| Hallucination Rate | Wrong/unsupported outputs |

---

## Experimental Results

### GSM8K Accuracy

| Model | Parameters | Type | Correct | Total | Accuracy |
|---|---|---|---|---|---|
| DistilGPT2 | 82M | Base | 0 | 10 | 0% |
| GPT2-Medium | 345M | Base | 0 | 10 | 0% |
| TinyLlama-1.1B | 1.1B | Instruction Tuned | 3 | 10 | 30% |

### Consistency Results

| Model | Run 1 | Run 2 | Run 3 | Consistent |
|---|---|---|---|---|
| DistilGPT2 | 0% | 0% | 0% | Yes ✅ |
| GPT2-Medium | 0% | 0% | 0% | Yes ✅ |
| TinyLlama | 30% | 30% | 30% | Yes ✅ |

---

## Error Analysis Summary

| Model | Primary Failure Pattern |
|---|---|
| DistilGPT2 | Extracts numbers from question instead of computing |
| GPT2-Medium | Same pattern — no mathematical reasoning ability |
| TinyLlama | Correct on simple addition, fails on subtraction/multiplication |

---

## Key Findings

### Finding 1 — Instruction Tuning is Critical
Base models (DistilGPT2, GPT2-Medium) scored 0% regardless
of size. Only instruction-tuned TinyLlama showed 30% accuracy.

### Finding 2 — Model Size Alone is Not Enough
GPT2-Medium (345M) = same as DistilGPT2 (82M) = 0%.
4x larger model showed zero improvement without instruction tuning.

### Finding 3 — Operation Type Matters
TinyLlama succeeded on simple addition but failed on
subtraction, multiplication, and multi-step problems.

---

## Generated Outputs
- `results/report/gsm8k_results_summary.csv`
- `results/report/accuracy_chart.png`
- `results/report/model_comparison.png`
- `results/report/hallucination_heatmap.png`
- `results/report/error_analysis.md`

---

## Observations
- Instruction tuning is more important than model size
- Base models have zero mathematical reasoning ability
- TinyLlama shows promising results for a 1.1B model
- Consistent results across multiple evaluation runs
- Modular framework supports easy benchmark expansion

---

## Future Work
- Add Mistral-7B evaluation (instruction tuned, 7B)
- Integrate TruthfulQA benchmark
- Integrate HellaSwag benchmark
- GPU support for larger models
- Increase sample size to 100+ questions
- Build interactive dashboard

---

## Conclusion
This study demonstrates that instruction tuning is the 
most critical factor for mathematical reasoning in 
open-source LLMs — more important than model size alone.

TinyLlama-1.1B-Chat achieved 30% accuracy on GSM8K while 
base models (DistilGPT2 82M, GPT2-Medium 345M) scored 0%, 
clearly answering our research question:

> Instruction tuning significantly impacts reasoning accuracy,
> regardless of model size.

---

## References
- [GSM8K Paper](https://arxiv.org/abs/2110.14168)
- [TruthfulQA Paper](https://arxiv.org/abs/2109.07958)
- [HuggingFace Transformers](https://github.com/huggingface/transformers)
- [TinyLlama](https://github.com/jzhang38/TinyLlama)

---

## Author
**Adi Lakshamma Bonam**
Computer Science Undergraduate
GitHub: https://github.com/Tejaa24