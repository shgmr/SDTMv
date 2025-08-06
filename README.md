## 📊 SDTM Metrics Interactive Dashboard Project Overview
When working with CDISC SDTM (Study Data Tabulation Model) databases, the goal of metric visualization is often to support clinical trial data review, quality control, and regulatory submission readiness. Here are several useful types of visualizations you can create, depending on the domain and the kind of insights you're looking for:

📄 database [a relative link](Survival.csv)
📄 database [a relative link](ae.csv)
📄 database [a relative link](lb.csv)
---

## 📷 Sample Visualizations

Visual sample [a relative link](SDTM Metrics Interactive Dashboard Snapshot.pdf)

## 📌 Key Insights
### 🔍 Why Use Kaplan-Meier for Time to First AE?
Kaplan-Meier (KM) analysis estimates the probability of survival (or remaining event-free) over time. In the context of AEs:
"Survival" means not having an AE yet.
"Event" is the first occurrence of an AE.
Censoring applies if a subject never experiences an AE during the study period.

### ✅ Why AE Over Time Visuals Are Valuable
1. Temporal Insight
Shows when AEs occur during the study.
Helps identify clusters or spikes in AE frequency (e.g., around certain visits or treatment phases).
2. Severity Stratification
Stratifying by severity (Mild, Moderate, Severe) highlights the risk profile over time.
Useful for assessing tolerability of treatment.

### 📈 Time-Series Plots of ALT and AST per Subject
1. Trend Monitoring
Track fluctuations in liver enzymes over time.
Detect abnormal spikes or gradual increases that may indicate liver stress or injury.
2. Individualized Assessment
Per-subject plots allow personalized safety monitoring.
Useful for identifying outliers or subjects needing further evaluation.
---

## 🚀 How to Run

Code sample [a relative link](dadhboard.py)
