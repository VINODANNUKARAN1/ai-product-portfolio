"""
AI-Powered Customer Intelligence Platform
Built by Vinod Kunhi Krishnan Annukaran

Purpose: Demonstrate how a PM bridges data science and business strategy.
Key Differentiator: Goes from raw data → segments → ACTIONABLE BUSINESS RECOMMENDATIONS
(Most data scientists stop at segments. PMs ask "So what do we DO with them?")
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.graph_objects as go

# Page Config
st.set_page_config(page_title="Customer Intelligence Platform", page_icon="🎯", layout="wide")

st.title("🎯 AI-Powered Customer Intelligence Platform")
st.markdown("""
**Business Problem:** Companies have millions of customers but treat them identically. 
Personalized strategy per segment increases revenue by 15-30%.

**What this does:** Raw transaction data → ML clustering → Business strategy per segment
""")

@st.cache_data
def generate_sample_data(n_customers=1000):
    """Generate realistic e-commerce customer data for demo."""
    np.random.seed(42)
    
    data = pd.DataFrame({
        'CustomerID': range(1, n_customers + 1),
        'Recency': np.random.exponential(30, n_customers).astype(int),  # Days since last purchase
        'Frequency': np.random.poisson(5, n_customers) + 1,  # Number of purchases
        'Monetary': np.random.lognormal(4, 1.2, n_customers).round(2),  # Total spend
        'AvgOrderValue': np.random.lognormal(3, 0.8, n_customers).round(2),
        'DaysSinceFirstPurchase': np.random.uniform(30, 730, n_customers).astype(int),
    })
    
    # Add some business-realistic patterns
    data['Monetary'] = data['Monetary'] * data['Frequency'] * 0.3
    data['AvgOrderValue'] = data['Monetary'] / data['Frequency']
    
    return data

@st.cache_data
def perform_segmentation(data, n_clusters=5):
    """RFM-based K-Means clustering with business interpretation."""
    features = ['Recency', 'Frequency', 'Monetary']
    X = data[features].copy()
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    data['Segment'] = kmeans.fit_predict(X_scaled)
    
    # Assign business-friendly segment names based on characteristics
    segment_means = data.groupby('Segment')[features].mean()
    
    # Name segments by characteristics
    segment_names = {}
    for seg in range(n_clusters):
        r = segment_means.loc[seg, 'Recency']
        f = segment_means.loc[seg, 'Frequency']
        m = segment_means.loc[seg, 'Monetary']
        
        if m > segment_means['Monetary'].quantile(0.7) and f > segment_means['Frequency'].quantile(0.6):
            segment_names[seg] = "💎 Champions"
        elif r < segment_means['Recency'].quantile(0.3) and f > segment_means['Frequency'].median():
            segment_names[seg] = "🌟 Loyal Customers"
        elif r < segment_means['Recency'].quantile(0.4):
            segment_names[seg] = "🆕 Recent Buyers"
        elif r > segment_means['Recency'].quantile(0.7):
            segment_names[seg] = "⚠️ At Risk"
        else:
            segment_names[seg] = "😴 Need Attention"
    
    data['SegmentName'] = data['Segment'].map(segment_names)
    
    return data, kmeans, scaler

# Generate data
data = generate_sample_data()

# Sidebar
with st.sidebar:
    st.header("⚙️ Model Configuration")
    n_clusters = st.slider("Number of Segments", 3, 8, 5)
    st.divider()
    st.header("📊 Data Summary")
    st.metric("Total Customers", f"{len(data):,}")
    st.metric("Total Revenue", f"${data['Monetary'].sum():,.0f}")
    st.metric("Avg Order Value", f"${data['AvgOrderValue'].mean():.2f}")

# Perform segmentation
segmented_data, model, scaler = perform_segmentation(data, n_clusters)

# Tab Layout
tab1, tab2, tab3, tab4 = st.tabs(["📊 Segment Overview", "🔍 Deep Dive", "💡 Recommendations", "🧠 PM Decisions"])

with tab1:
    st.header("Customer Segments")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 3D Scatter Plot
        fig = px.scatter_3d(
            segmented_data, x='Recency', y='Frequency', z='Monetary',
            color='SegmentName', title="Customer Segments (RFM Space)",
            labels={'Recency': 'Recency (days)', 'Frequency': 'Orders', 'Monetary': 'Total Spend ($)'}
        )
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Segment Distribution
        segment_counts = segmented_data['SegmentName'].value_counts()
        fig2 = px.pie(values=segment_counts.values, names=segment_counts.index,
                      title="Segment Distribution")
        fig2.update_layout(height=500)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Segment Summary Table
    st.subheader("Segment Statistics")
    summary = segmented_data.groupby('SegmentName').agg({
        'CustomerID': 'count',
        'Recency': 'mean',
        'Frequency': 'mean',
        'Monetary': ['mean', 'sum']
    }).round(1)
    summary.columns = ['Count', 'Avg Recency (days)', 'Avg Frequency', 'Avg Spend ($)', 'Total Revenue ($)']
    summary['% of Customers'] = (summary['Count'] / len(segmented_data) * 100).round(1)
    summary['% of Revenue'] = (summary['Total Revenue ($)'] / summary['Total Revenue ($)'].sum() * 100).round(1)
    st.dataframe(summary, use_container_width=True)

with tab2:
    st.header("Segment Deep Dive")
    selected_segment = st.selectbox("Select Segment:", segmented_data['SegmentName'].unique())
    
    segment_data = segmented_data[segmented_data['SegmentName'] == selected_segment]
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Customers", len(segment_data))
    col2.metric("Avg Recency", f"{segment_data['Recency'].mean():.0f} days")
    col3.metric("Avg Frequency", f"{segment_data['Frequency'].mean():.1f} orders")
    col4.metric("Avg Spend", f"${segment_data['Monetary'].mean():.0f}")
    
    fig3 = px.histogram(segment_data, x='Monetary', nbins=30, 
                        title=f"Spend Distribution: {selected_segment}")
    st.plotly_chart(fig3, use_container_width=True)

with tab3:
    st.header("💡 AI-Generated Business Recommendations")
    st.markdown("*A PM's job: Turn data segments into ACTIONABLE strategy*")
    
    recommendations = {
        "💎 Champions": {
            "strategy": "RETAIN & REWARD",
            "actions": [
                "Launch exclusive loyalty program with early access to new products",
                "Assign dedicated account manager for top 50 champions",
                "Offer referral bonuses (they're your best advocates)",
                "Invite to VIP events and product feedback sessions"
            ],
            "budget": "20% of marketing budget",
            "expected_roi": "3x (retention is 5x cheaper than acquisition)"
        },
        "🌟 Loyal Customers": {
            "strategy": "UPSELL & CROSS-SELL",
            "actions": [
                "Recommend premium/higher-tier products",
                "Bundle offers based on purchase history",
                "Birthday/anniversary personalized offers",
                "Loyalty tier progression notifications"
            ],
            "budget": "25% of marketing budget",
            "expected_roi": "2.5x (high conversion probability)"
        },
        "🆕 Recent Buyers": {
            "strategy": "NURTURE & CONVERT",
            "actions": [
                "Welcome series email (5 touchpoints in 30 days)",
                "Second-purchase incentive within 14 days",
                "Product education content",
                "Request review after first purchase"
            ],
            "budget": "20% of marketing budget",
            "expected_roi": "2x (convert to loyal before they churn)"
        },
        "⚠️ At Risk": {
            "strategy": "WIN-BACK (Urgent!)",
            "actions": [
                "Triggered re-activation email: 'We miss you' + 15% off",
                "SMS reminder of abandoned cart or wishlist items",
                "Survey: 'What can we do better?'",
                "Time-limited offer (creates urgency)"
            ],
            "budget": "20% of marketing budget",
            "expected_roi": "1.5x (some will churn regardless — that's okay)"
        },
        "😴 Need Attention": {
            "strategy": "ACTIVATE OR SUNSET",
            "actions": [
                "One final re-engagement campaign",
                "Dramatically different channel (if email didn't work, try SMS/push)",
                "Ask: 'Are you still interested?' (clean your list)",
                "If no response in 30 days: move to inactive (save marketing spend)"
            ],
            "budget": "15% of marketing budget",
            "expected_roi": "0.8x (accept some loss — focus budget elsewhere)"
        }
    }
    
    for segment_name, rec in recommendations.items():
        with st.expander(f"{segment_name} — Strategy: {rec['strategy']}"):
            st.markdown(f"**Budget Allocation:** {rec['budget']}")
            st.markdown(f"**Expected ROI:** {rec['expected_roi']}")
            st.markdown("**Specific Actions:**")
            for action in rec['actions']:
                st.markdown(f"- {action}")

with tab4:
    st.header("🧠 Product Manager's Decision Log")
    st.markdown("""
    ### Why K-Means over other algorithms?
    | Considered | Pros | Cons | Decision |
    |-----------|------|------|----------|
    | K-Means | Fast, interpretable, scales to millions | Assumes spherical clusters | ✅ CHOSEN: Business needs interpretability over perfection |
    | DBSCAN | Finds arbitrary shapes | Hard to explain to stakeholders | ❌ Rejected |
    | Hierarchical | Beautiful dendrograms | Doesn't scale past 10K customers | ❌ Rejected |
    | Gaussian Mixture | Soft clustering (probability) | Over-engineering for MVP | ❌ Rejected for V1 |
    
    ### Why RFM Features?
    - **Recency:** Most predictive of future behavior (recent = likely to buy again)
    - **Frequency:** Shows loyalty/habit formation
    - **Monetary:** Shows value to the business
    - These 3 features capture 80% of customer behavior variance in e-commerce
    
    ### What would V2 include?
    - Real-time clustering (as new transactions arrive)
    - Predictive churn probability per customer
    - A/B testing different strategies per segment
    - Integration with marketing automation (trigger campaigns automatically)
    - LLM-generated personalized messages per segment
    """)

# Footer
st.markdown("---")
st.markdown("*Built by Vinod Annukaran | AI Product Manager | [GitHub](https://github.com/your-username)*")
