# 📊 AI Product Metrics Dashboard

## Business Problem
AI products fail when teams track ONLY model accuracy. A model with 95% precision that users don't trust, costs too much to run, or doesn't drive revenue is a **failed product**. PMs need a holistic measurement framework.

**Insight:** AI products need 4 metric categories tracked simultaneously — not just "is the model accurate?"

## Live Demo
**Demo:** Run locally — see "How to Run" section below.

## The 4-Quadrant Measurement Framework

```
┌─────────────────────┬─────────────────────┐
│   🔬 MODEL HEALTH   │   💰 BUSINESS IMPACT │
│   Precision, Recall │   Revenue, Conv Rate │
│   NDCG, Drift Score │   Basket Size, CTR   │
├─────────────────────┼─────────────────────┤
│   👤 USER TRUST     │   ⚙️ OPERATIONS      │
│   Satisfaction, NPS │   Latency, Cost      │
│   Override Rate     │   Uptime, Throughput │
│   Feature Adoption  │   Monthly Infra $    │
└─────────────────────┴─────────────────────┘
```

**Key PM Insight:** A model that scores well in ONE quadrant but fails in others should NOT ship.

## Features
- Real-time 90-day metrics visualization across all 4 quadrants
- Alert thresholds (model drift > 0.2 triggers retraining alert)
- Business ROI summary (Before AI vs After AI comparison)
- Trust interpretation (override rate + adoption rate = trust proxy)
- Cost analysis (cost per prediction, monthly infra, cost per $1 revenue)
- KPI summary strip with week-over-week deltas

## Metrics Tracked

### Model Health
| Metric | What It Means | Alert If |
|--------|---------------|----------|
| Precision@5 | Of top 5 recommendations, how many are relevant | < 0.70 |
| Recall@10 | Of all relevant items, how many appear in top 10 | < 0.60 |
| NDCG | Ranking quality (are best items ranked highest?) | < 0.65 |
| Drift Score | Has the model's behavior changed from training? | > 0.20 |

### Business Impact
| Metric | What It Means | Target |
|--------|---------------|--------|
| Revenue/Session | $ attributed to AI recommendations | > $4.50 |
| Conversion Rate | % of AI-shown users who purchase | > 3.2% |
| Avg Basket Size | Items per order (AI cross-sell effect) | > 3.0 |
| CTR | Click-through on recommendations | > 15% |

### User Trust
| Metric | What It Means | Target |
|--------|---------------|--------|
| Satisfaction | 1-5 user rating of recommendations | > 4.0 |
| Override Rate | % of times users IGNORE AI suggestion | < 15% |
| Feature Adoption | % of eligible users engaging with AI | > 50% |

### Operations
| Metric | What It Means | SLA |
|--------|---------------|-----|
| P95 Latency | 95th percentile response time | < 250ms |
| Cost/Prediction | Infrastructure cost per AI call | < $0.01 |
| Uptime | Service availability | > 99.9% |
| Throughput | Predictions served per day | Capacity |

## Tech Stack
| Component | Tool | Why |
|-----------|------|-----|
| Dashboard | Streamlit | Rapid, interactive, free |
| Charts | Plotly | Professional, interactive, publication-quality |
| Data | Pandas + NumPy (simulated) | Realistic time-series patterns |
| Language | Python 3.10+ | Standard |

## How to Run

```bash
# 1. Clone
git clone https://github.com/VINODANNUKARAN1/ai-product-portfolio.git
cd product-metrics-dashboard

# 2. Install
pip install -r requirements.txt

# 3. Run
streamlit run app.py
```

## PM's Metrics Philosophy

> "If you can't measure it, you can't improve it. But if you measure the WRONG thing, you'll improve the wrong thing."

**Common PM mistakes with AI metrics:**
1. Tracking only accuracy (ignoring user trust)
2. Optimizing for model performance (ignoring business ROI)
3. Shipping fast (ignoring operational costs that scale)
4. Celebrating adoption (ignoring satisfaction/quality)

**This dashboard forces holistic thinking.** All 4 quadrants must be green to call an AI product "successful."

## Roadmap
- **V1 (Current):** Simulated data, 4-quadrant dashboard, alert thresholds
- **V2:** Connect to real model monitoring (MLflow/Weights & Biases integration)
- **V3:** Automated alerting (Slack/email when thresholds breached)
- **V4:** Causal attribution (A/B test integration to prove AI vs baseline)

---

*Built by Vinod Annukaran | MSc Data Science | AI Product Manager*
*Demonstrating: AI product measurement | 4-quadrant framework | PM metrics thinking*
