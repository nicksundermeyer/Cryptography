import itertools
import matplotlib.pyplot as plt

# assuming lfsr that pushes from the right side
keystream_sequence = '1010011010111100010001011110111001011011010011000011000110111100110001011011001001101011000010101100000000110010000111101101101101110001101111010001101001101101001001111111001101000010001100000'
# keystream_sequence = '0001100100010100011110101101111010110000110011011011110101111001010011010101010100001000010111011011101000010000100110100000110111110110001001010011001010001000011010110010100011100011010001000'

# C1(D) = 1 + D1 + D2 + D4 + D6 + D7 + D10 + D11 + D13
# C2(D)= 1 + D2 + D4 + D6 + D7 + D10 + D11 + D13 + D15
# C3(D)= 1 + D2 + D4 + D5 + D8 + D10 + D13 + D16 + D17j

# representing connection polynomials
# reverse order polynomials
L1_POLYNOMIAL = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
L2_POLYNOMIAL = [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0]
L3_POLYNOMIAL = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

# forward order polynomials
# L1_POLYNOMIAL = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1]
# L2_POLYNOMIAL = [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1]
# L3_POLYNOMIAL = [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1]

# helper method to calculate hamming distance between two strings
def calc_hamming(list_one, list_two):
    assert len(list_one) == len(list_one)
    return float(sum(s1 != s2 for s1, s2 in zip(list_one, list_two)))

def int_to_list(input):
    result = []
    for digit in str(input):
        result.append(int(digit))
    return result

keystream_sequence = int_to_list(keystream_sequence)

# runs through LFSR depending on connection polynomial, returns string containing all added digits
def calc_sequence(seq, connection):
    reg = seq
    #print(reg)
    output = []
    # print seq
    # testset = set()
    for i in seq:
        output.append(i)
    
    for i in range(len(keystream_sequence)):
        # print(reg)
        dig_new = 0

        for s, c in zip(reg, connection):
            # print(s, c)
            dig_new += s * c
        
        dig_new = dig_new % 2
        
        reg.pop(0)
        reg.append(dig_new)
        output.append(dig_new)
        # print
        # testset.add(str(reg))

    # print()
    # print len(testset)==len(keystream_sequence)
    # print output
    # print
    return output
# def list_to_string(l):
# 	for i in l:
# 		print(str(i), end="")
# 	print("\n")
def attack_keystream(n, cd):
    possible = ["".join(seq) for seq in itertools.product("01", repeat=n)]
    for p in possible:
        p = int(p, 2)

    initial = []
    p = []
    # possible = ['1110101000101']
    # go through each possible sequence
    for sequence in possible:
        output_seq = calc_sequence(int_to_list(sequence), cd)
        hamming = calc_hamming(output_seq, keystream_sequence)

        correlation = 1 - (hamming/len(output_seq))
        # print correlation
        # if (correlation > max(p)):
        initial.append(sequence)
        p.append(abs(0.5 - correlation))
        # print(sequence, abs(0.5 - correlation))

    return initial, p

key = []

L1, L1_P = attack_keystream(13, L1_POLYNOMIAL)
L2, L2_P = attack_keystream(15, L2_POLYNOMIAL)
L3, L3_P = attack_keystream(17, L3_POLYNOMIAL)

# plotting points
# print(type(L1[0]))
# print(type(L1_P[0]))
# print(max(L1_P))
# print L1[L1_P.index(max(L1_P))]
# print
# print(min(L1_P))
# print L1[L1_P.index(min(L1_P))]
# plt.scatter(tmp, L1_P)
# plt.show()

# print L1_P

# print(max(L1_P))
key.append(L1[L1_P.index(max(L1_P))])
key.append(L2[L2_P.index(max(L2_P))])
key.append(L3[L3_P.index(max(L3_P))])

print (key)

# output ['0000000101010', '011011011111010', '11011100011111111']
# output 2 (test polynomials) ['0100110100001', '001111001100111', '01110101101100101']
# correct:  1010001010111, 101001111001000, 10000110111111000

# def check_keysequence(key):
# 	seq13 = calc_sequence(int_to_list(key[0]),L1_POLYNOMIAL)
# 	seq15 = calc_sequence(int_to_list(key[1]),L2_POLYNOMIAL)
# 	seq17 = calc_sequence(int_to_list(key[2]),L3_POLYNOMIAL)
# 	for idx in range(len(keystream_sequence)):
# 		checkVal = seq13[idx]+seq15[idx]+seq17[idx]
# 		if (checkVal < 2):
# 			print("0",end="")
# 		else:
# 			print("1",end="")
# 	print()	
# print("check keysequence")
# check_keysequence(key)

# print("test calc_sequence")
# print(calc_sequence([1,0,0,0],[1,0,0,1]))

# test1 = map(int, list(calc_sequence(map(int, list("0000000101010")), L1_POLYNOMIAL)))
# test2 = map(int, list(calc_sequence(map(int, list("011011011111010")), L2_POLYNOMIAL)))
# test3 = map(int, list(calc_sequence(map(int, list("11011100011111111")), L3_POLYNOMIAL)))

# result = []

# for a, b, c, in zip(test1, test2, test3):
    # if a+b+c > 2:
        # result.append(1)
    # else:
        # result.append(0)