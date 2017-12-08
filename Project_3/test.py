import numpy as np

def get_lfsr_seq(register, cd, z, n):
    register = list(register)
    lfsr_out = []
    
    for i in range(n):
        feedback = 0
        for r, c, in zip(register, cd):
            feedback += r * c
        feedback = (z - feedback) % z
        
        lfsr_out.append(register.pop(0))
        register.append(feedback)
    
    return lfsr_out

keystream = '0001100100010100011110101101111010110000110011011011110101111001010011010101010100001000010111011011101000010000100110100000110111110110001001010011001010001000011010110010100011100011010001000'

# convert to a numpy array
keystream = np.array([int(k) for k in keystream])
n = len(keystream)

# connection_polynomials = [
    # [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    # [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    # [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]]
connection_polynomials = [[1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1]]

def to_binary_array(x, l):
    b = bin(x)[2:]
    r = [int(i) for i in b]
    while(len(r) < l):
        r = [0] + r
    return r

def correlation_value(a, b):
    return np.count_nonzero(a == b) / len(a)

def crack_lfsr(cd):
    correlation_values = []
    initial_states = []
    l = len(cd)
    
    for i in range(2**l):
        # convert int i to initial state of the register
        i = to_binary_array(i, l)
        
        # get the sequence for initial state i
        seq = get_lfsr_seq(i, cd, 2, n)
        seq = np.array(seq)
        
        # measure similarity between lfsr with input i and output keystream
        c = abs(.5 - correlation_value(seq, keystream))
        
        correlation_values.append(c)
        initial_states.append(i)
        
    return (initial_states, correlation_values)

key = []
for cd in connection_polynomials:
    init, corr = crack_lfsr(cd)
    print corr
    # add initial state with max correlation value to key
    key.append(init[corr.index(max(corr))])