

# 🛰️ Satellite Anomaly Detector — ESA Missions

## 📌 Project Overview

This project is a full-featured anomaly detection system for ESA satellite missions. It integrates multiple data sources, explores mission-specific anomalies, builds a predictive model using XGBoost, and interprets results using SHAP. It’s designed to identify anomalous satellite behavior across three missions and provide technical insights for decision-making and future projections.

---

## 🧠 Objectives

- Analyze anomalies across ESA-Mission1, ESA-Mission2, and ESA-Mission3  
- Engineer contextual features from raw telemetry and command data  
- Build a robust detection model using machine learning (XGBoost)  
- Apply explainability techniques (SHAP) to evaluate feature importance  
- Project anomaly patterns per mission and category  
- Deploy visual dashboards and export high-level reports  

---

## 🗂️ Repository Structure

```
satellite-anomaly-detector-ESA/
├── README.md                       # Project description and documentation
├── LICENSE                         # Project license
├── requirements.txt                # Required Python packages
├── .gitignore                      # Files to exclude from Git commits

├── data/                           # Raw ESA datasets (per mission)
│   ├── ESA-Mission1/
│   ├── ESA-Mission2/
│   └── ESA-Mission3/

├── processed/                      # Cleaned and engineered dataset
│   └── features_dataset.csv

├── notebooks/                      # Jupyter notebooks for analysis
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   ├── 03_XGBoost_Model.ipynb
│   ├── 04_Global_Anomalies.ipynb
│   ├── 05_SHAP_Interpretability.ipynb
│   └── 06_Mission_Projection.ipynb

├── src/                            # Modular Python scripts
│   ├── load_data.py
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── visualize.py
│   └── project_mission.py

├── figures/                        # Exported charts and visuals
│   ├── anomalies_overlay.png
│   ├── shap_importance.png
│   ├── temporal_heatmap.gif
│   └── mission_projection.png

├── dashboards/                     # Interactive visualizations
│   ├── dashboard_powerbi.pbix
│   └── app_streamlit.py

├── assets/                         # Logos and project assets
│   └── ESA_banner.png

└── reports/                        # Technical and executive summaries
    ├── technical_summary.md
    ├── non_technical_summary.pdf
    └── mission_projection.csv
```

---

## 🚀 Highlights

- ✔️ Clean and structured preprocessing pipeline
- ✔️ XGBoost model trained on engineered features
- ✔️ SHAP plots for model transparency
- ✔️ Visualization by class, mission, and category
- ✔️ Projection engine for future mission insights
- ✔️ Dashboards in Streamlit and Power BI
- ✔️ Modular code ready for deployment

---

## 🛠️ Technologies Used

- Python 3.9  
- Pandas, NumPy, Scikit-learn  
- XGBoost, SHAP  
- Seaborn, Matplotlib  
- Streamlit, Power BI  

---

## 📊 Use Case

This pipeline is ideal for mission control teams, satellite engineers, and aerospace data analysts interested in understanding anomaly patterns and improving telemetry-based fault detection.

---

📈 Results
- The trained XGBoost model reached 86% accuracy and 83% F1 score, outperforming logistic regression and random forest benchmarks.
- SHAP interpretability confirmed that command sequences immediately preceding anomalies have significant predictive power.
- The mission-wise projection revealed distinct anomaly profiles for ESA-Mission1 vs Mission3, particularly in telemetry categories.
- Visualizations highlight class distributions, command overlaps, and temporal patterns of anomalies.
- The Streamlit dashboard allows manual anomaly submission, prediction, and interpretation in real time.

🧾 Conclusion
This ESA satellite anomaly detector demonstrates a viable architecture for proactive fault detection using interpretable machine learning. It combines telemetry, command logs, and temporal patterns to flag irregular satellite behavior. With modular design, dashboard support, and comprehensive reporting, the system is deployable and extendable for future missions. Further work may explore integration with real-time telemetry streams or expand feature engineering based on signal diagnostics and subsystem models.




## 👨‍🚀 Author

- **Juan M.G.Y.** — Data Scientist, anomaly hunter, and architect of this mission.

