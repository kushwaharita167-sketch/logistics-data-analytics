import numpy as np
import pandas as pd

# 1. Data Collection Simulation
np.random.seed(42)
data_size = 100

data = {
    "Shipment_ID": [f"SHP_{1000+i}" for i in range(data_size)],
    "Transport_Cost": np.random.normal(loc=150, scale=30, size=data_size),
    "Delivery_Time_Hours": np.random.normal(loc=24, scale=5, size=data_size),
    "On_Time_Status": np.random.choice(
        ["On-Time", "Delayed", None], size=data_size, p=[0.7, 0.2, 0.1]
    ),
    "Distance_KM": np.random.uniform(50, 500, size=data_size),
}

df = pd.DataFrame(data)

# Introduce missing values and outliers for cleaning demonstration
df.loc[10:15, "Transport_Cost"] = np.nan
df.loc[5, "Delivery_Time_Hours"] = 150  # Outlier

print("--- Raw Dataset Sample ---")
print(df.head())

# 2. Data Cleaning: Handling Missing Values
df["Transport_Cost"].fillna(df["Transport_Cost"].median(), inplace=True)
df["On_Time_Status"].fillna("Unknown", inplace=True)

# 3. Outlier Handling (IQR Method)
Q1 = df["Delivery_Time_Hours"].quantile(0.25)
Q3 = df["Delivery_Time_Hours"].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR

df["Delivery_Time_Hours"] = np.where(
    df["Delivery_Time_Hours"] > upper_bound, upper_bound, df["Delivery_Time_Hours"]
)
df["Delivery_Time_Hours"] = np.where(
    df["Delivery_Time_Hours"] < lower_bound, lower_bound, df["Delivery_Time_Hours"]
)

# 4. Data Normalization (Min-Max Scaling)
df["Normalized_Cost"] = (df["Transport_Cost"] - df["Transport_Cost"].min()) / (
    df["Transport_Cost"].max() - df["Transport_Cost"].min()
)

print("\n--- Cleaned & Preprocessed Dataset Sample ---")
print(
    df[
        [
            "Shipment_ID",
            "Transport_Cost",
            "Normalized_Cost",
            "Delivery_Time_Hours",
            "On_Time_Status",
        ]
    ].head()
)
