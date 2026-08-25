# 🐟 Fish Species Analysis Project

Welcome to the **Fish Species Analysis Project** — a multi-tool exploration of global fish traits using data from **FishBase**. This repository showcases end-to-end skills in data wrangling, visualization, statistical modeling, machine learning, and dashboarding using **R, Python, SQL, Streamlit, and Tableau**.

---

## 🔍 Overview

Ecological and biological data, courtesy of FishBase, is leveraged to analyze species traits (habitat, weight, length, vulnerability, etc.) to reveal patterns in morphology, conservation status, and predictive physical growth metrics.

---

## 💻 Tech Stack & Module Workflow

### 1. **R (`r_scripts/`)**
- **Data Ingestion**: Extracted raw species traits via the `rfishbase` API package.
- **Wrangling & Cleaning**: Applied `dplyr`, `tidyr`, and `magrittr` workflows for missing value imputation and feature engineering.
- **Exploratory Graphics**: Built initial diagnostic visualizations using `ggplot2`.
- **Baseline Modeling**: Implemented linear regression (`lm`) for preliminary weight-length scaling baseline checks.

### 2. **SQL (`sql/`)**
- **Relational Schema**: Structured and populated a SQLite database (`fish_species_project.db`).
- **Data Modeling**: Formatted clean trait tables (`fish_species_traits`) and created structured views joining actual traits, predictions, and model residuals.

### 3. **Python & Machine Learning (`python-analysis/`)**
- **Exploratory Data Analysis**: Deep-dive analysis with `pandas`, `matplotlib`, `seaborn`, and interactive `plotly` charts.
- **Statistical Modeling**: Evaluated feature coefficients and multicollinearity using Ordinary Least Squares (`statsmodels`).
- **Machine Learning**: Built Linear Regression models with 5-Fold Cross-Validation, reporting evaluation metrics ($R^2 = 0.625$, $\text{MAE} = 11.07$, $\text{RMSE} = 35.02$).
- **Interactive Web App**: Built a local **Streamlit** interactive dashboard (`app.py`) for live metric filtering and prediction exploration.

### 4. **Tableau Analytics (`tableau/`)**
- **Data Export**: Generated `tableau_fish_traits.csv` (96,276 records) merging traits, actuals, predictions, and errors.
- **Interactive Dashboard**: Configured interactive worksheets for global morphology exploration, environmental vulnerability matrix heatmaps, and ML residual analysis.

---

## 📊 Sample Visualizations & Views

### 👀 Model Prediction Summary View

This CSV summary compares actual vs. predicted fish lengths, including model error and taxonomic information:

| actual_length | predicted_length | error | Genus | Species |
|---|---|---|---|---|
| 3.0 | 8.23 | 5.23 | Aapticheilichthys | Aapticheilichthys websteri |
| 130.0 | 157.60 | 27.60 | Aaptosyax | Aaptosyax grypus |
| 11.5 | 8.23 | -3.27 | Abactochromis | Abactochromis labrosus |
| 32.5 | 42.22 | 9.72 | Abalistes | Abalistes filamentosus |
| 60.0 | 73.31 | 13.31 | Abalistes | Abalistes stellatus |

---

## 🚀 How to Run the Project

1. **Python Streamlit Dashboard**:
   ```bash
   cd python
   streamlit run app.py
