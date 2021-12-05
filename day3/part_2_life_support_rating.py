# Imports
import pandas as pd

# Reading input file
with open(".\input.txt") as f:
    data = f.readlines()

# Creating a list of lists for all binary numbers
data = [list(str(x).strip()) for x in data]

# Creating a df where each row is a binary number (1 bit per col)
df_orig = pd.DataFrame(data)
# Creating 2 copies for oxygen and scrubber rating
df_oxygen = df_orig.copy()
df_scrubber = df_orig.copy()

# Oxygen rating
# Iterating over each bit
for col in df_oxygen.columns:
    # Converting the col to numeric
    df_oxygen[col] = pd.to_numeric(df_oxygen[col])

    # Average gives us the indicator if more 1 or 0
    bit_avg = df_oxygen[col].mean()

    # Getting the most common bit
    mcb = 1 if bit_avg >= 0.5 else 0

    # Creating a binary mask to keep only the mcb on that bit/col
    mask = df_oxygen[col] == mcb

    # Slicing that bit for where it equals the mcb
    new_df = df_oxygen.loc[mask].copy()
    # Assigning truncated df as the working df
    df_oxygen = new_df

    # Case when only 1 number left, break
    if len(df_oxygen) == 1:
        break


# Print rating
print("Oxygen rating")
print(df_oxygen)

# CO2 Scrubber  rating
# Iterating over each bit
for col in df_scrubber.columns:
    # Converting current col to numeric
    df_scrubber[col] = pd.to_numeric(df_scrubber[col])

    # Average gives us the indicator if more 1 or 0
    bit_avg = df_scrubber[col].mean()

    # Getting the least common bit
    lcb = 1 if bit_avg < 0.5 else 0

    # Creating a binary mask to keep only the mcb
    mask = df_scrubber[col] == lcb

    # Assigning the truncated df to the working df
    df_scrubber = df_scrubber[mask].copy()

    # If 1 number left, break
    if len(df_scrubber) == 1:
        break


print("Scrubber  rating")
print(df_scrubber)


# Converting the resulting series to a binary string and then decimal
print("Life support rating")
scrubber_rating = "".join([str(x) for x in list(df_scrubber.iloc[0])])
oxygen_rating = "".join([str(x) for x in list(df_oxygen.iloc[0])])
print(int(scrubber_rating, 2) * int(oxygen_rating, 2))
