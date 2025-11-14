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

## 1️⃣ Overview

**Goal:** High-level summary for executives — overall population wellness, trends, and top risk flags.

**KPIs (cards):**

- **Avg Wellness Score** — average of `wellness_score` across selected users/time.

- **% At-Risk (Fatigue)** — proportion with `fatigue_risk = 1`.

- **Avg Daily Steps** — mean steps per day.

- **Avg Sleep Hours** — mean sleep_hours.

- **Weight Trend** — delta in average weight vs prior period.

**Visuals:**

- KPI cards across top ribbon.

- Line chart: Avg Wellness Score trend (date).

- Bar chart: Distribution of Wellness Score buckets (0–1).

- Top 5 risk drivers table (feature importance from model).

- Small map or cohort breakdown (if geo available).

**DAX Examples:**
```DAX
AvgWellness = AVERAGE(Features[wellness_score])

PctFatigueRisk = 
DIVIDE(
  COUNTROWS(FILTER(ModelPredictions, ModelPredictions[fatigue_risk] = 1)),
  COUNTROWS(ModelPredictions)
)

AvgDailySteps = AVERAGE(Activity[steps])
```

## 2️⃣ Nutrition Insights

**Goal:** Understand calorie intake, macro balance, and high-impact foods.

**KPIs:**

- **Avg Daily Calories (per user)**

- **Macro Balance (Protein %, Carb %, Fat %)**

- **Top High-Calorie Foods** (by average calories)

**Visuals:**

- Stacked area: Daily calories (in vs burned) per cohort.

- Treemap: Top food items by calories or frequency.

- Bar chart: Macro composition by meal_type.

- Table: Users with highest net calorie surplus.

**DAX Examples:**
```DAX

DailyCalories = SUM(Nutrition[calories])

NetCalories = SUM(Features[net_calories])

ProteinPct = DIVIDE(SUM(Nutrition[protein]), SUM(Nutrition[protein] + Nutrition[carbs] + Nutrition[fat]))

```
**Interactions:** Clicking an SKU/food filters Wellness and Activity pages to show downstream effects.

## 3️⃣ Fitness Activity

**Goal:** Measure activity volume & intensity and its effect on wellness.

**KPIs:**

- **Avg Steps per Day**

- **Workout Frequency (sessions per week)**

- **Avg Calories Burned per Workout**

**Visuals:**

- Heatmap: Steps by day-of-week vs hour (if timestamps available).

- Bar chart: Workout types by frequency & avg duration.

- Scatter: Activity Score vs Wellness Score (per user).

**DAX Examples:**

```DAX
WorkoutCount = COUNTROWS(Activity)

AvgCaloriesBurned = AVERAGE(Activity[calories_burned])

WorkoutFrequencyPerWeek = 
DIVIDE(
  COUNTROWS(Activity),
  DISTINCTCOUNT(Date[week])
)
```

## 4️⃣ Sleep & Recovery

**Goal:** Monitor sleep patterns, correlate sleep to wellness and risk.

**KPIs:**

- **Avg Sleep Hours**

- **Avg Sleep Score** (derived)

- **Resting HR trend**

**Visuals:**

- Line chart: Sleep hours trend (user or cohort).

- Box plot: Sleep distribution across users.

- Correlation matrix: Sleep Score vs Wellness Score vs Steps.

**DAX Examples:**
```DAX

AvgSleepHours = AVERAGE(Sleep[sleep_hours])

AvgSleepScore = AVERAGE(Features[sleep_score])

```

## 5️⃣ Health Risk Modeling

**Goal:** Present model predictions (e.g., fatigue risk), calibration, and explainability.

**Contents / Visuals:**

- **Risk Distribution:** Histogram of prediction probabilities per risk label.

- **Cohort Drill-Down:** Top N users flagged as high risk with recent metrics.

- **SHAP / Feature Importance:** Bar chart of most influential features for model predictions (pre-computed and exported as table).

- **Confusion Matrix & Performance:** Show precision/recall if labeled test data available.

- **Threshold Controls:** What-if slider to adjust decision threshold and view count of flagged users.

**DAX Examples:**

```DAX

AvgFatigueProb = AVERAGE(ModelPredictions[fatigue_probability])

FatigueRiskCount = COUNTROWS(FILTER(ModelPredictions, ModelPredictions[fatigue_probability] >= 0.7))

```
