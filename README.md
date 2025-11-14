# 🥗 Nutrition & Fitness Data Analytics for Preventive Health

A complete end-to-end analytics project for understanding dietary behavior, activity patterns, and early-stage health risks.
## 🌟 Project Overview

The **Nutrition & Fitness Data Analytics for Preventive Health** project analyzes dietary intake, physical activity, sleep quality, and biometric indicators to uncover patterns that contribute to long-term health outcomes.

The project provides:

- Insights into daily nutrition & workout patterns

- Predictive modeling for detecting early health risks

- A Power BI dashboard for visualizing wellness KPIs

- A full analytics pipeline (data → transformation → insights → modeling → reporting)

This project is suitable for:

- Data analysts in health & wellness

- Healthcare BI teams

- Fitness & nutrition app companies

- Academic/public health researchers

## 🎯 Objectives

✔ Identify the relationship between diet, activity, and wellness metrics<br />
✔ Detect early warning indicators for fatigue, stress, obesity risk, and poor recovery<br />
✔ Build visual dashboards for personal and population-level preventive health<br />
✔ Develop ML models that predict health risk categories<br />
✔ Provide actionable lifestyle recommendations

## 📂 Folder Structure
```
Nutrition_Fitness_Analytics/
│
├── data/
│   ├── raw/                # Raw logs (food intake, workouts, steps, biometrics)
│   └── processed/          # Cleaned datasets ready for modeling
│
├── scripts/
│   ├── load_data.py        # Load CSV/JSON data and validate structure
│   ├── clean_data.py       # Handle missing nutrition/activity fields
│   ├── feature_engineering.py  # Compute calories, macros, sleep score, etc.
│   ├── train_model.py      # ML model training for health risk prediction
│   ├── analytics_metrics.py # Wellness scoring, correlations, pattern detection
│   └── app.py              # Streamlit-based fitness + nutrition monitoring app
│
├── dashboard/
│   └── PowerBI_Report_Spec.md  # Full Power BI specification
│
├── docs/
│   └── Workflow_Spec.md    # Detailed ETL + ML workflow
│
├── models/
│   └── health_risk_model.pkl
│
├── requirements.txt
└── README.md
```


## 🧪 Data Sources (Example Schema)
**Nutrition Logs**

| Column              | Description                        |
| ------------------- | ---------------------------------- |
| date                | Entry date                         |
| food_item           | Logged meal/snack                  |
| calories            | Total calories                     |
| protein, carbs, fat | Macronutrient breakdown            |
| meal_type           | Breakfast / Lunch / Dinner / Snack |

**Fitness Logs**

| Column | Description | <br />
| steps | Daily step count | <br />
| workout_type | Cardio / Strength / Yoga / HIIT | <br />
| duration_min | Workout duration |<br />
| calories_burned | Estimated burn |

**Sleep + Biometrics**

| sleep_hours | Nighttime sleep |<br />
| heart_rate | Resting heart rate | <br />
| stress_level | Self-reported scale (0–10) | <br />
| weight | Daily/weekly weight logs |

## 🛠 Tech Stack
**Languages**

- Python (pandas, numpy, scikit-learn, seaborn, matplotlib)

- DAX (Power BI)

- SQL (for transformation queries)

**Tools**

- **Power BI** → Dashboard + KPI reporting

- **Streamlit** → Health insights web app

- **Scikit-learn** → Predictive modeling

- **Plotly** → Interactive wellness visualizations

 ## ⚙️ Workflow Summary
**1. Data Ingestion**

- Load nutrition logs, workout logs, biometrics, and sleep patterns

- Validate file structure & unify timestamps

**2. Data Cleaning**

- Fix missing calories/macros

- Normalize inconsistent units

- Remove duplicate entries

- Compute derived data (e.g., calories burned ratios)

**3. Feature Engineering**

- Daily & weekly aggregated metrics

- Macro breakdown ratios

- Workout intensity scores

- Sleep recovery score

- Stress score normalization

- Health Risk Index (HRI)

**4. Predictive Modeling**

ML algorithms:

- Logistic Regression

- Random Forest

- XGBoost (optional)

Predictions:

- Stress Risk Level

- Obesity Risk

- Fatigue / Low Energy Detection

- Overtraining Indicator

**5. Analytics & KPIs**

Calculated metrics:

- Net Calories (Calories In – Out)

- Macro Ratio Balance

- Workout Frequency Score

- Sleep Consistency Score

- Weekly Stress Index

- Hydration Consistency (if included)

**6. Visualization**

Power BI dashboard pages:

- Overview

- Nutrition Patterns

- Fitness Activity

- Health Risk Modeling

- Sleep & Recovery

- Weekly Wellness Scorecard

**7. Deployment (Optional)**

- Streamlit monitoring dashboard

- Automated pipelines using cron / Airflow 

## 📊 Power BI Dashboard Preview
### Pages Included
**1. Overview**

- Wellness score

- Steps vs sleep vs calories overview

- Weight trend

- Stress level trend

**2. Nutrition Insights**

- Calories by meal type

- Macro distribution

- Weekly calorie trends

- High-calorie food drivers

**3. Fitness Activity**

- Workout frequency & intensity

- Steps trend

- Calories burned analysis

- Workout category comparison

**4. Sleep & Recovery**

- Sleep quality trend

- Heart rate & stress correlation

- Recovery score (HRV proxy)

**5. Health Risk Modeling**

- Predicted risk categories

- Feature importance (model insights)

- Comparison with ground truth factors

**6. Weekly Wellness Scorecard**

- Combined KPIs

- Personalized recommendations

