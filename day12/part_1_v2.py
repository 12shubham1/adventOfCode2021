import os
import pandas as pd
from collections import defaultdict, deque

os.chdir(r"C:\Users\12shu\OneDrive\side_projects\adventOfCode2021\day12")

# Reading in data
with open(".\input.txt") as file:
    data = file.readlines()

paths = [x.strip().split("-") for x in data]

# Keeping track for all nodes what they are connected to
node_dict = defaultdict(list)
for a, b in paths:
    node_dict[a].append(b)
    node_dict[b].append(a)

print(node_dict)

# Starting state i.e. we start from 'start' and we cannot visit 'start'
start = ("start", set(["start"]), None)
# Var to store all possible path count
ans = 0
# Creating a list of paths as a bi-directional list
Q = deque([start])
while Q:
    # Get the first value in list
    pos, small, twice = Q.popleft()
    # If pos is end, we have a valid path finished and count this
    if pos == "end":
        ans += 1
        continue
    # Iterating over all possible nodes for this node
    for y in node_dict[pos]:
        # If node has not been visited in small
        if y not in small:
            # Check if node is small
            new_small = set(small)
            # if node is small, add to small set
            if y.lower() == y:
                new_small.add(y)
            # Append (right side) the new node and new small
            Q.append((y, new_small, twice))

        elif y in small and twice is None and y not in ["start", "end"]:
            Q.append((y, small, y))
print(ans)
