import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Shopper Spectrum Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GLOBAL STYLING ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    color: #e6e6e6;
    background-color: #0f0f12;
}

/* Gradient only for specific texts */
h1, h2, h3, h4, h5, h6, .gradient-text {
    background: linear-gradient(135deg, #00C9FF, #92FE9D);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-weight: 600;
}

/* Make tabs readable */
.stTabs [data-baseweb="tab"] {
    color: #e6e6e6 !important;
    font-weight: 500;
}



/* Gradient buttons */
.stButton>button {
    background: linear-gradient(135deg, #00C9FF, #92FE9D);
    color: #000;
    border: none;
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.3s ease-in-out;
}

.stButton>button:hover {
    opacity: 0.9;
    transform: scale(1.03);
}

/* Input boxes for clarity */
.stNumberInput input, .stTextInput input {
    background-color: #1b1b1f;
    color: #e6e6e6;
    border-radius: 8px;
    border: 1px solid #333;
}
</style>
""", unsafe_allow_html=True)


# --- SIDEBAR ---
with st.sidebar:
    st.title("🛍️ Shopper's Spectrum")
    st.write("An interactive dashboard for:")  
    st.markdown("- Customer Segmentation (RFM)\n- Product Recommendation")
    st.write("---")
    st.write("Developed by **thejj_theju**")

# --- LOAD DATA ---
rfm = pd.read_csv("C:/Users/Ajay/Desktop/Python/shopper Project/rfm.csv")
sim_df = joblib.load("C:/Users/Ajay/Desktop/Python/shopper Project/item_similarity_matrix.joblib")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["Customer Segmentation", "Product Recommendation", "Summary & Visualizations"])

# --- TAB 1 ---
with tab1:
    st.header("Customer Segment Predictor")
    recency = st.number_input('Recency (days since last purchase)', min_value=0, step=3, value=0)
    frequency = st.number_input('Frequency (number of purchases)', min_value=0, step=2, value=0)
    monetary = st.number_input('Monetary (total spend)', min_value=0.0, step=1000.00, format="%.2f", value=0.0)

    if st.button('Predict Segment'):
        scaler = joblib.load("C:/Users/Ajay/Desktop/Python/shopper Project/scaler.pkl")
        kmeans_model = joblib.load("C:/Users/Ajay/Desktop/Python/shopper Project/kmeans_final.pkl")
        features = np.array([[recency, frequency, monetary]])
        features_scaled = scaler.transform(features)
        cluster_idx = kmeans_model.predict(features_scaled)[0]
        label_map = {
            0: 'Occasional',
            1: 'At-Risk / Dormant',
            2: 'High-Value / Champions',
            3: 'Loyal / Regular'
        }
        segment = label_map.get(cluster_idx, 'Unknown')

        if segment == 'High-Value / Champions':
            st.success(f"🔥 Predicted Segment: **{segment}**")
        elif segment == 'At-Risk / Dormant':
            st.warning(f"⚠️ Predicted Segment: **{segment}**")
        else:
            st.info(f"✅ Predicted Segment: **{segment}**")

# --- TAB 2 ---
with tab2:
    st.header("Product Recommendation Engine")
    prod_name = st.text_input('Enter product name (exact description)')
    if st.button('Get Recommendations'):
        if prod_name not in sim_df.index:
            st.error("❌ Product not found. Please check spelling or try another product.")
        else:
            sims = sim_df[prod_name].sort_values(ascending=False)
            top5 = sims.index[1:6]
            st.write("**Top 5 similar products:**")
            for i, p in enumerate(top5, 1):
                st.write(f"{i}. {p}")

# --- TAB 3 ---
with tab3:
    df = pd.read_csv("C:/Users/Ajay/Desktop/Python/shopper Project/df.csv", parse_dates=['InvoiceDate'])
    df['Month'] = df['InvoiceDate'].dt.to_period('M').astype(str)

    st.markdown("""
    <style>
      .stat-card {
        background: linear-gradient(135deg, #00C9FF, #92FE9D);
        color: white;
        text-align: center;
        border-radius: 11px;
        padding: 12px 10px;
        margin: 8px 0;
        box-shadow: 0 2px 6px rgba(0,0,0,0.12);
      }
      .stat-card .stat-value {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 4px;
      }
      .stat-card .stat-label {
        font-size: 12px;
        letter-spacing: 1px;
      }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    #with st.expander("📆 Show Date Range"):
     #s   st.write("**Date covered:** 2022-12-01 to 2023-12-09")
    with col1:
        st.markdown('<div class="stat-card"><div class="stat-value">4,338</div><div class="stat-label">Total Customers</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><div class="stat-value">3,665</div><div class="stat-label">Total Products</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><div class="stat-value">18,532</div><div class="stat-label">Total Transactions</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-card"><div class="stat-value">₹ 8,887,208</div><div class="stat-label">Total Revenue</div></div>', unsafe_allow_html=True)


  #  st.write("**Date covered:** 2022-12-01 08:26:00 to 2023-12-09 12:50:00")
    st.write("---")

    option = st.selectbox(
        "Select visualisation to display",
        [
            "Month-wise Revenue",
            "Segment-wise Customer Count",
            "Top 10 Products on Sale",
            "Top 5 Countries by Revenue",
            "Top 5 High-Value Customers"
        ]
    )

    if option == "Month-wise Revenue":
        monthly_rev = df.groupby('Month')['Revenue'].sum().reset_index()
        fig = px.line(monthly_rev, x='Month', y='Revenue', title="Revenue by Month", markers=True)
        st.plotly_chart(fig, use_container_width=True)

    elif option == "Segment-wise Customer Count":
        seg_count = rfm.groupby('Segment')['CustomerID'].nunique().reset_index()
        fig = px.bar(seg_count, x='Segment', y='CustomerID', title="Customer Count by Segment", color='Segment')
        st.plotly_chart(fig, use_container_width=True)

    elif option == "Top 10 Products on Sale":
        prod_rev = df.groupby('Description')['Revenue'].sum().reset_index().sort_values(by='Revenue', ascending=False).head(10)
        fig = px.bar(prod_rev, x='Revenue', y='Description', orientation='h', title="Top 10 Products by Revenue")
        fig.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

    elif option == "Top 5 Countries by Revenue":
        country_rev = df.groupby('Country')['Revenue'].sum().reset_index().sort_values(by='Revenue', ascending=False).head(5)
        fig = px.bar(country_rev, x='Country', y='Revenue', title="Top 5 Countries by Revenue", color='Country')
        st.plotly_chart(fig, use_container_width=True)

    elif option == "Top 5 High-Value Customers":
        cust_rev = df.groupby('CustomerID')['Revenue'].sum().reset_index()
        top_customers = cust_rev.sort_values(by='Revenue', ascending=False).head(5)
        top_customers['CustomerID'] = top_customers['CustomerID'].astype(str)
        fig = px.bar(top_customers,x='CustomerID', y='Revenue', color='Revenue', color_continuous_scale='Blues', title='Top 5 High-Value Customers')
        fig.update_layout( xaxis_title='Customer ID',yaxis_title='Revenue',template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)



    st.write("---")

