# load_data.py
import pandas as pd
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
RAW = BASE / 'data' / 'raw'
PROC = BASE / 'data' / 'processed'
PROC.mkdir(parents=True, exist_ok=True)
def load():
    df = pd.read_csv(RAW / 'sample_health_logs.csv', parse_dates=['date'])
    df.to_csv(PROC / 'raw_loaded.csv', index=False)
    print('Loaded', df.shape)
if __name__=='__main__':
    load()
