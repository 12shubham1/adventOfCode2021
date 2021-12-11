from numpy.core.numeric import full
import pandas as pd
import os

os.chdir(r"C:\Users\12shu\OneDrive\side_projects\adventOfCode2021\day9")
# Reading in data
with open(".\input.txt") as f:
    data = f.readlines()

all_data = []
for line in data:
    all_data.append([int(x.strip()) for x in list(line) if x != "\n"])

df = pd.DataFrame.from_records(all_data)

# Num rows, num cols
print(len(df), len(df.columns))


def check_min(val, others):
    if val == min([val] + others):
        if val not in others:
            return True

    return False


# Getting all low points

low_indexes = []
# Iterating over each row, col
# i =row
for i in range(len(df)):
    # j =col
    for j in range(len(df.columns)):
        p1 = df.iloc[i, j]
        # Top left
        if i == 0 and j == 0:
            p2 = df.iloc[i + 1, j]
            p3 = df.iloc[i, j + 1]

            if check_min(p1, [p2, p3]):
                low_indexes.append([i, j, p1])

        # Top row
        elif i == 0 and j not in (0, len(df.columns) - 1):
            p2 = df.iloc[i + 1, j]
            p3 = df.iloc[i, j - 1]
            p4 = df.iloc[i, j + 1]

            if check_min(p1, [p2, p3, p4]):
                low_indexes.append([i, j, p1])

        # First col
        elif i not in (0, len(df) - 1) and j == 0:
            p2 = df.iloc[i + 1, j]
            p3 = df.iloc[i, j + 1]
            p4 = df.iloc[i - 1, j]

            if check_min(p1, [p2, p3, p4]):
                low_indexes.append([i, j, p1])

        # Bottom left
        elif i == len(df) - 1 and j == 0:
            p2 = df.iloc[i - 1, j]
            p3 = df.iloc[i, j + 1]

            if check_min(p1, [p2, p3]):
                low_indexes.append([i, j, p1])

        # Bottom Row
        elif i == len(df) - 1 and j not in (0, len(df.columns) - 1):
            p2 = df.iloc[i - 1, j]
            p3 = df.iloc[i, j + 1]
            p4 = df.iloc[i, j - 1]

            if check_min(p1, [p2, p3, p4]):
                low_indexes.append([i, j, p1])

        # Top right
        elif i == 0 and j == len(df.columns) - 1:
            p2 = df.iloc[i, j - 1]
            p3 = df.iloc[i + 1, j]

            if check_min(p1, [p2, p3]):
                low_indexes.append([i, j, p1])

        # Right column
        elif i not in (0, len(df) - 1) and j == len(df.columns) - 1:
            p2 = df.iloc[i, j - 1]
            p3 = df.iloc[i + 1, j]
            p4 = df.iloc[i - 1, j]

            if check_min(p1, [p2, p3, p4]):
                low_indexes.append([i, j, p1])

        # Bottom Right
        elif i == len(df) - 1 and j == len(df.columns) - 1:
            p2 = df.iloc[i - 1, j]
            p3 = df.iloc[i, j - 1]

            if check_min(p1, [p2, p3]):
                low_indexes.append([i, j, p1])

        # All other cases
        else:
            p2 = df.iloc[i - 1, j]
            p3 = df.iloc[i + 1, j]
            p4 = df.iloc[i, j + 1]
            p5 = df.iloc[i, j - 1]

            if check_min(p1, [p2, p3, p4, p5]):
                low_indexes.append([i, j, p1])

print(low_indexes)


def check_higher_points(row, col, df):

    curr_point = df.iloc[row, col]
    all_higher = []
    try:
        new_row = row + 1
        new_col = col
        if df.iloc[new_row, new_col] > curr_point and new_row >= 0 and new_col >= 0:
            all_higher.append([new_row, new_col])
    except IndexError:
        pass
    try:
        new_row = row - 1
        new_col = col
        if df.iloc[new_row, new_col] > curr_point and new_row >= 0 and new_col >= 0:
            all_higher.append([new_row, new_col])
    except IndexError:
        pass

    try:
        new_row = row
        new_col = col + 1
        if df.iloc[new_row, new_col] > curr_point and new_row >= 0 and new_col >= 0:
            all_higher.append([new_row, new_col])
    except IndexError:
        pass

    try:
        new_row = row
        new_col = col - 1
        if df.iloc[new_row, new_col] > curr_point and new_row >= 0 and new_col >= 0:
            all_higher.append([new_row, new_col])
    except IndexError:
        pass

    return all_higher


# Replacing all 9's as they don't count
df.replace(9, 0, inplace=True)

# Once all low points have been identified, iterate over neighbours and keep
# finding higher values
basins = []
for outcome in low_indexes:
    print("\n")
    print("Starting from low point and finding higher values:")
    print(outcome[0], outcome[1])
    all_higher_count = 1
    # Getting first set of higher neighbours
    all_higher = check_higher_points(outcome[0], outcome[1], df)
    all_higher_count += len(all_higher)
    full_higher_list = all_higher.copy()
    while len(all_higher):
        new_higher = []
        for coords in all_higher:
            # Check all neighbours of curr point and if higher
            curr_higher = check_higher_points(coords[0], coords[1], df)

            curr_higher = [x for x in curr_higher if x not in full_higher_list]
            all_higher_count += len(curr_higher)
            # For current set of coords want to keep adding to list of coords
            new_higher += curr_higher
            full_higher_list += curr_higher

        all_higher = new_higher.copy()

    basins.append(all_higher_count)
    print(f"Basin size: {all_higher_count}")

basins.sort(reverse=True)

print(basins[0] * basins[1] * basins[2])
