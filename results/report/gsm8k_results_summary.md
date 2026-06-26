# GSM8K Mini Evaluation Summary

## Experiment

A mini GSM8K benchmark evaluation was performed to compare the reasoning performance of open-source language models.

## Models Evaluated

1. DistilGPT2
2. TinyLlama 1.1B Chat

## Results

| Model | Accuracy |
|---------|---------|
| DistilGPT2 | 0.0 |
| TinyLlama | 1.0 |

## Observations

- TinyLlama successfully solved all benchmark questions.
- DistilGPT2 failed to produce correct numerical reasoning outputs.
- TinyLlama demonstrated significantly better reasoning capability than DistilGPT2.
- Benchmark result storage and reporting modules worked correctly.

## Limitations

- Only a small GSM8K sample set was evaluated.
- Phi-2 could not be fully evaluated due to model loading issues.
- Mistral benchmarking is pending.

## Conclusion

TinyLlama outperformed DistilGPT2 on the GSM8K mini benchmark and proved more suitable for mathematical reasoning tasks. The evaluation framework successfully generated benchmark reports, accuracy metrics, and comparison results.

## Future Work

- Expand GSM8K coverage.
- Add Mistral benchmarking.
- Evaluate larger instruction-tuned models.
- Add automated leaderboard generation.