# Imports =========================================

import pandas as pd
import numpy as np
import sys
import os

# Reading in data =================================

data_file = os.path.join(sys.path[0], "input.txt")

with open(data_file) as f:
    data = f.readlines()

# Parsing input ==================================

# Instantiating variables
max_num = 0
all_lines = []
rejected_lines = []

# Iterating over all lines of data
for line in data:
    # Getting the two pairs of coords
    a, b = line.strip().split(" -> ")
    # Splitting both to extract the ints
    a = a.split(",")
    b = b.split(",")
    # Converting to a tuple of ints
    a = (int(a[0]), int(a[-1]))
    b = (int(b[0]), int(b[-1]))
    # If in a straight line
    if (a[0] == b[0]) or (a[-1] == b[-1]):
        # Append to lines list
        all_lines.append([a, b])
        # Calc max coord
        if max(a) > max_num:
            max_num = max(a)
        elif max(b) > max_num:
            max_num = max(b)
    # Also store rejected lines for debugging
    else:
        rejected_lines.append([a, b])


# Create a board of size max_num by max_num
# As it starts from 0 increase by 1
max_num += 1
df = pd.DataFrame(np.zeros((max_num, max_num)))
# Convert all to numeric
for col in df.columns:
    df[col] = df[col].astype("int64")

# Iterate over each line
for line in all_lines:
    # Vertical condition i.e. same x coord
    if line[0][0] == line[1][0]:
        x = line[0][0]
        y1 = line[0][1]
        y2 = line[1][1]
        y_list = [min(y1, y2), max(y1, y2)]
        print(f"Vertical line: {line}")
        df.iloc[y_list[0] : y_list[1] + 1, x] += 1

    # Horizontal Condition i.e. same y coord
    elif line[0][1] == line[1][1]:
        y = line[0][1]
        x1 = line[0][0]
        x2 = line[1][0]
        x_list = [min(x1, x2), max(x1, x2)]
        print(f"Horizontal line: {line}")
        df.iloc[y, x_list[0] : x_list[1] + 1] += 1


mask = df >= 2
print("Total number of points with 2 or more intersections:")
print(f"\t{df[mask].count().sum()}")
