from collections import defaultdict

from helper import read_data

s = read_data(f"{__file__.split('.')[0]}.txt", converter=str)


def calc_freq(data):
    freq = defaultdict(int)
    for bin_num in data:
        for c, x in enumerate(bin_num):
            freq[c] += int(x)
    return freq


freq = calc_freq(s)
bin_num_length = len(freq)
gamma = [0 if freq[x] < (len(s) / 2) else 1 for x in range(bin_num_length)]
epsilon = [1 - g for g in gamma]


def bin_2_dec(bin_list):
    if isinstance(bin_list, str):
        bin_list = [int(x) for x in bin_list]
    s = 0
    for c, x in enumerate(reversed(bin_list)):
        s += 2 ** c * x
    return s


print(bin_2_dec(gamma) * bin_2_dec(epsilon))

data = s[:]


def bin_filter(old_data, keep_common, k=0):
    local_freq = calc_freq(old_data)
    if local_freq[k] > len(old_data) / 2 or local_freq[k] * 2 == len(old_data):
        keep_num = 1 if keep_common else 0
    else:
        keep_num = 0 if keep_common else 1

    new_data = [x for x in old_data if int(x[k]) == keep_num]
    if not new_data:
        raise
    elif len(new_data) == 1:
        return new_data[0]
    else:
        return bin_filter(new_data, keep_common, k + 1)


oxy = bin_2_dec(bin_filter(data, True))
co2 = bin_2_dec(bin_filter(data, False))

print(f"{oxy} * {co2} = {oxy * co2}")
