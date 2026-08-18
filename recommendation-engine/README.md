# 🛍️ AI Product Recommendation Engine

## Business Problem
E-commerce platforms lose 30-40% potential revenue by showing generic "best sellers" instead of personalized recommendations. Intelligent recommendations can increase average order value by 25% and cross-sell conversion by 40%.

**Target:** Demonstrate enterprise recommendation system product thinking — not just the algorithm, but the FULL product system (cold-start, fairness, business rules, A/B testing).

## Live Demo
**Demo:** Run locally — see "How to Run" section below.

## What Makes This Different
Most recommendation demos show ONLY the algorithm. This shows the **complete PM perspective:**
- Collaborative Filtering + Content-Based Hybrid (with configurable weights)
- Cold-start strategy (what to show new users)
- Business rules that OVERRIDE AI (stock, pricing, diversity)
- Fairness checks (category coverage, price fairness, popularity bias)
- A/B test results (proving business impact)
- Explainability (WHY each item is recommended)

## Features
- Hybrid recommendation engine (CF + Content-Based, configurable weights)
- Interactive user selection with purchase history display
- Relevance scoring with confidence indicators
- Simulated A/B test results (CTR, AOV, Revenue/User)
- PM Decision Log (algorithm selection, cold-start, business rules, risk register)
- Fairness dashboard (category coverage, price fairness, popularity bias checks)
- Diversity boost option (prevent filter bubbles)

## Architecture

```
┌─────────────────────────────────────────────┐
│              BUSINESS RULES LAYER            │
│   (Stock check, price bounds, diversity)    │
├──────────────────┬──────────────────────────┤
│  Collaborative   │    Content-Based         │
│  Filtering (60%) │    Filtering (40%)       │
│  User-Item       │    Category + Price      │
│  Similarity      │    Matching              │
├──────────────────┴──────────────────────────┤
│           USER INTERACTION DATA              │
│   (Ratings, Purchases, Browsing)            │
└─────────────────────────────────────────────┘
```

## Tech Stack
| Component | Tool | Why |
|-----------|------|-----|
| Collaborative Filtering | Cosine Similarity (Scikit-learn) | Interpretable, fast for demo scale |
| Data Processing | Pandas + NumPy | Standard |
| Visualization | Plotly | Interactive A/B test charts |
| Frontend | Streamlit | Rapid demo |
| Language | Python 3.10+ | Standard |

## Key PM Decisions

| Decision | Chosen | Why |
|----------|--------|-----|
| CF over Deep Learning | Collaborative Filtering | Interpretable for stakeholders. DL overkill for <1M interactions. |
| Hybrid over single algo | 60/40 CF/Content split | Handles cold-start (content) + serendipity (CF) |
| Business rules override AI | Hard rules > model score | Never recommend out-of-stock. Customer trust > marginal revenue. |
| Explainability built-in | Every rec has a "why" | Users who understand WHY trust 30% more (lower override rate). |
| Diversity enforced | Max 2 items/category | Prevents filter bubble. Long-term engagement > short-term CTR. |

## A/B Test Results (Simulated)
| Metric | Control (No AI) | Treatment (AI Recs) | Lift |
|--------|:-:|:-:|:-:|
| Click-Through Rate | 8.1% | 12.4% | +53% |
| Avg Order Value | $45.20 | $58.40 | +29% |
| Revenue per User | $3.66 | $7.24 | +98% |
| Items per Order | 2.3 | 3.1 | +35% |

## How to Run

```bash
# 1. Clone
git clone https://github.com/VINODANNUKARAN1/ai-product-portfolio.git
cd recommendation-engine

# 2. Install
pip install -r requirements.txt

# 3. Run
streamlit run app.py
```

## Roadmap
- **V1 (Current):** Item-item CF + content hybrid, simulated data, business rules
- **V2:** Matrix factorization (SVD), real interaction logging, session-based recs
- **V3:** Deep learning (Neural Collaborative Filtering), real-time inference
- **V4:** Multi-objective optimization (revenue + fairness + diversity simultaneously)

## Fairness & Responsible AI
| Check | Measurement | Threshold |
|-------|-------------|-----------|
| Category coverage | All categories get exposure | Min 3/6 categories per user |
| Price fairness | Not always pushing expensive | Within 2x user's avg spend |
| Popularity bias | Long-tail gets exposure | Min 20% non-top-100 items |
| Explainability | Every rec has a reason | 100% coverage |

---

*Built by Vinod Annukaran | MSc Data Science | AI Product Manager*
*Demonstrating: Recommendation systems | PM trade-offs | Business rules | Fairness | A/B testing*
