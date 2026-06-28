# Framework Architecture

## System Overview

Input Layer
└── Datasets
├── GSM8K (Mathematical Reasoning)
└── TruthfulQA (Planned)

↓

Evaluation Pipeline
├── Model Loader
│   ├── DistilGPT2 (82M) — Base Model
│   ├── GPT2-Medium (345M) — Base Model
│   └── TinyLlama-1.1B (1.1B) — Instruction Tuned
│
├── Benchmark Runner
│   ├── Question loading
│   ├── Answer generation
│   └── Number extraction (regex)

↓

Metrics Engine
├── Accuracy Calculator
├── Consistency Checker
├── Reliability Scorer
└── Hallucination Detector

↓

Results Storage
├── CSV Reports
├── JSON Summaries
└── Raw outputs

↓

Visualization Layer
├── Accuracy Chart
├── Model Comparison Chart
└── Performance Heatmap

↓

Report Generation
├── Markdown Reports
├── Error Analysis
└── PDF Final Report

## Key Design Decisions

| Decision | Reason |
|---|---|
| Modular structure | Easy to add new models and benchmarks |
| Regex number extraction | Handles varied model output formats |
| CSV storage | Easy to analyze results later |
| Separate model runners | Each model has independent configuration |