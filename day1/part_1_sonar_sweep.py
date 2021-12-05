# Imports
import pandas as pd

# Read Data
with open(".\input.txt") as f:
    data = f.readlines()

# Parse data as integers
data = [int(x) for x in data]

# Create a DataFrame
df = pd.DataFrame(data, columns=["data"])

# Rolling window to calculate change
df["rolling_diff"] = df.rolling(window=2).apply(lambda x: x.iloc[1] - x.iloc[0])
# Getting all increases
mask = df["rolling_diff"] > 0

# Print how many as answer
print(f"There are {len(df[mask])} measurements bigger than previous")
