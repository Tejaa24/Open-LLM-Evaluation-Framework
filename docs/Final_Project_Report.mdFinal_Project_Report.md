# Chapter 1 – Introduction

## 1.1 Introduction

Large Language Models (LLMs) have become one of the most important developments in Artificial Intelligence. These models are capable of understanding natural language, generating human-like text, solving reasoning problems, answering questions, and assisting users in various applications. Many organizations have released open-source language models that can be used for research and development.

Although these models perform well on many tasks, their performance is not always consistent. Different models may produce different answers for the same question, and some models may generate incorrect or unsupported information. Therefore, evaluating the performance of open-source LLMs has become an important research area.

This project presents an evaluation framework for benchmarking open-source Large Language Models using standard benchmark datasets. The framework focuses on measuring model performance using multiple evaluation metrics such as accuracy, consistency, reliability, and hallucination analysis.

The framework has been implemented using Python and the Hugging Face Transformers library. Benchmark datasets are processed through an automated evaluation pipeline, and the generated outputs are analyzed to compare different language models. The framework also stores results in CSV format and generates visual reports for easier interpretation.

During this project, DistilGPT2 and TinyLlama models were integrated and evaluated using a GSM8K benchmark prototype. The evaluation pipeline successfully generated benchmark reports and comparison results, providing a reusable framework for future LLM benchmarking experiments.


# Chapter 2 – Literature Survey

## 2.1 Background

Large Language Models (LLMs) have rapidly evolved in recent years and are widely used for text generation, question answering, summarization, and reasoning tasks. Models such as GPT, LLaMA, Mistral, Gemma, and TinyLlama demonstrate strong capabilities across various natural language processing applications.

As the number of available open-source models continues to grow, selecting an appropriate model for a specific application has become increasingly challenging. Different models exhibit varying levels of reasoning ability, factual correctness, inference speed, and computational efficiency.

## 2.2 Need for Evaluation

Most language models are evaluated using benchmark datasets. However, benchmark scores alone are often insufficient to understand a model's overall reliability. A comprehensive evaluation framework should measure not only accuracy but also consistency, robustness, and the tendency to generate hallucinated information.

Benchmark-based evaluation enables researchers to compare multiple models under identical conditions, making performance comparisons more objective and reproducible.

## 2.3 Existing Evaluation Benchmarks

Several benchmark datasets are commonly used for evaluating Large Language Models:

- GSM8K – Mathematical reasoning benchmark.
- TruthfulQA – Measures factual correctness and hallucination.
- HellaSwag – Evaluates commonsense reasoning.

These benchmarks provide standardized tasks that allow fair comparison across different language models.

## 2.4 Motivation

The motivation behind this project is to develop a lightweight and reusable evaluation framework capable of benchmarking multiple open-source language models. The framework automates model inference, benchmark execution, result collection, and performance reporting while remaining easy to extend for future research.


# Chapter 3 – System Design

## 3.1 Project Architecture

The Open LLM Evaluation Framework is designed as a modular benchmarking system that evaluates multiple open-source Large Language Models using standardized benchmark datasets.

The framework consists of the following components:

- Dataset Loader
- Model Runner
- Evaluation Engine
- Metrics Calculator
- Report Generator
- Visualization Module

Each component operates independently, making the framework easy to maintain and extend.

---

## 3.2 Workflow

The overall workflow of the framework is as follows:

1. Load benchmark dataset.
2. Select the target language model.
3. Generate model predictions.
4. Compare predictions with expected answers.
5. Calculate evaluation metrics.
6. Store evaluation results.
7. Generate visualizations and reports.

This workflow ensures reproducibility across multiple benchmark evaluations.

---

## 3.3 Project Structure

The project is organized into the following directories:

```
├── config/
├── datasets/
├── docs/
├── experiments/
├── presentation/
├── report/
├── results/
│   └── report/
├── src/
│   ├── benchmarks/
│   ├── evaluation/
│   ├── metrics/
│   ├── models/
│   └── visualization/
├── run_all.py
├── generate_pdf.py
├── README.md
└── requirements.txt
```

The modular directory structure improves readability and simplifies future development.

---

## 3.4 Evaluation Pipeline

The evaluation pipeline follows a sequential execution process:

Dataset
↓
Model Loading
↓
Answer Generation
↓
Prediction Evaluation
↓
Metric Calculation
↓
Result Storage
↓
Visualization

This pipeline allows benchmarking multiple models under identical experimental conditions.

---

## 3.5 Design Advantages

The proposed framework offers several advantages:

- Modular architecture
- Easy integration of new language models
- Reproducible benchmark execution
- Automated result generation
- Extensible evaluation metrics
- Research-oriented implementation


# Chapter 4 – Implementation

## 4.1 Development Environment

The project was implemented using Python and the Hugging Face Transformers library. Visual Studio Code was used as the primary development environment, while Git and GitHub were used for version control.

### Software Used

| Software | Purpose |
|----------|---------|
| Python | Programming Language |
| Visual Studio Code | Development Environment |
| Transformers | Model Loading |
| Hugging Face Hub | Model Repository |
| Git | Version Control |
| GitHub | Project Hosting |

---

## 4.2 Implemented Models

The framework currently supports evaluation of multiple open-source language models.

### DistilGPT2

