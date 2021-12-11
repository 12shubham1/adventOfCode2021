# Reading in data
with open(".\input.txt") as f:
    data = f.readlines()

all_data = []
for line in data:
    all_data.append([x.strip() for x in line.split(' | ')])

# general mapping
# Num digits to num segments
general_mapping = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}

# So per set of displays, the mappings are the same
count = 0
for mapping in all_data:
    #curr_mapping_signals = {}
    #for signal in mapping[0].split(' '):
    #    if len(signal) in [2,3,4,7]:
    #        num = general_mapping.get(len(signal))[0]
    #        curr_mapping_signals[num] = signal

    #print(curr_mapping_signals)
    for signal in mapping[1].split(' '):
        print(signal)
        if len(signal) in [2,3,4,7]:
            count += 1

print(count)
        

