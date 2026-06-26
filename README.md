# Open-LLM-Evaluation-Framework

A research-oriented framework for evaluating open-source Large Language Models (LLMs) using benchmark datasets and multiple evaluation metrics. The framework supports benchmarking, model comparison, result visualization, and report generation.

---

# Project Overview

The objective of this project is to evaluate the performance of open-source LLMs on reasoning benchmarks and compare their performance using standardized evaluation metrics.

The framework currently supports:

- Benchmark evaluation
- Accuracy calculation
- Consistency analysis
- Reliability evaluation
- Hallucination analysis
- Model comparison
- Result visualization
- Report generation

---

# Features

- GSM8K benchmark evaluation
- Accuracy measurement
- Consistency evaluation
- Reliability scoring
- Hallucination analysis
- CSV result generation
- Model comparison
- Visualization using charts
- Modular project structure

---

# Models Evaluated

| Model | Status |
|--------|--------|
| DistilGPT2 | Completed |
| TinyLlama-1.1B-Chat | Completed |
| Phi-2 | In Progress |
| Mistral | Planned |

---

# Supported Benchmarks

- GSM8K
- TruthfulQA (Planned)
- HellaSwag (Planned)

---

# Evaluation Metrics

| Metric | Description |
|---------|-------------|
| Accuracy | Measures correctness of model outputs |
| Consistency | Measures stability across multiple evaluations |
| Reliability | Measures overall model dependability |
| Hallucination Rate | Measures unsupported factual outputs |

---

# Project Structure

```text
Open-LLM-Evaluation-Framework/
│
├── datasets/
├── docs/
├── experiments/
├── presentation/
├── results/
│   └── report/
├── src/
│   ├── benchmarks/
│   ├── metrics/
│   ├── models/
│   └── visualization/
├── README.md
├── LICENSE
└── requirements.txt
```

---

# Current Progress

Completed

- Evaluation framework
- GSM8K benchmark pipeline
- DistilGPT2 integration
- TinyLlama integration
- Accuracy calculation
- CSV report generation
- Result visualization
- Model comparison
- Documentation

---

# Current Results

| Model | Accuracy | Consistency | Reliability | Status |
|--------|-----------|-------------|-------------|--------|
| DistilGPT2 | 0.0 | Low | Low | Completed |
| TinyLlama | 1.0 | High | High | Completed |
| Phi-2 | N/A | N/A | N/A | In Progress |
| Mistral | N/A | N/A | N/A | Planned |

---

# Generated Outputs

The framework automatically generates:

- GSM8K evaluation report
- Accuracy report
- Model comparison report
- CSV benchmark results
- Accuracy graph
- Model comparison graph

Generated files are stored in:

```text
results/report/
```

---

# Technologies Used

- Python
- Hugging Face Transformers
- Pandas
- Matplotlib
- CSV
- Git
- GitHub

---

# How to Run

Clone the repository

```bash
git clone https://github.com/Tejaa24/Open-LLM-Evaluation-Framework.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run benchmark

```bash
python -m src.benchmarks.gsm8k_eval
```

---

# Future Work

- Evaluate Phi-2 completely
- Add Mistral evaluation
- Integrate TruthfulQA benchmark
- Integrate HellaSwag benchmark
- Add automated benchmarking pipeline
- Build interactive dashboard
- Support additional open-source LLMs

---

# Research Applications

- Large Language Models
- Benchmarking
- Explainable AI
- AI Safety
- Reliability Analysis
- Transformer Models
- Machine Learning Research

---

# Author

**Adi Lakshamma Bonam**

Computer Science Undergraduate

GitHub: https://github.com/Tejaa24

---

# License

This project is released under the MIT License.