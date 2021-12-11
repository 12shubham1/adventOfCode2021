import pandas as pd
import numpy as np
import sys
import os

data_file = os.path.join(sys.path[0], "input.txt")

# Reading in data
with open(data_file) as f:
    data = f.readlines()

# Parsing input
max_num = 0
all_lines = []
diag_lines = []
for line in data:
    a, b = line.strip().split(" -> ")
    a = a.split(",")
    b = b.split(",")
    a = (int(a[0]), int(a[-1]))
    b = (int(b[0]), int(b[-1]))

    # If in a straight line
    if (a[0] == b[0]) or (a[-1] == b[-1]):
        all_lines.append([a, b])
        if max(a) > max_num:
            max_num = max(a)
        elif max(b) > max_num:
            max_num = max(b)
    else:
        diag_lines.append([a, b])


# Create a board of size max_num x max_num
# As it starts from 0
max_num += 1
df = pd.DataFrame(np.zeros((max_num, max_num)))
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


# Diag lines
for line in diag_lines:
    print(f"Diagnol line: {line}")
    x1, y1 = line[0][0], line[0][1]
    x2, y2 = line[1][0], line[1][1]

    x_list = []
    y_list = []
    # Can go in 1 of 4 directions
    # NE
    if x1 < x2 and y1 < y2:
        x_list = [x for x in range(x1, x2 + 1)]
        y_list = [y for y in range(y1, y2 + 1)]
    # NW
    elif x1 > x2 and y1 < y2:
        x_list = [x for x in range(x1, x2 - 1, -1)]
        y_list = [y for y in range(y1, y2 + 1)]
    # SE
    elif x1 < x2 and y1 > y2:
        x_list = [x for x in range(x1, x2 + 1)]
        y_list = [y for y in range(y1, y2 - 1, -1)]

    # SW
    elif x1 > x2 and y1 > y2:
        x_list = [x for x in range(x1, x2 - 1, -1)]
        y_list = [y for y in range(y1, y2 - 1, -1)]

    for i in range(len(x_list)):
        df.iloc[y_list[i], x_list[i]] += 1

mask = df >= 2
print("Total number of points with 2 or more intersections:")
print(f"\t{df[mask].count().sum()}")
