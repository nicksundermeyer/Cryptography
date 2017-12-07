# Keystream Sequence to attack:
# 1010011010111100010001011110111001011011010011000011000110111100110001011011001001101011000010101100000000110010000111101101101101110001101111010001101001101101001001111111001101000010001100000
import pprint
import itertools
from collections import deque
import matplotlib.pyplot as plt

# assuming lfsr that pushes from the left side
keystream_sequence = "1010011010111100010001011110111001011011010011000011000110111100110001011011001001101011000010101100000000110010000111101101101101110001101111010001101001101101001001111111001101000010001100000"

# generating possible initial states for the lfsrs
L1_POSSIBLE = ["".join(seq) for seq in itertools.product("01", repeat=13)]
L2_POSSIBLE = ["".join(seq) for seq in itertools.product("01", repeat=15)]
L3_POSSIBLE = ["".join(seq) for seq in itertools.product("01", repeat=17)]

# dictionaries to hold results
L1_RESULTS = {}
L2_RESULTS = {}
L3_RESULTS = {}

def calc_hamming(string_one, string_two):
    assert len(string_one) == len(string_two)
    return sum(s1 != s2 for s1, s2 in zip(string_one, string_two))

# C1(D) = 1 + D1 + D2 + D4 + D6 + D7 + D10 + D11 + D13
# C2(D)= 1 + D2 + D4 + D6 + D7 + D10 + D11 + D13 + D15
# C3(D)= 1 + D2 + D4 + D5 + D8 + D10 + D13 + D16 + D17j

# runs through corret LFSR depending on length, returns output stream
def calc_sequence(seq):
    reg = deque(seq)
    output = ""
    
    for i in range(len(keystream_sequence)):
        if len(reg) == 13:
            dig_new = (int(reg[0]) + int(reg[1]) + int(reg[3]) + int(reg[5]) + int(reg[7]) + int(reg[9]) + int(reg[10]) + int(reg[12])) % 2
        elif len(reg) == 15:
            dig_new = (int(reg[1]) + int(reg[3]) + int(reg[5]) + int(reg[6]) + int(reg[9]) + int(reg[10]) + int(reg[12]) + int(reg[14])) % 2
        elif len(reg) == 17:
            dig_new = (int(reg[1]) + int(reg[3]) + int(reg[4]) + int(reg[7]) + int(reg[9]) + int(reg[12]) + int(reg[15]) + int(reg[16])) % 2
        
        reg.popleft()
        reg.append(dig_new)
        output += str(dig_new)

    return output

for sequence in L1_POSSIBLE:
    tmp = calc_sequence(sequence)
    L1_RESULTS[sequence] = (1 - (float(calc_hamming(tmp, keystream_sequence))/float(len(tmp))))

# tmp = max(L1_RESULTS, key=L1_RESULTS.get)
# print tmp
# print L1_RESULTS[tmp]

# pprint.pprint(L1_RESULTS)
lists = L1_RESULTS.items()
x, y = zip(*lists)

plt.plot(x, y, marker='.', linestyle='None', color='k', label='Test')
plt.show()