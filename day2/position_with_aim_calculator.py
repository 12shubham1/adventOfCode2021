# Reading in all data
with open(".\input.txt") as f:
    data = f.readlines()

# Splitting commands as normal
data = [(x.split(" ")[0], int(x.split(" ")[1])) for x in data]

# Creating a mapping for aim
aim_mapping = {
    "down": 1,
    "up": -1,
}

# Instantiating variables
horizontal = 0
depth = 0
aim = 0

# Iterating over all commands
for command in data:
    # Handling the different criteria
    if command[0] in ("down", "up"):
        aim += aim_mapping.get(command[0]) * command[1]
    elif command[0] == "forward":
        horizontal += command[1]
        depth += aim * command[1]
    else:
        print(command[0])
        print("Command not identified")

# Printing all output variables
print(f"Depth: {depth}")
print(f"Horizontal: {horizontal}")
print(f"Aim: {aim}")
print(f"Total: {horizontal*depth}")
