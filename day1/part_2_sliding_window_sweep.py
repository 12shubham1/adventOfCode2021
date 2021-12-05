# Imports
import pandas as pd

# Read Data
with open(".\input.txt") as f:
    data = f.readlines()

# Read data as integers
data = [int(x) for x in data]

# Create a DataFrame
df = pd.DataFrame(data, columns=["data"])

# Get a rolling window sum as new measure
df["new_rolling_measure"] = df.rolling(window=3).sum()

# Getting the new measures rolling changes
df["rolling_diff"] = (
    df[["new_rolling_measure"]].rolling(window=2).apply(lambda x: x.iloc[1] - x.iloc[0])
)

# Get a rolling window for all increases
mask = df["rolling_diff"] > 0

# Printing out how many increases in the new measure
print(f"There are {len(df[mask])} measurements bigger than previous")
