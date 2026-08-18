# RICE-AI Prioritization Framework

## Standard RICE vs AI-Adapted RICE

Traditional RICE doesn't account for AI-specific factors like model uncertainty, data availability, and ethical risk.

## AI-RICE Formula

**Score = (Reach × Impact × Confidence × Data Readiness) / (Effort + Risk Penalty)**

### Factors

| Factor | Scale | AI-Specific Consideration |
|--------|-------|---------------------------|
| **Reach** | # users affected/quarter | Same as standard RICE |
| **Impact** | 0.25 / 0.5 / 1 / 2 / 3 | Consider: accuracy improvement vs user-visible change |
| **Confidence** | 0-100% | Lower for novel AI (no prior art) vs proven patterns (recommendation engines) |
| **Data Readiness** | 0-100% | Do we have clean, labeled, sufficient training data? |
| **Effort** | Person-months | Include: data labeling, model training, evaluation, monitoring setup |
| **Risk Penalty** | 0-3 (0=safe, 3=high ethical/safety risk) | Bias risk, hallucination potential, regulatory exposure |

## Example Scoring

| Feature | Reach | Impact | Confidence | Data Ready | Effort | Risk | Score |
|---------|:-----:|:------:|:----------:|:----------:|:------:|:----:|:-----:|
| Smart search (semantic) | 50K | 2 | 80% | 90% | 4 | 0 | 18,000 |
| Auto-categorization | 30K | 1 | 90% | 95% | 2 | 0 | 12,825 |
| AI content generation | 20K | 3 | 50% | 60% | 6 | 2 | 2,250 |
| Fraud detection | 5K | 3 | 70% | 80% | 8 | 1 | 933 |

## When to Use
- Quarterly roadmap planning for AI product teams
- Comparing AI features against non-AI features fairly
- Communicating prioritization rationale to stakeholders
