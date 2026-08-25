# Tableau Visualization Architecture

## Overview
This directory contains the cleaned dataset (`tableau_fish_traits.csv`) generated from our SQLite database and Python pipeline, as well as the design architecture for the Tableau Public dashboard.

## Dashboard Layout & Key Views

### View 1: Global Trait & Morphology Explorer
- **Visuals**: Scatter plot (Length vs. Weight with log-scaling option) and bar charts of `BodyShapeI`.
- **Interactivity**: Filter by habitat flags (`Fresh`, `Brack`, `Saltwater`) and depth profile (`DemersPelag`).
- **Core Metric**: Distribution of species physical traits across taxonomic families.

### View 2: Environmental Vulnerability Matrix
- **Visuals**: Heatmap of average `Vulnerability` score grouped by habitat domain and body shape.
- **Insights**: Highlights high-risk species profiles to support conservation priority scoring.

### View 3: Machine Learning Model Residual Analysis
- **Visuals**: Scatter plot comparing `Length` (Actual) vs. `predicted_length` colored by `prediction_error`.
- **Metrics**: Interactive KPI tiles displaying global MAE (11.07 cm), RMSE (35.02 cm), and OLS $R^2$ (0.625).

## Data Source
- Input file: `tableau_fish_traits.csv` (96,276 records)
