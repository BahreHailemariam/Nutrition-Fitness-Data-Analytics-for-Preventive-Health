# 📊 Power BI Report Specification — Nutrition & Fitness Data Analytics (Preventive Health)

**Purpose:** Provide operational and clinical teams with interactive, actionable dashboards that combine nutrition logs, activity, sleep, and biometrics into preventive-health KPIs and model-driven risk indicators.

**Primary Users:** Health analysts, clinicians, product managers for wellness apps, data scientists.

## 📁 Report Structure (Pages)

**1. Overview**— Executive summary & wellness snapshot

**2. Nutrition Insights** — Meal-level and macro analytics

**3. Fitness Activity** — Steps, workouts, intensity, and energy balance

**4. Sleep & Recovery** — Sleep quality, HR trends, recovery indicators

**5. Health Risk Modeling** — Predicted risk categories and model explainability

**6. Weekly Wellness Scorecard** — Aggregated weekly KPIs & recommendations

**7. Anomaly & Trends** — Sudden deviations and cohort trends

## 🔑 Key Data Sources / Tables

- `Nutrition` (date, user_id, food_item, calories, protein, carbs, fat, meal_type)

- `Activity` (date, user_id, steps, workout_type, duration_min, calories_burned)

- `Sleep `(date, user_id, sleep_hours, sleep_quality_score, awake_minutes)

- `Biometrics` (date, user_id, weight, resting_hr, hr_variability, stress_level)

- `Features` (derived features: net_calories, protein_pct, activity_score, sleep_score, wellness_score)

- `ModelPredictions` (date, user_id, fatigue_risk, obesity_risk, prediction_probabilities)

- `Date dimension` (date, year, month, week, weekday)

Preferably stored in a data warehouse or as refreshable CSV/Parquet for Power BI.
