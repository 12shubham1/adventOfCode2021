from collections import OrderedDict

# Reading in data
with open(".\input.txt") as f:
    data = f.readlines()[0].strip().split(",")

# Converting all to ints
fish = [int(x) for x in data]

# Use a dict mapping rather than storing all
fish_life = {}
for x in fish:
    if x not in fish_life:
        fish_life[x] = 1
    else:
        fish_life[x] += 1


fish_life = OrderedDict(sorted(fish_life.items()))
print(fish_life)

# Playing over 256 days
for i in range(256):
    print(i)
    curr_fish_life = fish_life.copy()

    for key in list(fish_life.keys()):
        if key == 0:
            if 8 in curr_fish_life:
                curr_fish_life[8] += fish_life[0]
            else:
                curr_fish_life[8] = fish_life[0]

            try:
                curr_fish_life[6] += fish_life[0]
            except KeyError:
                curr_fish_life[6] = fish_life[0]

            # Reset number of fish with timer 0 as these
            # have been converted to new fish
            curr_fish_life[0] = 0
        
        else:
            try:
                curr_fish_life[key - 1] += fish_life[key]
            except KeyError:
                curr_fish_life[key - 1] = fish_life[key]

            curr_fish_life[key] -= fish_life[key]

    fish_life = OrderedDict(sorted(curr_fish_life.items()))


print(sum(fish_life.values()))
