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

