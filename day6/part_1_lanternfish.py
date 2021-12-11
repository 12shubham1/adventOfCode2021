# Reading in data
with open(".\input.txt") as f:
    data = f.readlines()[0].strip().split(",")

# Converting all to ints
fish = [int(x) for x in data]

print(fish)

# Playing over 80 days
for i in range(81):
    print(i)
    next_gen = fish.copy()
    for j, fish_timer in enumerate(next_gen):
        if fish_timer == 0:
            fish[j] = 6
            fish.append(8)
        else:
            fish[j] -= 1


print(f"Num fish after 80 days: {len(next_gen)}") 
        

        




