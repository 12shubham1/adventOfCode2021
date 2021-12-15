import os
import pandas as pd

os.chdir(r"C:\Users\12shu\OneDrive\side_projects\adventOfCode2021\day13")

# Reading in data
with open(".\input.txt") as file:
    data = file.readlines()

all_dots = []
all_folds = []
max_x = 0
max_y = 0
for line in data:
    line = line.strip()
    if line.split(" ")[0] == "fold":
        instruction = line.split(" ")[-1]
        all_folds.append(instruction)
    else:
        split_line = line.split(",")
        if split_line[0] != "":
            a = int(split_line[0])
            b = int(split_line[1])
            if a > max_x:
                max_x = a
            if b > max_y:
                max_y = b
            all_dots.append([a, b])

# Creating an empty df
df = pd.DataFrame(
    columns=[x for x in range(max_x + 1)], index=[x for x in range(max_y + 1)]
)

# Assigning all dots
for dots in all_dots:
    df.iloc[dots[1], dots[0]] = 1

# Filling in non-dots with 0
df[df != 1] = 0

# Applying the first fold
fold = all_folds[0]


def apply_fold_vertically(fold_pos, df):

    # Getting all points that will be shifted
    mask = df.index > fold_pos

    for _, row in df[mask].iterrows():
        row_below_fold = row.name - fold_pos
        row_to_assign_to = fold_pos - row_below_fold

        target_row = df.iloc[row_to_assign_to, :]

        resultant_row = target_row | row

        df.iloc[row_to_assign_to, :] = resultant_row

    return df[~(df.index >= fold_pos)]


def apply_fold_left(fold_pos, df):

    mask = df.columns > fold_pos

    for col in df.loc[:, mask].columns:
        col_after_fold = col - fold_pos
        target_col_number = fold_pos - col_after_fold

        target_col = df[target_col_number]
        resultant_col = target_col | df[col]

        df[target_col_number] = resultant_col

    return df.loc[:, ~(df.columns >= fold_pos)]


# Fold upwards along y axis
for fold in all_folds:
    print(fold)
    if fold[0] == "y":
        fold_row = int(fold.split("=")[-1])
        df = apply_fold_vertically(fold_row, df)
        # Fold left along x axis
    else:
        fold_col = int(fold.split("=")[-1])
        df = apply_fold_left(fold_col, df)


df.replace(True, "#", inplace=True)
df.replace(False, ".", inplace=True)

print(df)
