# 🎯 AI Customer Intelligence Platform

## Business Problem
Companies have millions of customers but treat them identically. Personalized strategy per segment increases revenue by 15-30%, yet most organizations lack the tools to bridge ML clustering with actionable business recommendations.

**Target:** Transform raw transaction data into business strategy — demonstrating how a PM bridges data science and commercial impact.

## Live Demo
[Try it here](YOUR_STREAMLIT_URL) — Explore 1,000+ customers segmented by AI with real-time business recommendations.

## What Makes This Different
Most data scientists stop at clusters. This platform goes further:
- Raw Data → ML Segmentation → **Business Strategy per Segment**
- Each segment gets: budget allocation, channel strategy, ROI projection, campaign triggers
- PM Decision Log documents WHY certain algorithms and features were chosen

## Features
- RFM-based K-Means clustering (auto-generates 5 business segments)
- Interactive 3D visualization of customer clusters
- Revenue attribution per segment (% of customers vs % of revenue)
- AI-generated business recommendations with budget + ROI projections
- Configurable number of segments (3-8 clusters)
- PM Decision Log (algorithm selection rationale, feature choices, V2 roadmap)

## Segments Generated
| Segment | Strategy | Expected ROI |
|---------|----------|:------------:|
| Champions | Retain & Reward | 3x |
| Loyal Customers | Upsell & Cross-sell | 2.5x |
| Recent Buyers | Nurture & Convert | 2x |
| At Risk | Win-Back (Urgent) | 1.5x |
| Need Attention | Activate or Sunset | 0.8x |

## Tech Stack
| Component | Tool | Why This Choice |
|-----------|------|-----------------|
| Clustering | K-Means (Scikit-learn) | Interpretable for business stakeholders |
| Features | RFM (Recency, Frequency, Monetary) | Captures 80% of behavioral variance |
| Visualization | Plotly (3D scatter + pie + histogram) | Interactive, professional |
| Frontend | Streamlit | Rapid prototyping, free deployment |
| Language | Python 3.10+ | Industry standard |

## Key PM Decisions

| Decision | Options Considered | Chosen | Reasoning |
|----------|-------------------|--------|-----------|
| Algorithm | K-Means vs DBSCAN vs GMM vs Hierarchical | K-Means | Business needs interpretability over statistical perfection. Stakeholders must understand and act on segments. |
| Features | RFM vs 20+ behavioral features | RFM (3 features) | Pareto: 3 features capture 80% of variance. Adding more increases complexity without proportional insight gain. |
| Segments | 3 vs 5 vs 8 | 5 (configurable) | Sweet spot: enough granularity for distinct strategies, few enough for humans to manage. |
| Output | Just clusters vs Clusters + Strategy | Clusters + Strategy | A PM's job is "So what?" Not just "here are segments" but "here's what to DO." |

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/ai-customer-intelligence.git
cd ai-customer-intelligence

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

## Roadmap
- **V1 (Current):** Static dataset, K-Means, manual strategy mapping
- **V2:** Real-time data ingestion, auto-retraining when segments shift
- **V3:** LLM-generated personalized messages per segment
- **V4:** A/B testing integration (test strategies per segment), marketing automation triggers

## What I'd Do Differently in Production
1. Connect to real data warehouse (Snowflake/BigQuery) instead of synthetic data
2. Add time-series: track segment migration (who moved from "Loyal" to "At Risk"?)
3. A/B test recommendations per segment (prove ROI empirically)
4. Build API endpoint for marketing tools (trigger campaigns automatically)
5. Add churn prediction MODEL per segment (not just RFM clustering)
6. Executive dashboard view (C-suite wants 1 slide, not 4 tabs)

---

*Built by Vinod Annukaran | MSc Data Science | AI Product Manager*
*Demonstrating: ML → Business strategy bridge | PM decision-making | Commercial thinking*
