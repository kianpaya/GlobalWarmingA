# Global Warming Analysis Project

## Overview

The **Global Warming Analysis Project** aims to analyze long-term climate trends and the impact of global warming using advanced data science techniques and machine learning models. The project explores over 250 years of historical temperature data, investigating how climate change has evolved and predicting future temperature trends using models such as **LSTM** and **ARIMA**.

The data includes global **Land and Ocean Temperature Records** with corresponding uncertainty values. The goal is to uncover patterns in global temperature changes and identify the contributing factors behind these changes, including **CO2 emissions**, **population growth**, and **GDP**.

<img src="https://github.com/kianpaya/GlobalWarmingA/blob/main/images/World%20Map.jpg" width="600" alt="World Map of Temperature Changes">
*Land temperature data is calculated differently from ocean temperature data, and the final global temperature was averaged accordingly.*

---

## Project Components

### 1. Data Collection and Preparation
- The dataset, **GlobalTemperatures.csv**, spans **1750 to 2015**, providing monthly global temperature records.
- **Data Cleaning**:
  - Standardized date formats and country names (e.g., accounting for historical changes in country borders).
  - Missing values were handled using interpolation and predictive modeling.
  
### 2. Data Aggregation and Feature Engineering
- **Yearly Averages**: Monthly data was aggregated into yearly averages to provide a clearer long-term view.
- **Weighted Averages**: Global temperatures were calculated using weighted averages, factoring in country-level metrics such as **land area**, **population**, and **GDP**.
- **Geographical Categorization**: The globe was divided into longitudinal zones around the tropics and other key areas to understand regional climate patterns more clearly.

### 3. Visualization and Analysis
- **Heatmaps** and **time series plots** were generated to visualize temperature changes across different regions over time.
- **Geospatial Mapping**: Temperature changes were mapped globally, allowing for regional comparisons and the identification of climate hotspots.

### 4. Machine Learning Models
- Multiple models, including **ARIMA**, **Random Forest**, **RNN**, and **LSTM**, were used to predict future temperature trends.
- **Model Evaluation**: **PyCaret** was employed to compare model performance and accuracy, with **LSTM** showing the best predictive results.

### 5. Dealing with Uncertainty
- The dataset includes an **Uncertainty Column** that accounts for the reliability of each data point. This uncertainty was factored into the machine learning models to provide more accurate and reliable predictions.

---

## Future Considerations

The following enhancements are planned for the next phase of the project:

1. **Improved Data Cleaning**:
   - Standardize country names across historical time periods for more accurate historical analysis.
   
2. **CO2 Emissions**: 
   - Incorporate country-level CO2 emissions data to assess its correlation with temperature changes over time.

3. **Geographical Granularity**:
   - Divide the globe into finer geographical regions, including **elevation** and **coastal proximity**, to better understand the impact of these factors on temperature variations.

4. **Model Comparison and Tuning**:
   - Further evaluate models like **XGBoost** and **Prophet** alongside the existing models to identify the most accurate method for temperature predictions.

5. **External Data Integration**:
   - Integrate **NASA GIS** data for improved geospatial accuracy in temperature predictions and climate impact analysis.

6. **Project Management**:
   - Follow an **Agile methodology** (Kanban or Scrum) for the next project phase, targeting a one-month completion for advanced models and data integration.

---

## Requirements

To run the project, ensure the following Python libraries are installed. Use the provided `requirements.txt` for easy installation.

```plaintext
numpy
pandas
matplotlib
seaborn
scikit-learn
tensorflow
keras
pycaret
statsmodels
jupyter
