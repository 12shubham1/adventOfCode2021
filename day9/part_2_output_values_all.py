import functions as f


# Reading in data
# Reading in data
with open(".\input.txt", "r") as file:
    data = file.readlines()

all_data = []
for line in data:
    all_data.append([x.strip() for x in line.split(" | ")])

# general mapping
# Num digits to num segments
general_mapping = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}


output_vals = []
# So per set of displays, the mappings are the same
# For each display, getting the known numbers
for mapping in all_data:
    segments = {"t": "", "tl": "", "tr": "", "m": "", "bl": "", "br": "", "b": ""}
    # Getting all easily identified numbers i.e. len is enough to identify
    # Identify 1, 4, 7 ,8
    curr_mapping_signals = f.get_simple_nums(mapping[0], general_mapping)

    # Identify top segment by comparing 1 and 7
    segments["t"] = f.get_top_segment(curr_mapping_signals)

    # Identifynumber for 6 and top right/bottom right segments
    curr_mapping_signals[6], segments["tr"], segments["br"] = f.get_number_6_signal(
        mapping[0], curr_mapping_signals
    )

    # Identifying number 3
    (
        curr_mapping_signals[2],
        curr_mapping_signals[3],
        curr_mapping_signals[5],
    ) = f.get_len_5_letters(mapping[0], segments)

    curr_mapping_signals[0], curr_mapping_signals[9] = f.get_0_9_letters(
        mapping[0], curr_mapping_signals
    )

    final_mapping = dict((v, k) for k, v in curr_mapping_signals.items())
    curr_num = []
    for signal in mapping[1].split(" "):
        for k, v in final_mapping.items():
            if set(k) == set(signal):
                curr_num.append(str(v))

    current_out = int("".join(curr_num))
    output_vals.append(current_out)
    print(current_out)

print(sum(output_vals))
