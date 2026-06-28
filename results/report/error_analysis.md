# Error Analysis

## Overview
Detailed analysis of model failures on GSM8K benchmark.

---

## DistilGPT2 — Error Patterns

**Accuracy: 0/10 (0%)**

| Question | Expected | Extracted | Error Type |
|---|---|---|---|
| John has 5 apples and buys 3 more | 8 | 1.0 | Extracts random number from question |
| A box contains 10 balls, 2 removed | 8 | 10.0 | Repeats first number in question |
| Sara has 12 candies, gives 4 away | 8 | 3.0 | Extracts last number from question |
| Farmer has 7 cows, buys 5 more | 12 | 7.0 | Repeats first number in question |
| Train has 50 seats, 23 occupied | 27 | None | No number generated at all |

**Root Cause:**
DistilGPT2 is a base language model with no instruction
tuning. It cannot understand mathematical questions.
It simply repeats or extracts numbers from the input
without performing any calculation.

---

## GPT2-Medium — Error Patterns

**Accuracy: 0/10 (0%)**

| Question | Expected | Extracted | Error Type |
|---|---|---|---|
| John has 5 apples and buys 3 more | 8 | 5.0 | Repeats first number |
| A box contains 10 balls, 2 removed | 8 | 2.0 | Repeats last number |
| Farmer has 7 cows, buys 5 more | 12 | 7.0 | Repeats first number |
| Train has 50 seats, 23 occupied | 27 | 23.0 | Repeats last number |
| Class has 30 students, 11 absent | 19 | None | No number generated |

**Root Cause:**
Same failure pattern as DistilGPT2 despite being
4x larger. Confirms that base model architecture
cannot perform arithmetic reasoning regardless of size.

---

## TinyLlama — Error Patterns

**Accuracy: 3/10 (30%)**

### Correct Cases:
| Question | Expected | Extracted |
|---|---|---|
| John has 5 apples and buys 3 more | 8 | 8.0 ✅ |
| A box contains 10 balls, 2 removed | 8 | 8.0 ✅ |
| Tom has 20 stickers, gives away 8 | 12 | 12.0 ✅ |

### Failed Cases:
| Question | Expected | Extracted | Error Type |
|---|---|---|---|
| Sara has 12 candies, gives 4 away | 8 | 10.0 | Addition instead of subtraction |
| Farmer has 7 cows, buys 5 more | 12 | 5.0 | Extracts operand only |
| 3 baskets with 4 apples each | 12 | 4.0 | Fails on multiplication |
| Train has 50 seats, 23 occupied | 27 | 37.0 | Wrong subtraction |

**Root Cause:**
TinyLlama handles simple addition correctly but
struggles with subtraction and multiplication.
Multi-step reasoning also causes failures.

---

## Summary of Error Types

| Error Type | DistilGPT2 | GPT2-Medium | TinyLlama |
|---|---|---|---|
| Repeats input number | 7/10 | 8/10 | 0/10 |
| No output generated | 3/10 | 2/10 | 0/10 |
| Wrong operation | 0/10 | 0/10 | 5/10 |
| Correct answer | 0/10 | 0/10 | 3/10 |

---

## Key Insight

> Base models (DistilGPT2, GPT2-Medium) fail because
> they have no instruction following ability.
> TinyLlama partially succeeds because it was trained
> with instruction tuning on math-related tasks.
> This confirms instruction tuning is the key factor
> for reasoning performance, not model size alone.