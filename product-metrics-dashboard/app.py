"""
AI Product Metrics Dashboard
Built by Vinod Kunhi Krishnan Annukaran

Purpose: Demonstrate how to MEASURE AI products differently from traditional products.
Key Insight: AI products need 4 metric categories tracked simultaneously:
  1. Model Health (technical)
  2. Business Impact (revenue/growth)
  3. User Trust (satisfaction/adoption)
  4. Operational (cost/latency/reliability)
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

st.set_page_config(page_title="AI Product Metrics", page_icon="📊", layout="wide")

st.title("📊 AI Product Metrics Dashboard")
st.markdown("**Monitoring an AI Recommendation Engine in Production**")

# Generate realistic time-series data
@st.cache_data
def generate_metrics(days=90):
    dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
    np.random.seed(42)
    
    return pd.DataFrame({
        'date': dates,
        # Model metrics
        'precision_at_5': 0.72 + np.cumsum(np.random.normal(0.001, 0.005, days)),
        'recall_at_10': 0.65 + np.cumsum(np.random.normal(0.0005, 0.004, days)),
        'ndcg': 0.68 + np.cumsum(np.random.normal(0.0008, 0.003, days)),
        'model_drift_score': np.abs(np.random.normal(0, 0.1, days)),
        # Business metrics
        'revenue_per_session': 4.5 + np.cumsum(np.random.normal(0.01, 0.05, days)),
        'conversion_rate': 0.032 + np.cumsum(np.random.normal(0.0001, 0.0005, days)),
        'avg_basket_size': 3.2 + np.cumsum(np.random.normal(0.005, 0.02, days)),
        'click_through_rate': 0.15 + np.cumsum(np.random.normal(0.0005, 0.003, days)),
        # User metrics
        'user_satisfaction': 4.1 + np.random.normal(0, 0.15, days),
        'override_rate': 0.12 + np.random.normal(0, 0.02, days),
        'feature_adoption': 0.45 + np.cumsum(np.random.normal(0.002, 0.005, days)),
        # Operational metrics
        'p95_latency_ms': 180 + np.random.normal(0, 20, days),
        'cost_per_prediction': 0.008 + np.random.normal(0, 0.001, days),
        'uptime_pct': 99.9 + np.random.normal(0, 0.05, days),
        'predictions_per_day': 50000 + np.cumsum(np.random.normal(100, 500, days)),
    })

data = generate_metrics()
latest = data.iloc[-1]
prev_week = data.iloc[-7]

# KPI Summary Row
st.markdown("### Key Indicators (Last 24 Hours)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Revenue/Session", f"${latest['revenue_per_session']:.2f}", 
              f"+${latest['revenue_per_session'] - prev_week['revenue_per_session']:.2f} vs last week")
with col2:
    st.metric("Model Precision@5", f"{latest['precision_at_5']:.1%}", 
              f"{(latest['precision_at_5'] - prev_week['precision_at_5'])*100:.1f}pp")
with col3:
    st.metric("User Satisfaction", f"{latest['user_satisfaction']:.2f}/5", 
              f"{latest['user_satisfaction'] - prev_week['user_satisfaction']:.2f}")
with col4:
    st.metric("P95 Latency", f"{latest['p95_latency_ms']:.0f}ms", 
              f"{latest['p95_latency_ms'] - prev_week['p95_latency_ms']:.0f}ms",
              delta_color="inverse")

st.divider()

# Four-Panel Dashboard
tab1, tab2, tab3, tab4 = st.tabs(["🔬 Model Health", "💰 Business Impact", "👤 User Trust", "⚙️ Operations"])

with tab1:
    st.header("Model Health Metrics")
    
    col1, col2 = st.columns(2)
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['date'], y=data['precision_at_5'], name='Precision@5', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=data['date'], y=data['recall_at_10'], name='Recall@10', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=data['date'], y=data['ndcg'], name='NDCG', line=dict(color='purple')))
        fig.add_hline(y=0.7, line_dash="dash", line_color="red", annotation_text="Minimum Threshold")
        fig.update_layout(title="Model Quality Over Time", yaxis_title="Score", height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=data['date'], y=data['model_drift_score'], 
                                   fill='tozeroy', name='Drift Score'))
        fig2.add_hline(y=0.2, line_dash="dash", line_color="red", annotation_text="Alert Threshold")
        fig2.update_layout(title="Model Drift Detection", yaxis_title="Drift Score", height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Alert
    if data['model_drift_score'].iloc[-1] > 0.2:
        st.error("⚠️ ALERT: Model drift detected! Consider retraining.")
    else:
        st.success("✅ Model is stable. No significant drift detected.")

with tab2:
    st.header("Business Impact Metrics")
    
    col1, col2 = st.columns(2)
    with col1:
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=data['date'], y=data['revenue_per_session'], 
                                   name='Revenue/Session', fill='tozeroy'))
        fig3.update_layout(title="Revenue per Session (AI-Attributed)", 
                          yaxis_title="USD", height=400)
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(x=data['date'], y=data['conversion_rate']*100, name='Conversion %'))
        fig4.update_layout(title="Conversion Rate (AI vs Baseline)", 
                          yaxis_title="%", height=400)
        st.plotly_chart(fig4, use_container_width=True)
    
    # ROI Summary
    st.markdown("""
    ### Business Summary
    | Metric | Before AI | After AI | Lift |
    |--------|-----------|----------|------|
    | Revenue/Session | $3.80 | $5.12 | +35% |
    | Conversion Rate | 2.8% | 3.6% | +29% |
    | Avg Basket Size | 2.8 items | 3.4 items | +21% |
    """)

with tab3:
    st.header("User Trust Metrics")
    
    col1, col2 = st.columns(2)
    with col1:
        fig5 = go.Figure()
        fig5.add_trace(go.Scatter(x=data['date'], y=data['user_satisfaction'], name='Satisfaction'))
        fig5.add_hline(y=4.0, line_dash="dash", line_color="orange", annotation_text="Target: 4.0+")
        fig5.update_layout(title="User Satisfaction (1-5 Scale)", height=400)
        st.plotly_chart(fig5, use_container_width=True)
    
    with col2:
        fig6 = go.Figure()
        fig6.add_trace(go.Scatter(x=data['date'], y=data['override_rate']*100, name='Override Rate'))
        fig6.add_trace(go.Scatter(x=data['date'], y=data['feature_adoption']*100, name='Adoption Rate'))
        fig6.update_layout(title="Trust Indicators", yaxis_title="%", height=400)
        st.plotly_chart(fig6, use_container_width=True)
    
    st.markdown("""
    ### Trust Interpretation
    - **Override Rate** (users ignoring AI suggestions): Lower = more trust
    - **Feature Adoption** (users engaging with AI features): Higher = more trust
    - **Satisfaction**: Direct feedback score
    
    **Action Threshold:** If override rate > 20%, investigate: Is the model wrong? Or is the UX unclear?
    """)

with tab4:
    st.header("Operational Metrics")
    
    col1, col2 = st.columns(2)
    with col1:
        fig7 = go.Figure()
        fig7.add_trace(go.Scatter(x=data['date'], y=data['p95_latency_ms'], name='P95 Latency (ms)'))
        fig7.add_hline(y=250, line_dash="dash", line_color="red", annotation_text="SLA: 250ms")
        fig7.update_layout(title="Response Latency (P95)", yaxis_title="ms", height=400)
        st.plotly_chart(fig7, use_container_width=True)
    
    with col2:
        fig8 = go.Figure()
        fig8.add_trace(go.Scatter(x=data['date'], y=data['cost_per_prediction']*1000, name='Cost (mUSD)'))
        fig8.update_layout(title="Cost per Prediction", yaxis_title="milli-USD", height=400)
        st.plotly_chart(fig8, use_container_width=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.metric("Uptime (30-day)", f"{data['uptime_pct'].mean():.2f}%")
        st.metric("Predictions/Day", f"{latest['predictions_per_day']:,.0f}")
    with col4:
        monthly_cost = latest['cost_per_prediction'] * latest['predictions_per_day'] * 30
        st.metric("Monthly Infra Cost", f"${monthly_cost:,.0f}")
        st.metric("Cost per $1 Revenue", f"${monthly_cost / (latest['revenue_per_session'] * latest['predictions_per_day'] * 30):.4f}")

# Footer
st.markdown("---")
st.markdown("""
**PM's Metrics Philosophy:** AI products fail when teams track ONLY model accuracy. 
You need all 4 quadrants: Model Health + Business Impact + User Trust + Operations.
A model with 95% accuracy that users don't trust is a failed product.

*Built by Vinod Annukaran | AI Product Manager | Demonstrating AI Product Measurement*
""")
