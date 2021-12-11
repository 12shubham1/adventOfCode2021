import os

os.chdir(r"C:\Users\12shu\OneDrive\side_projects\adventOfCode2021\day10")

# Reading in data
with open(".\input.txt") as f:
    data = f.readlines()

all_data = [x.strip() for x in data]

# print(all_data)

open_chunk = ["(", "{", "[", "<"]

c2o = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<",
}

o2c = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}


chunks = []


illegal = []
lines_to_remove = []
for i, line in enumerate(all_data):
    for char in line:
        # An opening character hit, append to chunk tracker
        if char in open_chunk:
            chunks.append(char)
        # It must be a closing character
        else:
            # Case where latest opening char is not closed
            if chunks[-1] != c2o.get(char):
                illegal.append(char)
                lines_to_remove.append(i)
                # This line is illegal, move to next
                break
            else:
                # Case where chunk is closed, remove opening of
                # associated chunk
                chunks.pop()


lines_to_keep = []
for i, line in enumerate(all_data):
    if i not in lines_to_remove:
        lines_to_keep.append(line)

all_to_add = []
for line in lines_to_keep:
    chunks = []
    for char in line:
        if char in open_chunk:
            chunks.append(char)
        else:
            chunks.pop()

    # Once we have got to end of string, invert order to find closing
    to_close = [o2c.get(x) for x in chunks[::-1]]
    all_to_add.append(to_close)

close_mapping = {")": 1, "]": 2, "}": 3, ">": 4}

all_totals = []
for to_add in all_to_add:
    total = 0
    for char in to_add:
        total = total * 5
        total += close_mapping.get(char)

    all_totals.append(total)

print(sorted(all_totals)[len(all_totals) // 2])
