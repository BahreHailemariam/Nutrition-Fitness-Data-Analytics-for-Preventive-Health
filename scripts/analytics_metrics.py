# analytics_metrics.py
import pandas as pd
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
PROC = BASE / 'data' / 'processed'
def metrics():
    df = pd.read_csv(PROC / 'features.csv', parse_dates=['date'])
    df['week'] = pd.to_datetime(df['date']).dt.to_period('W').astype(str)
    agg = df.groupby('week').agg({'wellness_score':'mean','steps':'mean','sleep_hours':'mean','net_calories':'mean'}).reset_index()
    agg.to_csv(PROC / 'weekly_metrics.csv', index=False)
    print('Saved weekly_metrics.csv')
if __name__=='__main__':
    metrics()
