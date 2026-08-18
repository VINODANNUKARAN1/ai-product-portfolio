# Model Evaluation Scorecard

## Purpose
Use this scorecard to decide if an AI/ML model is READY TO SHIP.
A model must pass ALL categories to go to production.

## Model Information
- **Model Name:** [Name]
- **Version:** [v1.0]
- **Task:** [Classification / Generation / Recommendation / etc.]
- **Evaluator:** [PM Name]
- **Date:** [Date]

## Evaluation Criteria

### 1. Accuracy & Quality (Must Pass)

| Metric | Threshold | Actual | Pass? |
|--------|:---------:|:------:|:-----:|
| Primary metric (e.g., Precision) | > X% | | |
| Secondary metric (e.g., Recall) | > Y% | | |
| Error rate | < Z% | | |
| Hallucination rate (for GenAI) | < W% | | |

### 2. Fairness & Bias (Must Pass)

| Check | Threshold | Actual | Pass? |
|-------|:---------:|:------:|:-----:|
| Performance across demographics | < 5% gap | | |
| No disparate impact on protected groups | Verified | | |
| Tested on diverse inputs | Yes | | |

### 3. Safety & Robustness (Must Pass)

| Check | Threshold | Actual | Pass? |
|-------|:---------:|:------:|:-----:|
| Adversarial input handling | Graceful degradation | | |
| Edge case behavior | No harmful outputs | | |
| Prompt injection resistance (GenAI) | Blocked | | |
| PII leakage | Zero | | |

### 4. Operational Readiness (Must Pass)

| Check | Threshold | Actual | Pass? |
|-------|:---------:|:------:|:-----:|
| P95 latency | < Xms | | |
| Throughput | > Y req/sec | | |
| Cost per prediction | < $Z | | |
| Monitoring in place | Yes | | |
| Rollback plan documented | Yes | | |
| Alerting configured | Yes | | |

### 5. User Experience (Should Pass)

| Check | Threshold | Actual | Pass? |
|-------|:---------:|:------:|:-----:|
| User satisfaction (beta test) | > 4.0/5 | | |
| Task completion rate | > X% | | |
| Explainability available | Yes | | |
| Fallback UX when AI fails | Designed | | |

## Final Decision

| Decision | Criteria |
|----------|----------|
| SHIP | All 4 "Must Pass" sections pass + UX acceptable |
| FIX & RETEST | 1-2 failures in non-critical areas |
| BLOCK | Any safety or fairness failure |
| KILL | Fundamental accuracy below threshold |

## Decision: [ SHIP / FIX / BLOCK / KILL ]

**Rationale:** [Why this decision]

**Next Steps:** [What happens now]

---
*Template by Vinod Annukaran | AI Product Manager*
