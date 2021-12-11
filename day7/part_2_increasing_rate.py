# Reading in data
with open(".\input.txt") as f:
    data = f.readlines()[0].strip().split(",")

# Converting all to ints
horizontal_pos = [int(x) for x in data]

print(min(horizontal_pos), max(horizontal_pos))
unique_pos = [x for x in range(min(horizontal_pos), max(horizontal_pos)+1)]

def get_diff(curr_pos):
    total = 0
    n = abs(curr_pos -x )
    return n*(n+1)/2
    #for i in range(1, abs(curr_pos-x)+1):
    #    total += i
    #return total
        
        

total_fuel = 1e10
pos = -1
for x in unique_pos:
    print('\n')
    print(x)
    fuel_per_pos = map(get_diff, horizontal_pos)
    new_total_fuel = sum(fuel_per_pos)
    if new_total_fuel < total_fuel:
        pos = x
        total_fuel = new_total_fuel
    print(new_total_fuel)
    print(total_fuel)

print(f'Min fuel pos: {pos}')
print(f'Min fuel needed: {total_fuel}')





        




