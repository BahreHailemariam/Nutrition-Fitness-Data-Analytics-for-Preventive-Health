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

**Notes:** Compute SHAP or feature contributions offline and save to a `ModelExplainer` table for in-report visualizations.

## 6️⃣ Weekly Wellness Scorecard

**Goal:** Compact weekly summary for coaches and users.

**KPIs & Visuals:**

- Weekly Avg Wellness Score (trend line)

- Weekly Steps, Sleep, Net Calories (bar or line)

- User scorecard with suggestions (Power BI conditional text or button linking to recommendations)

- Table: Top improvement recommendations per user (precomputed rules)

**DAX Examples:**
```DAX

WeeklyWellness = 
AVERAGEX(
  VALUES(Date[week]),
  CALCULATE(AVERAGE(Features[wellness_score]))
)

```

## 7️⃣ Anomaly & Trends

**Goal:** Detect sudden deviations (e.g., sharp drops in wellness or spikes in stress).

**Triggers & Visuals:**

- Alerts tile: list of anomalies (e.g., wellness drop > 15% week-over-week).

- Line + anomaly markers: wellness trend with flagged dates.

- Word cloud or keyword heatmap for textual journal entries (if available) around anomaly windows.

**DAX Example (simple drop detection):**

```DAX

Wellness_WoW_Change =
DIVIDE(
  [AvgWellness] - CALCULATE([AvgWellness], DATEADD(Date[date], -7, DAY)),
  CALCULATE([AvgWellness], DATEADD(Date[date], -7, DAY))
)

```

## 📦 Data Model Recommendations

- Use a star schema:

     - Central fact tables: `NutritionFact`, `ActivityFact`, `SleepFact`, `BiometricsFact`, `FeaturesFact`, `PredictionsFact`

     - Dimension tables: `Date`, `User`, `MealType`, `WorkoutType`, `Location` (if available)

- Pre-aggregate daily KPIs into a `DailyMetrics` table for heavy visuals.

- Store model artifacts/SHAP outputs as separate tables for the Risk Modeling page.

- Prefer numeric surrogate keys for joins; avoid text-only joins in visuals.

## ♻️ Refresh & Performance

- **Recommended refresh cadence:** Daily for historical pipelines; near-real-time (hourly) if feeding from streaming sources. For demo/local, schedule every 15–60 minutes.

- **DirectQuery vs Import:** Import for smaller datasets for best performance. Use DirectQuery for very large datasets or when using a dedicated warehouse (BigQuery / Snowflake).

- **Performance tips:**

     - Use pre-aggregated tables for visuals that span long time windows.

     - Limit top N visuals and use slicers to reduce cardinality.

     - Optimize DAX measures (prefer measures over calculated columns when dynamic).

## 🔐 Security & Deployment

- Implement **Row-Level Security (RLS)** to limit users to their own data (user_id-based filters) — especially important for health data.

- Use Power BI Service for scheduled refresh and data alerts.

- Consider data anonymization or hashing of PII before uploading to Power BI.

## 🧩 UX & Interaction Guidelines

- Global filter bar: `Date Range`, `User`, `Cohort`, `MealType`, `WorkoutType`.

- Drill-through: Allow drill-through from weekly summary to daily entries and to individual raw reviews/notes.

- Bookmarks: Create “Executive Summary”, “Coach View”, and “User View” bookmarks for quick access.

- Mobile layout: a condensed card-only page (Wellness Score + Top 3 KPIs).

 ## 🧪 Validation & QA

- Validate DAX measures with SQL queries against the source tables.

- Unit-test sample measures with known labels (e.g., user with static values).

- Verify model predictions by comparing Power BI aggregates to an offline test harness CSV. 

## ⚙️ Optional Advanced Extensions

- **Forecasting:** Add short-term forecasting (Prophet / Azure ML) for weight and wellness trends.

- **Anomaly Detection:** Use rolling z-score or ML anomaly detection and surface results in Alerts page.

- **Personalized Recommendations:** Embed precomputed suggestions (nutrition/workout changes) and surface them in the Weekly Scorecard.

- **Integration:** Power Automate → send alerts/notifications to coach or user when risk thresholds are met.

- **Embedded Analytics:** Use Power BI Embedded for in-app dashboards (if product integrates with a mobile app).


## ✅ Implementation Checklist

 - Confirm source table/field names and types.

 - Create Date and User dimension tables.

 - Build Power Query transformations to import and clean tables reliably.

 - Precompute daily metrics table where appropriate.

 - Implement DAX measures and validate against SQL.

 - Configure scheduled refresh (Power BI Service) and data-driven alerts.

 - Implement RLS for user-based data security.

 - Publish and test mobile layout and bookmarks.

