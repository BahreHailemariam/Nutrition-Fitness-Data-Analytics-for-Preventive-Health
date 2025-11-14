# app.py - Streamlit demo
import streamlit as st, pandas as pd, plotly.express as px
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
PROC = BASE / 'data' / 'processed'
st.set_page_config(page_title='Wellness Dashboard', layout='wide')
st.title('Nutrition & Fitness - Wellness Dashboard')
if not (PROC / 'features.csv').exists():
    st.warning('Run pipeline to generate features.csv')
else:
    df = pd.read_csv(PROC / 'features.csv', parse_dates=['date'])
    users = df['user_id'].unique().tolist()
    user = st.sidebar.selectbox('Select user', users)
    user_df = df[df['user_id']==user]
    st.metric('Latest Wellness Score', f"{user_df['wellness_score'].iloc[-1]:.2f}")
    weekly = pd.read_csv(PROC / 'weekly_metrics.csv') if (PROC / 'weekly_metrics.csv').exists() else None
    if weekly is not None:
        fig = px.line(weekly, x='week', y='wellness_score', title='Weekly Wellness Score')
        st.plotly_chart(fig)
    st.dataframe(user_df.tail(50))
