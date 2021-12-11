# Reading in data
with open(".\input.txt") as f:
    data = f.readlines()[0].strip().split(",")

# Converting all to ints
horizontal_pos = [int(x) for x in data]

unique_pos = sorted(list(set(horizontal_pos)))

def get_diff(curr_pos):
    return abs(curr_pos - x)

total_fuel = 1e8
pos = -1
for x in unique_pos:
    fuel_per_pos = map(get_diff, horizontal_pos)
    new_total_fuel = sum(fuel_per_pos)
    if new_total_fuel < total_fuel:
        pos = x
        total_fuel = new_total_fuel

print(f'Min fuel pos: {pos}')
print(f'Min fuel needed: {total_fuel}')





        




