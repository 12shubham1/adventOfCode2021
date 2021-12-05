# Imports
import pandas as pd

# Read in all data
with open(".\input.txt") as f:
    data = f.readlines()

# Split binary numbers into a list of lists
data = [list(str(x).strip()) for x in data]

# Create a df where each row contains all numbers as diff columns
df = pd.DataFrame(data)

# Converting cols all to numeric
for col in df.columns:
    df[col] = pd.to_numeric(df[col])

# power_rate = epsilon rate * gamma rate
# To identify if more '0' or '1', calculate the mean. Axis=0 i.e. sum of all
# rows
df_mean = df.mean(axis=0)

# Gamma rate binary
gamma_binary = ["1" if x > 0.5 else "0" for x in list(df_mean)]
# Epsilon rate binary
epsilon_binary = ["0" if x > 0.5 else "1" for x in list(df_mean)]

# Getting the result for both as binary
gamma_binary = "".join(gamma_binary)
epsilon_binary = "".join(epsilon_binary)

# Converting to decimals
gamma = int(gamma_binary, 2)
epsilon = int(epsilon_binary, 2)

# Getting power rate
power_rate = gamma * epsilon
print(power_rate)
