# %% [markdown]
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Load dataset
df = pd.read_csv("/content/drive/MyDrive/Global_warming/GlobalTemperatures.csv")

# Standardize date format
def standardize_date_format(date_str):
    if '/' in date_str:
        return pd.to_datetime(date_str, format='%m/%d/%Y', errors='coerce')
    return pd.to_datetime(date_str, format='%Y-%m-%d', errors='coerce')

df['dt'] = df['dt'].apply(standardize_date_format)

# Drop unnecessary columns
df_removed_col = df.drop([
    'LandMaxTemperature', 'LandMaxTemperatureUncertainty',
    'LandMinTemperature', 'LandMinTemperatureUncertainty',
    'LandAndOceanAverageTemperature', 'LandAndOceanAverageTemperatureUncertainty'
], axis=1)

# Remove NaN values and duplicates
df_removed_col.dropna(inplace=True)
df_removed_col.drop_duplicates(inplace=True)

# Create a clean version without NaNs
df_removed_na = df.dropna().reset_index(drop=True)

# Visualizations
sns.pairplot(df_removed_col)
plt.show()

for column in df_removed_col.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df_removed_col[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

for column in df_removed_col.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(df_removed_col[column])
    plt.title(f'Box Plot of {column}')
    plt.show()
