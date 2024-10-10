# Global Warming Analysis Project

## Overview

The **Global Warming Analysis Project** is dedicated to understanding long-term climate trends through the application of advanced data science techniques and machine learning models. Leveraging over 250 years of historical global temperature data, this project aims to analyze the impact of global warming and predict future climate conditions. By incorporating advanced models such as **LSTM** and **ARIMA**, and powerful data visualization tools, this project provides actionable insights into temperature changes over time and their potential future impact.

The data used in this project comes from **Global Land and Ocean Temperature Records**. It includes a range of temperature measures such as **Land Average Temperature**, **Land Max/Min Temperatures**, and **Land and Ocean Average Temperatures**, along with their respective uncertainty values. The project also explores how external factors like **CO2 emissions**, **population growth**, and **GDP** influence global temperatures.

![World Map: Highlighting Global Temperature Changes](https://github.com/kianpaya/GlobalWarmingA/blob/main/images/World%20Map.jpg)
*Figure: A dynamic visualization of global regions affected by temperature changes over time. The heat zones represent areas experiencing significant temperature increases, while cooler zones indicate less impact.*

---

## Project Components

### 1. Data Collection and Preparation
- The dataset, **GlobalTemperatures.csv**, was obtained from publicly available climate records, containing monthly observations from **1750 to 2015**.
- **Data Cleaning**: 
   - Removed invalid entries.
   - Standardized date formats.
   - Dealt with missing values using interpolation and predictive modeling techniques to ensure data completeness.
   - Processed and standardized **country names** to account for geopolitical changes (e.g., countries that no longer exist, new countries).

### 2. Data Aggregation and Feature Engineering
- **Monthly Data to Yearly Aggregates**: Data was aggregated from monthly to yearly averages, simplifying the analysis while maintaining data integrity. Weighted averages were calculated, factoring in **land area**, **population**, and **GDP** of each country to derive a more accurate global temperature trend.
- **Geographical Categorization**: The globe was divided into five primary longitudinal zones around the **Tropic of Cancer and Capricorn**, and further divided by longitudinal sections. This breakdown allows for an in-depth study of temperature trends within specific geographic regions.

### 3. Visualization and Analysis
- **Interactive Visualizations**: Using **Matplotlib** and **Seaborn**, various plots such as heatmaps, line graphs, and scatter plots were created to represent global temperature changes over time.
- **Geospatial Mapping**: Detailed visualizations highlight the regions most affected by climate change. These visualizations provide a global view, while allowing a deeper dive into regional trends.
  
### 4. Machine Learning Models
- **ARIMA**, **Random Forest**, **RNN**, and **LSTM** models were applied to predict future temperature trends based on historical data. The best performing model, **LSTM**, was used to produce long-term predictions for the next 50 years.
- **Model Comparison**: Tools such as **PyCaret** were used to compare different models based on their performance (accuracy, RMSE) and ability to generalize predictions across different regions.

### 5. Dealing with Uncertainty
- The dataset includes an **Uncertainty Column**, representing the reliability of the temperature data. This uncertainty was factored into the model training to weigh data points appropriately, ensuring more robust and accurate results.

---

## Future Considerations and Enhancements

While the core components of the project have been developed, the following future considerations will enhance the depth and accuracy of the analysis:

1. **Enhanced Data Cleaning**:
   - Further refinement in the handling of **country names**, especially for regions where borders have changed or countries no longer exist. Apply a historical reference to ensure that data matches the appropriate time period.
   
2. **Feature Engineering**:
   - **CO2 Emissions**: Integrate **CO2 emissions** data for each country and year to investigate its direct correlation with global temperature changes. This will be treated as an independent factor, allowing for insights into how industrialization and carbon output have impacted climate change.
   
3. **More Granular Geographical Categorization**:
   - Currently, regions are categorized by latitude and longitude zones. Future updates will aim to incorporate **elevation data** and **coastal proximity** to understand how geography influences temperature trends.
   
4. **Advanced Model Comparison**:
   - **PyCaret** will be used to systematically compare additional models, such as **XGBoost** and **Prophet**, alongside existing models like **LSTM** and **ARIMA**. This will allow us to determine which models are best suited for both short-term and long-term climate predictions.

5. **Data Enrichment**:
   - **NASA GIS** data will be integrated to enrich the current dataset, providing detailed insights into specific geospatial regions. This will offer a more comprehensive understanding of climate change impacts on different continents and regions.
   
6. **Project Management and Agile Execution**:
   - The next phase of this project will follow an **Agile framework** (Kanban or Scrum), with a flexible one-month timeline for the first deliverables. Milestones include advanced model training, additional data integration, and more detailed visualizations.

---

## Requirements

To run this project, ensure that the following dependencies are installed. The complete list is available in the `requirements.txt` file.

