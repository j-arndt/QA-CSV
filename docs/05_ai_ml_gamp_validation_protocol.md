# Operational Qualification Protocol: Non-Deterministic AI/ML Systems
### *VAL-PROT-AI-088 | Under ISPE GAMP® AI & ISO/IEC 42001:2023*

---

## 1. Executive Summary & The Non-Deterministic Challenge

In classical CSV, deterministic algorithms are validated by asserting $f(x) == y$. When validating Machine Learning models—such as Process Analytical Technology (PAT) using Raman spectroscopy to predict real-time dissolution curves of lysergide ODT or NLP pipelines extracting clinical adverse event signals—natural probabilistic variance causes exact string-matching assertions to fail.

This protocol operationalizes the **ISPE GAMP® AI Framework** using statistical confidence intervals and automated human-in-the-loop exception gating.

---

## 2. Statistical Acceptance Criteria & Wilson Score Intervals

### 2.1 Hypothesis Testing
* **Null Hypothesis ($H_0$):** The AI model's accuracy on the qualified benchmark dataset is $< 90\%$ ($\pi < 0.90$).
* **Alternative Hypothesis ($H_1$):** The AI model's accuracy is $\ge 90\%$ ($\pi \ge 0.90$) at $95\%$ statistical confidence ($p < 0.01$).

### 2.2 Mathematical Formulation (Wilson Score Lower Bound)
$$\text{LB}_{95\%} = \frac{\hat{p} + \frac{z^2}{2n} - z \sqrt{\frac{\hat{p}(1-\hat{p})}{n} + \frac{z^2}{4n^2}}}{1 + \frac{z^2}{n}}$$

Where:
* $n$ = Total benchmark test cases ($n = 50$)
* $\hat{p}$ = Observed empirical accuracy
* $z$ = 1.96 (for 95% two-sided confidence)
* **Acceptance Threshold:** $\text{LB}_{95\%} \ge 0.900$

---

## 3. Human-in-the-Loop (HITL) Exception Gating Architecture

```
                          [RAW CLINICAL / PAT INPUT]
                                      │
                                      ▼
                        [AI/ML MODEL INFERENCE ENGINE]
                                      │
                                      ▼
                      [CONFIDENCE SCORE EVALUATION (C)]
                                      │
                    ┌─────────────────┴─────────────────┐
                    ▼                                   ▼
          HIGH CONFIDENCE (C >= 0.90)         LOW CONFIDENCE (C < 0.90)
                    │                                   │
                    ▼                                   ▼
        [AUTOMATED GxP PART 11 LOG]         [ESCALATE TO HITL QUEUE]
        • SHA-256 Event Record              • Qualified SME Clinical Review
        • Contemporaneous UTC Time          • 21 CFR Part 11 Electronic Signature
        • Auto-Release to Next Stage        • Documented Reason for Decision
```

---

## 4. Model Change Control & Drift Monitoring Invariants

1. **Retraining & Weight Updates:** Any fine-tuning or weight modification triggers automatic regression testing against the SHA-256 locked Golden Benchmark Dataset.
2. **Drift Monitoring:** Daily production inference distributions are compared against baseline distributions using Kolmogorov-Smirnov statistical testing.
3. **Fail-Safe Quarantine:** If rolling 7-day model confidence dips below 90%, the system automatically falls back to 100% human-verified mode.
