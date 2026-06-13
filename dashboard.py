import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title="NayePankh Foundation Dashboard", layout="wide", page_icon="🕊️")

@st.cache_data
def load_data():
    if not os.path.exists('data/nayepankh_data_12_months.csv'):
        st.warning("Data file not found. Please run `generate_data.py` first.")
        return pd.DataFrame()
    return pd.read_csv('data/nayepankh_data_12_months.csv')

df = load_data()

if not df.empty:
    st.title("🕊️ NayePankh Foundation - Analytics Dashboard")
    st.markdown("Monitor social media engagement, website traffic, and donation metrics for the NayePankh Foundation.")

    # Sidebar Filters
    st.sidebar.header("Filter Options")
    selected_month = st.sidebar.selectbox("Select Month", options=["All Time"] + df['Month'].tolist())

    if selected_month != "All Time":
        filtered_df = df[df['Month'] == selected_month]
    else:
        filtered_df = df

    # KPI Cards
    st.subheader("Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)

    total_donations = filtered_df['Total_Donations_INR'].sum()
    total_donors = filtered_df['Unique_Donors'].sum()
    total_traffic = filtered_df['Website_Traffic_Page_Views'].sum()
    avg_insta_eng = filtered_df['Instagram_Engagement_Rate'].mean()

    col1.metric("Total Donations Raised", f"₹{total_donations:,.0f}")
    col2.metric("Unique Donors", f"{total_donors:,}")
    col3.metric("Website Page Views", f"{total_traffic:,}")
    col4.metric("Avg Insta Engagement", f"{avg_insta_eng:.2f}%")

    st.markdown("---")

    # Visualizations
    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader("Donations vs Website Traffic")
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=df['Month'], y=df['Total_Donations_INR'], name='Donations (INR)', marker_color='#2E8B57'))
        fig1.add_trace(go.Scatter(x=df['Month'], y=df['Website_Traffic_Page_Views'], name='Page Views', yaxis='y2', line=dict(color='#4682B4', width=3)))
        fig1.update_layout(
            yaxis2=dict(title='Page Views', overlaying='y', side='right'),
            yaxis=dict(title='Donations (INR)'),
            legend=dict(x=0.01, y=0.99),
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col_chart2:
        st.subheader("Platform Engagement Rates Over Time")
        eng_df = df[['Month', 'Instagram_Engagement_Rate', 'LinkedIn_Engagement_Rate', 'Facebook_Engagement_Rate', 'X_Engagement_Rate']]
        eng_df = eng_df.melt(id_vars='Month', var_name='Platform', value_name='Engagement Rate')
        eng_df['Platform'] = eng_df['Platform'].str.replace('_Engagement_Rate', '')
        
        fig2 = px.line(eng_df, x='Month', y='Engagement Rate', color='Platform', markers=True, color_discrete_sequence=px.colors.qualitative.Bold)
        st.plotly_chart(fig2, use_container_width=True)

    # Data Table View
    st.subheader("Raw Data View")
    st.dataframe(filtered_df.style.format({
        "Total_Donations_INR": "₹{:,.2f}",
        "Instagram_Engagement_Rate": "{:.2f}%",
        "LinkedIn_Engagement_Rate": "{:.2f}%"
    }), use_container_width=True)
