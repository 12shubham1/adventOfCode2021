import functions as f
import os
import pandas as pd

os.chdir(r"C:\Users\12shu\OneDrive\side_projects\adventOfCode2021\day11")

# Reading in data
with open(".\input.txt") as file:
    data = file.readlines()

all_data = [list(x.strip()) for x in data if x != "\n"]

df = pd.DataFrame.from_records(all_data)

for col in df.columns:
    df[col] = pd.to_numeric(df[col])

# Simulating 100 flashes
total_flashes = 0
print(df)
for i in range(100):
    print("\n")
    print(f"Step: {i+1}")
    # Step 1: Increment everything as a base +1
    df = df + 1

    # Step 2: Slicing wherever high vals exist
    mask = df > 9
    while not df[mask].isnull().all().all():
        df = f.propagate_energy(df, mask)
        mask = df > 9

    curr_flashes = df[df < 0].count().sum()
    df[df < 0] = 0
    print(curr_flashes)
    total_flashes += curr_flashes

    print(df)

print(total_flashes)
