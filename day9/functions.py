def get_simple_nums(all_signals, general_mapping, curr_mapping_signals=None):
    if curr_mapping_signals is None:
        curr_mapping_signals = {}

    # Getting all signals with unique numb of digits
    for signal in all_signals.split(" "):
        if len(signal) in [2, 3, 4, 7]:
            associated_num = general_mapping.get(len(signal))[0]
            curr_mapping_signals[associated_num] = signal

    return curr_mapping_signals


def get_top_segment(curr_mapping_signals):
    return list(set(curr_mapping_signals[7]) - set(curr_mapping_signals[1]))[0]


def get_number_6_signal(signals, curr_mapping_signal):
    poss_6 = []
    for signal in signals.split(" "):
        if len(signal) == 6:
            poss_6.append(signal)

    signal_1 = list(curr_mapping_signal[1])
    # Check where only 1 instance of right side i.e. length of 6 has only b or e
    for signal in poss_6:
        if signal_1[0] in signal and signal_1[1] not in signal:
            return signal, signal_1[1], signal_1[0]
        elif signal_1[0] not in signal and signal_1[1] in signal:
            return signal, signal_1[0], signal_1[1]


def get_len_5_letters(signals, segments):
    poss_3 = []
    for signal in signals.split(" "):
        if len(signal) == 5:
            poss_3.append(signal)

    # Check where both top right and bottom right in signal
    for signal in poss_3:
        if segments["tr"] in signal and segments["br"] in signal:
            signal_3 = signal
        elif segments["tr"] in signal and segments["br"] not in signal:
            signal_2 = signal
        elif segments["tr"] not in signal and segments["br"] in signal:
            signal_5 = signal

    return signal_2, signal_3, signal_5


def get_0_9_letters(signals, curr_mapping_signals):
    for signal in signals.split(" "):
        if len(signal) == 6 and signal != curr_mapping_signals[6]:
            if len(set(curr_mapping_signals[5]) - set(signal)) == 0:
                signal_9 = signal
            else:
                signal_0 = signal

    return signal_0, signal_9
