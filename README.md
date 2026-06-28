# Open-LLM-Evaluation-Framework

A research-oriented framework for evaluating open-source Large Language Models (LLMs) using benchmark datasets and multiple evaluation metrics.

---

## 🔬 Research Question

Does instruction tuning impact reasoning accuracy in open-source LLMs of varying sizes?

---

## 📊 Key Findings

| Model | Parameters | Type | GSM8K Accuracy |
|---|---|---|---|
| DistilGPT2 | 82M | Base Model | 0% |
| GPT2-Medium | 345M | Base Model | 0% |
| TinyLlama-1.1B | 1.1B | Instruction Tuned | 30% |

> Instruction-tuned models significantly outperform base models — TinyLlama achieved 30% while base GPT2 variants scored 0%, confirming that instruction tuning is critical for mathematical reasoning tasks.

---

## Project Overview

The objective of this project is to evaluate open-source LLMs on reasoning benchmarks and compare performance using standardized evaluation metrics.

The framework supports:

- Benchmark evaluation
- Accuracy calculation
- Consistency analysis
- Reliability evaluation
- Hallucination analysis
- Model comparison
- Result visualization
- Report generation

---

## Features

- GSM8K benchmark evaluation
- Accuracy measurement
- Consistency evaluation
- Reliability scoring
- Hallucination analysis
- CSV result generation
- Model comparison
- Visualization using charts
- Modular project structure
- One-command pipeline (`run_all.py`)

---

## Models Evaluated

| Model | Parameters | Type | Status |
|---|---|---|---|
| DistilGPT2 | 82M | Base Model | Completed |
| GPT2-Medium | 345M | Base Model | Completed |
| TinyLlama-1.1B-Chat | 1.1B | Instruction Tuned | Completed |
| Mistral-7B | 7B | Instruction Tuned | Planned |

---

## Supported Benchmarks

| Benchmark | Focus | Status |
|---|---|---|
| GSM8K | Mathematical Reasoning | Completed |
| TruthfulQA | Factual Accuracy / Hallucination | Planned |
| HellaSwag | Common Sense Reasoning | Planned |

---

## Evaluation Metrics

| Metric | Description |
|---|---|
| Accuracy | Measures correctness of model outputs |
| Consistency | Measures stability across multiple evaluations |
| Reliability | Measures overall model dependability |
| Hallucination Rate | Measures unsupported factual outputs |

---

## Project Structure

```text
Open-LLM-Evaluation-Framework/
│
├── config/
│   └── eval_config.json
├── datasets/
│   ├── gsm8k_sample.json
│   └── truthfulqa_sample.json
├── docs/
│   ├── Final_Project_Report.md
│   ├── methodology.md
│   ├── limitations.md
│   └── future_work.md  
├── experiments/
├── report/
│   ├── abstract.md
│   ├── methodology.md
│   ├── results.md
│   ├── error_analysis.md
│   └── conclusions.md
├── results/
│   └── report/
├── src/
│   ├── benchmarks/
│   │   ├── gsm8k_eval.py
│   │   └── truthfulqa_eval.py
│   ├── evaluation/
│   │   └── evaluator.py
│   ├── metrics/
│   │   ├── accuracy.py
│   │   ├── consistency.py
│   │   ├── hallucination.py
│   │   └── reliability.py
│   ├── models/
│   │   ├── model_runner.py
│   │   ├── model_runner_tinyllama.py
│   │   └── model_runner_gemma.py
│   └── visualization/
│       ├── model_comparison.py
│       ├── results_plot.py
│       └── heatmap.py
├── run_all.py
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Current Results

| Model | Parameters | GSM8K Accuracy | Type |
|---|---|---|---|
| DistilGPT2 | 82M | 0% | Base Model |
| GPT2-Medium | 345M | 0% | Base Model |
| TinyLlama-1.1B | 1.1B | 30% | Instruction Tuned |

---

## Error Analysis Summary

| Model | Common Failure Pattern |
|---|---|
| DistilGPT2 | Extracts numbers from question instead of computing answer |
| GPT2-Medium | Same pattern — repeats numbers from input |
| TinyLlama | Correct on simple addition, fails on multi-step reasoning |

---

## How to Run

Clone the repository:
```bash
git clone https://github.com/Tejaa24/Open-LLM-Evaluation-Framework.git
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run full pipeline:
```bash
python run_all.py
```

Run GSM8K benchmark only:
```bash
python -m src.benchmarks.gsm8k_eval
```

---

## Technologies Used

- Python 3.10+
- Hugging Face Transformers
- PyTorch
- Pandas
- Matplotlib
- CSV
- Git / GitHub

---

## Future Work

- Add Mistral-7B evaluation
- Integrate TruthfulQA benchmark
- Integrate HellaSwag benchmark
- Build interactive dashboard
- GPU support for larger models
- Automated benchmarking pipeline

---

## 📚 References

- [GSM8K Paper](https://arxiv.org/abs/2110.14168)
- [TruthfulQA Paper](https://arxiv.org/abs/2109.07958)
- [HuggingFace Transformers](https://github.com/huggingface/transformers)
- [TinyLlama](https://github.com/jzhang38/TinyLlama)

---

## Author

**Adi Lakshamma Bonam**
Computer Science Undergraduate
GitHub: https://github.com/Tejaa24

---

## License

This project is released under the MIT License.