DistilGPT2 was used as the baseline language model because of its lightweight architecture and fast inference speed.

Observed Characteristics:

- Small model size
- Fast inference
- Weak mathematical reasoning
- Poor GSM8K performance

---

### TinyLlama

TinyLlama was integrated for benchmark evaluation.

Observed Characteristics:

- Better reasoning capability
- Improved benchmark accuracy
- Better instruction following
- Suitable for lightweight evaluation

---

### Phi-2

Microsoft Phi-2 was explored as an additional comparison model.

Observed Characteristics:

- Strong reasoning capability
- Higher computational requirements
- Large model download size
- Longer loading time

---

## 4.3 Benchmark Implementation

The GSM8K benchmark prototype was implemented using a small evaluation dataset.

The benchmark execution pipeline performs the following steps:

1. Load benchmark questions.
2. Generate model predictions.
3. Compare generated answers with expected answers.
4. Calculate accuracy.
5. Save results into CSV files.
6. Generate summary reports.

---

## 4.4 Result Storage

Generated outputs are automatically stored inside the project.

```
results/
└── report/
    ├── gsm8k_mini_results.csv
    ├── gsm8k_results_summary.md
    ├── accuracy_chart.png
    ├── model_comparison.png
    ├── error_analysis.md
```

This enables easy visualization and future analysis.

---

## 4.5 Challenges Faced

During implementation, several practical challenges were encountered:

- Hugging Face model download delays
- Authentication issues for gated models
- Large model sizes
- Windows dependency configuration
- GPU availability limitations
- Benchmark compatibility across different models

These challenges were resolved through model selection, environment configuration, and modular project design.


# Chapter 5 – Results and Discussion

## 5.1 Experimental Results

The Open LLM Evaluation Framework was tested using a prototype GSM8K benchmark consisting of sample mathematical reasoning questions.

Three lightweight language models were considered during experimentation:

- DistilGPT2
- TinyLlama
- Phi-2 (implementation explored)

---

## 5.2 Benchmark Results

| Model | Parameters | Type | Accuracy | Consistency | Status |
|---|---|---|---|---|---|
| DistilGPT2 | 82M | Base Model | 0% | Consistent | Completed |
| GPT2-Medium | 345M | Base Model | 0% | Consistent | Completed |
| TinyLlama-1.1B | 1.1B | Instruction Tuned | 30% | Consistent | Completed |

---

## 5.3 Result Analysis

### DistilGPT2

DistilGPT2 generated incomplete responses for mathematical reasoning tasks. Although inference was fast, its reasoning capability was limited, resulting in poor benchmark accuracy

### TinyLlama
TinyLlama demonstrated significantly better reasoning 
performance, achieving 30% accuracy on GSM8K. Being an 
instruction-tuned model, it correctly answered simple 
addition problems but struggled with subtraction and 
multiplication tasks.

### GPT2-Medium
GPT2-Medium (345M parameters) was evaluated as a middle 
ground between DistilGPT2 and TinyLlama. Despite being 
4x larger than DistilGPT2, it achieved 0% accuracy — 
confirming that model size alone without instruction 
tuning does not improve reasoning ability.

---

## 5.4 Discussion

The experimental results indicate that model architecture has a significant impact on reasoning performance.

Smaller general-purpose language models such as DistilGPT2 perform well for lightweight text generation but struggle with reasoning tasks.

Instruction-tuned models such as TinyLlama demonstrate improved reasoning performance while maintaining relatively low computational requirements.

Larger reasoning-focused models like Phi-2 offer additional potential but require greater computational resources.

---

## 5.5 Summary

The implemented framework successfully:

- Evaluated multiple open-source language models
- Generated benchmark reports
- Calculated evaluation metrics
- Stored experimental results
- Produced visual comparison reports

The modular design also allows future integration of additional benchmark datasets and language models.


# Chapter 6 – Conclusion and Future Work

## 6.1 Conclusion

This project presented the design and implementation of an Open LLM Evaluation Framework for assessing the performance of open-source Large Language Models.

A prototype evaluation pipeline was successfully developed using Python and the Hugging Face Transformers library. The framework supports benchmark execution, accuracy calculation, result storage, and performance comparison.

The GSM8K benchmark was used as a proof of concept to evaluate mathematical reasoning capability. Experimental results showed that TinyLlama outperformed DistilGPT2 on the prototype benchmark, demonstrating stronger reasoning performance.

The project also explored the integration of additional open-source models such as Phi-2, highlighting the flexibility and extensibility of the framework.

Overall, the project provides a modular foundation for future research on benchmarking, reliability analysis, and comparative evaluation of open-source language models.

---

## 6.2 Future Work

The framework can be extended in several ways:

- Integrate additional benchmark datasets such as TruthfulQA, HellaSwag, and MMLU.
- Evaluate larger open-source language models.
- Implement hallucination detection metrics.
- Support automated multi-model evaluation.
- Add statistical analysis of benchmark results.
- Develop an interactive dashboard for visualization.
- Enable GPU-accelerated evaluation for larger models.
- Expand benchmark coverage for research applications.

---

## References

1. Hugging Face Transformers Documentation.
2. GSM8K Benchmark Dataset.
3. Hugging Face Model Hub.
4. Python Documentation.
5. GitHub Documentation.