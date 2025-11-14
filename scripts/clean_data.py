# clean_data.py
import pandas as pd
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
PROC = BASE / 'data' / 'processed'
def clean():
    df = pd.read_csv(PROC / 'raw_loaded.csv', parse_dates=['date'])
    df = df.drop_duplicates()
    for c in ['calories','protein','carbs','fat','steps','calories_burned','sleep_hours','heart_rate','stress_level','weight']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce').fillna(df[c].median())
    df.to_csv(PROC / 'cleaned.csv', index=False)
    print('Saved cleaned.csv')
if __name__=='__main__':
    clean()
