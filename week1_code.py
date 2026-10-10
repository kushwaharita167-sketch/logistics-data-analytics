import pandas as pd

# Load Logistics Dataset
df = pd.read_csv("logistics_data.csv")

# Display first 5 rows of data
print("--- Logistics Dataset Overview ---")
print(df.head())

# Calculate Key Logistics Metrics
total_orders = len(df)
on_time_orders = len(df[df['delivery_status'] == 'On-Time'])
on_time_rate = (on_time_orders / total_orders) * 100

avg_delivery_time = df['delivery_time_hours'].mean()

print(f"\nTotal Orders Processed: {total_orders}")
print(f"On-Time Delivery Rate: {on_time_rate:.2f}%")
print(f"Average Delivery Time: {avg_delivery_time:.2f} hours")
