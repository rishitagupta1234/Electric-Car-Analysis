import pandas as pd
import numpy as np

df = pd.read_excel("car.xlsx")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "").str.replace("-", "")

df = df.dropna(axis=1, how='all')

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col] = df[col].fillna('Unknown')

df = df.drop_duplicates()

df.to_excel("cleaned_data.xlsx", index=False)
print(" Cleaned data saved as 'cleaned_data.xlsx'")

df = pd.read_excel("cleaned_data.xlsx")

if 'number_of_cells' in df.columns:
    cells = df['number_of_cells'].to_numpy()

    print("\n NumPy Analysis of 'number of cells':")
    print(f" Mean: {np.mean(cells)}")
    print(f" Median: {np.median(cells)}")
    print(f" Std Deviation: {np.std(cells)}")
    print(f" Max: {np.max(cells)}")
    print(f" Min: {np.min(cells)}")

    high_cell_df = df[cells > np.median(cells)]
    high_cell_df.to_excel("ev data.xlsx", index=False)

if 'range_km' in df.columns:
    range_vals = df['range_km'].to_numpy()
    norm_range = (range_vals - np.min(range_vals)) / (np.max(range_vals) - np.min(range_vals))
    df['normalized_range'] = norm_range

    df.to_excel("final ev data.xlsx", index=False)
    print(" Final file saved as 'final ev data.xlsx'")