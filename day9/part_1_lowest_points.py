import pandas as pd

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


low_indexes = []
# Iterating over each row, col
# i =row
for i in range(len(df)):
    # j =col
    for j in range(len(df.columns)):
        print(i, j)
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

total = 0
for outcome in low_indexes:
    df.iloc[outcome[0], outcome[1]] = "x"
    total += outcome[-1] + 1


print(df)
print(total)
