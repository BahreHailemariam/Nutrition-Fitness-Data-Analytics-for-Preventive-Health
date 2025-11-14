# train_model.py
import pandas as pd, joblib
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
BASE = Path(__file__).resolve().parents[1]
PROC = BASE / 'data' / 'processed'
MODELS = BASE / 'models'
MODELS.mkdir(parents=True, exist_ok=True)
def train():
    df = pd.read_csv(PROC / 'features.csv')
    df['fatigue_risk'] = (df['wellness_score'] < 0.4).astype(int)
    features = ['net_calories','protein_pct','carb_pct','fat_pct','sleep_score','activity_score','wellness_score']
    X = df[features].fillna(0)
    y = df['fatigue_risk']
    if len(df) < 5:
        print('Not enough rows to train in demo.')
        return
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train, y_train)
    joblib.dump(clf, MODELS / 'health_risk_model.pkl')
    print('Trained and saved model.')
if __name__=='__main__':
    train()
