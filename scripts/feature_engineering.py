# feature_engineering.py
import pandas as pd
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
PROC = BASE / 'data' / 'processed'
def fe():
    df = pd.read_csv(PROC / 'cleaned.csv', parse_dates=['date'])
    df['net_calories'] = df['calories'] - df['calories_burned']
    total = df['protein']+df['carbs']+df['fat']
    df['protein_pct'] = df['protein'] / total
    df['carb_pct'] = df['carbs'] / total
    df['fat_pct'] = df['fat'] / total
    df['sleep_score'] = (df['sleep_hours'] / 8.0).clip(0,1)
    df['activity_score'] = (df['steps'] / 10000.0).clip(0,1) * 0.6 + (df['duration_min'] / 60.0).clip(0,1) * 0.4
    df['wellness_score'] = 0.4*df['sleep_score'] + 0.35*df['activity_score'] + 0.25*(1 - (df['stress_level']/10.0))
    df.to_csv(PROC / 'features.csv', index=False)
    print('Saved features.csv')
if __name__=='__main__':
    fe()
