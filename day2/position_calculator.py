# Reading Data
with open(".\input.txt") as f:
    data = f.readlines()

# Parsing data as ('Command', value)
data = [(x.split(" ")[0], int(x.split(" ")[1])) for x in data]

# Creating a mapping for each direction
dir_mapping = {"forward": 1, "down": 1, "up": -1}

# Instantiating variables
horizontal = 0
depth = 0

# Iterating over all commands
for command in data:
    if command[0] == "forward":
        horizontal += dir_mapping.get(command[0]) * command[1]
    else:
        depth += dir_mapping.get(command[0]) * command[1]

# Printing all resulting variables
print(f"Depth: {depth}")
print(f"Horizontal: {horizontal}")
print(f"Total: {horizontal*depth}")
