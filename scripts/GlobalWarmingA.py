# %% [markdown]
# # Library Import

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# %%
from google.colab import drive
drive.mount('/content/drive')

# %% [markdown]
# # Raw Data Reading and Cleaning

# %%
data = pd.read_csv("/content/drive/MyDrive/Global_warming/GlobalTemperatures.csv")
df = pd.DataFrame(data)
df

# %%
df.describe()

# %%
df.dtypes

# %%
def standardize_date_format(date_str):
    # Check if the date is in MM/DD/YYYY format (if there's a '/' in the string)
    if '/' in date_str:
        try:
            # Convert from MM/DD/YYYY to YYYY-MM-DD
            return pd.to_datetime(date_str, format='%m/%d/%Y', errors='coerce')
        except ValueError:
            return np.nan
    else:
        # Convert from YYYY-MM-DD to datetime format
        try:
            return pd.to_datetime(date_str, format='%Y-%m-%d', errors='coerce')
        except ValueError:
            return np.nan

# %%


# %%
# Apply the function to the 'dt' column
df['dt'] = df['dt'].apply(standardize_date_format)

# %%
df

# %%
df.info()

# %% [markdown]
# # Data with Removed Column Handling

# %%
df_removed_col = df.copy()

# %%
df_removed_col.drop(['LandMaxTemperature', 'LandMaxTemperatureUncertainty', 'LandMinTemperature', 'LandMinTemperatureUncertainty', 'LandAndOceanAverageTemperature', 'LandAndOceanAverageTemperatureUncertainty'], axis=1 ,inplace=True)
df_removed_col

# %%
df_removed_col.isnull().sum()

# %%
df_removed_col.dropna(inplace=True)

# %%
df_removed_col.drop_duplicates(inplace=True)

# %% [markdown]
# # Data with Removed NaN Handling

# %%
df_removed_na = df.copy()

# %%
df_removed_na = df_removed_na.dropna()

# %%
df_removed_na.reset_index(drop=True, inplace=True)

# %%
df_removed_na

# %% [markdown]
# # Visualization for DataFrame with removed Columns

# %%
sns.pairplot(df_removed_col)
plt.show()

# %%
numeric_columns = df_removed_col.columns
for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df_removed_col[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

# %%
numeric_columns = df_removed_col.columns
for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(df_removed_col[column])
    plt.title(f'Box Plot of {column}')
    plt.show()

# %% [markdown]
# # Visualization for DataFrame with removed NaNs

# %%
sns.pairplot(df_removed_na, hue='LandAverageTemperature')
plt.show()

# %%
numeric_columns = df_removed_na.columns
for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df_removed_na[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

# %%
numeric_columns = df_removed_na.columns
for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(df_removed_na[column])
    plt.title(f'Box Plot of {column}')
    plt.show()

# %% [markdown]
# # Analysis of Removed Column Data with Clustering

# %%
df_removed_col

# %% [markdown]
# # Regression


