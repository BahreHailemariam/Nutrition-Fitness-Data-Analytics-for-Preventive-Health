# 🏥 Workflow Specification — Nutrition & Fitness Data Analytics for Preventive Health

This document describes the **end-to-end data pipeline, modeling workflow, processing logic, and automation blueprint** for the Nutrition & Fitness Data Analytics for Preventive Health project.

The workflow is designed to support: <br />
✔ Preventive-health analytics <br />
✔ Personalized wellness insights <br />
✔ Machine learning–based risk prediction <br />
✔ Dashboarding in Power BI and Streamlit <br />
✔ Scalable ETL suitable for production environments

## 📌 1. Architecture Overview

**Data Sources → ETL Pipeline → Feature Store → ML Modeling → Analytics Layer → Dashboards**

```java
Mobile App / Wearables / Logs
      ↓
Raw Storage (CSV/JSON/Parquet)
      ↓
Python ETL (Cleaning + Feature Engineering)
      ↓
Processed Warehouse Tables (SQLite / DuckDB / BigQuery)
      ↓
ML Models (RandomForest, LogisticRegression)
      ↓
Analytics Metrics + Predictions Tables
      ↓
Power BI / Streamlit Dashboards

```

## 📂 2. Data Sources
**2.1 Nutrition Logs**

- daily meal entries

- calories, protein, carbs, fat

- meal_type (breakfast, lunch, snacks, etc.)

**2.2 Fitness Activity**

- steps, workout duration, calories burned

- workout_type (cardio, strength, HIIT)

- intensity score

**2.3 Sleep Tracking**

- sleep hours

- sleep quality score

- awake/restless minutes

**2.4 Biometrics**

- weight

- resting heart rate

- HRV (heart rate variability)

- stress score

**2.5 Derived Data (Feature Store)**

- net_calories

- macro % distribution

- activity_score

- sleep_score

- wellness_score (blended metric)

