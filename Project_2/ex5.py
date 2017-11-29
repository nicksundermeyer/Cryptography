from collections import deque

# starting/current register
register = deque([0, 0, 0, 1])

# final de bruijn sequences, in z2, z5, and z10
Z2 = []
Z5 = []
Z10 = []
Codes = []
DeBruin = []

outputFile="outFile.txt"

# lfsr shifts digits in from the right side
# create two de bruijn sequences, one of Z2 and one of Z5

# p(x) = x^4 + x + 1

# generating Z2
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

register = deque([1, 0, 0, 0])

# C(D) = 1 + 2D + 2D^3 + 2D^4

while(not register in Z5):
    Z5.append(register.copy())

    # adding registers 1, 3, 4 multiplied by their coefficients and mod 5
    x = (3*register[0] + 2*register[2] + 2*register[3])%5

    # print(str(2*register[0]) + "+" + str(2*register[1]) + "+" + str(2*register[3]) + " = " + str(2*register[0] + 2*register[1] + 2*register[3]) + "mod5 = " + str(x))
    # print(register)
    # print()

    if(register == deque([1, 0, 0, 0])):
        register.popleft()
        register.append(0)
    elif(register == deque([0, 0, 0, 0])):
        register.popleft()
        register.append(3)
    else:
        register.popleft()
        register.append(x)
print(len(Z5))

firstThree=0

file = open(outputFile, "w")

for x in Z2:
	for y in Z5:
		digit=0
		base=1
		for index in range(len(y)):
			codeDigit = x[index]*5 + y[index]
			if ( firstThree < 3):
				DeBruin.append(codeDigit)
				file.write("%s" % codeDigit)
				firstThree += 1
			digit += codeDigit* base
			base *= 10
			Codes.append(digit)
		codeDigitOuter = x[3] * 5 + y[3]
		DeBruin.append(codeDigitOuter)
		file.write("%s" % codeDigitOuter)
		print("%04d" %(digit,))
file.close()
print(len(DeBruin))