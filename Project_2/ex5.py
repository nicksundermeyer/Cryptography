from collections import deque
import os
from collections import Counter

# tracking registers for Z2 and Z5
register2 = deque([1, 0, 0, 0])
register5 = deque([1, 0, 0, 0])

# final de bruijn sequences, Z2, and Z5
Z2 = []
Z5 = []
DeBruin = []

# make sure the current workign directory is in the project 2 folder, not the overall crypto folder
outputFile=os.getcwd() + "/Project_2/outputFile"

# appending starting values to de Bruijn sequences
Z2.append(1)
Z2.append(0)
Z2.append(0)
Z2.append(0)
Z5.append(1)
Z5.append(0)
Z5.append(0)
Z5.append(0)

"""
This loop creates the de Bruijn sequences in Z2 and Z5
Using our two primitive polynomials p(x) = x^4 + x + 1 and p(x) = 3x^4 + 2x^2 + 2x + 1
We use an LFSR which shifts digits in from the right side
Each iteration of the loop, we append the newly added digit to our Z2/Z5 lists and shift the register
We also check for the special case 1000 and shift in a 0 to add the 0000 case to our sequence, making it a de Bruijn sequence
"""
for i in range(9999):
	# Creating Z2
	a = (register2[0] + register2[3])%2

	if(register2 == deque([1, 0, 0, 0])):
		register2.popleft()
		register2.append(0)
		Z2.append(0)
	elif(register2 == deque([0, 0, 0, 0])):
		register2.popleft()
		register2.append(1)
		Z2.append(1)
	else:
		register2.popleft()
		register2.append(a)
		Z2.append(a)

	# Creating Z5
	b = (3*register5[0] + 2*register5[2] + 2*register5[3])%5

	if(register5 == deque([1, 0, 0, 0])):
		register5.popleft()
		register5.append(0)
		Z5.append(0)
	elif(register5 == deque([0, 0, 0, 0])):
		register5.popleft()
		register5.append(3)
		Z5.append(3)
	else:
		register5.popleft()
		register5.append(b)
		Z5.append(b)

file = open(outputFile, "w")

"""
Here is where we map Z2 and Z5 to Z10 to create the final de Bruijn sequence and write it to the file
We go through each element of Z2 and Z5, and then map them to a digit in Z10 with (2 * element of Z5) + (element of Z2)
Append each digit to the final sequence, write to file
"""
for i in range(len(Z2)):
	x = Z2[i]
	y = Z5[i]

	codeDigit = 2*y + x

	DeBruin.append(codeDigit)
	file.write("%s" % codeDigit)

file.close()