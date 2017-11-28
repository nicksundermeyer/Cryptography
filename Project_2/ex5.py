from collections import deque

# starting/current register
register = deque([0, 0, 0, 1])

# final de bruijn sequences, in z2, z5, and z10
Z2 = []
Z5 = []
Z10 = []

# lfsr shifts digits in from the right side
# create two de bruijn sequences, one of Z2 and one of Z5

# p(x) = x^4 + x + 1

generating Z2
while(not register in Z2):
    Z2.append(register.copy())

    # adding only registers 1 and 4
    x = (register[0] + register[3])%2
    
    if(register == deque([1, 0, 0, 0])):
        register.popleft()
        register.append(0)
    elif(register == deque([0, 0, 0, 0])):
        register.popleft()
        register.append(1)
    else:
        register.popleft()
        register.append(x)

register = deque([0, 0, 0, 1])

# C(D) = 1 + 2D + 2D^3 + 2D^4

while(not register in Z5):
    Z5.append(register.copy())

    # adding registers 1, 3, 4 multiplied by their coefficients and mod 5
    x = (2*register[0] + 2*register[1] + 2*register[3])%5

    print(str(2*register[0]) + "+" + str(2*register[1]) + "+" + str(2*register[3]) + " = " + str(2*register[0] + 2*register[1] + 2*register[3]) + "mod5 = " + str(x))
    print(register)
    print()

    register.popleft()
    register.append(x)
print(len(Z5))