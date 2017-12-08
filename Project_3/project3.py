import itertools
import numpy

# assuming lfsr that pushes from the left side
keystream_sequence = "1010011010111100010001011110111001011011010011000011000110111100110001011011001001101011000010101100000000110010000111101101101101110001101111010001101001101101001001111111001101000010001100000"

# generating possible initial states for the lfsrs
L1_POSSIBLE = ["".join(seq) for seq in itertools.product("01", repeat=13)]
L2_POSSIBLE = ["".join(seq) for seq in itertools.product("01", repeat=15)]
L3_POSSIBLE = ["".join(seq) for seq in itertools.product("01", repeat=17)]

# representing connection polynomials
L1_POLYNOMIAL = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
L2_POLYNOMIAL = [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0]
L3_POLYNOMIAL = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

# helper method to calculate hamming distance between two strings
def calc_hamming(string_one, string_two):
    assert len(string_one) == len(string_two)
    return sum(s1 != s2 for s1, s2 in zip(string_one, string_two))

# C1(D) = 1 + D1 + D2 + D4 + D6 + D7 + D10 + D11 + D13
# C2(D)= 1 + D2 + D4 + D6 + D7 + D10 + D11 + D13 + D15
# C3(D)= 1 + D2 + D4 + D5 + D8 + D10 + D13 + D16 + D17j

# runs through LFSR depending on connection polynomial, returns string containing all added digits
def calc_sequence(seq, connection):
    reg = seq
    output = ""
    # print seq
    # testset = set()
    
    for i in range(len(keystream_sequence)):
        # print reg
        dig_new = 0

        for s, c in zip(reg, connection):
            # print s, c
            dig_new += s * c
        
        dig_new = dig_new % 2
        
        reg.pop(0)
        reg.append(dig_new)
        output += str(dig_new)
        # testset.add(str(reg))
        # print

    # print len(testset)==len(keystream_sequence)
    return output

def attack_keystream(cd):
    L1 = {}
    L2 = {}
    L3 = {}

    # go through each possible sequence
    for sequence in L1_POSSIBLE:
        output_seq = calc_sequence(map(int, list(sequence)), cd)


attack_keystream(L1_POLYNOMIAL)

# tmp = max(L1_RESULTS, key=L1_RESULTS.get)
# print tmp
# print L1_RESULTS[tmp]

# pprint.pprint(L1_RESULTS)
# lists = L1_RESULTS.items()
# x, y = zip(*lists)

# plt.plot(x, y, marker='.', linestyle='None', color='k', label='Test')
# plt.show()