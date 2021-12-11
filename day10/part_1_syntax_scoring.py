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

chunks = []


illegal = []
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
                # This line is illegal, move to next
                break
            else:
                # Case where chunk is closed, remove opening of
                # associated chunk
                chunks.pop()


close_mapping = {")": 3, "]": 57, "}": 1197, ">": 25137}

total = 0
for char in illegal:
    total += close_mapping.get(char)

print(total)

