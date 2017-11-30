from collections import deque
import os
from collections import Counter

# starting/current register
register2 = deque([1, 0, 0, 0])
register5 = deque([1, 0, 0, 0])

# final de bruijn sequences, in z2, z5, and z10
Z2 = []
Z5 = []
DeBruin = []

# make sure the current workign directory is in the project 2 folder, not the overall crypto folder
outputFile=os.getcwd() + "/Project_2/outputFile"

# lfsr shifts digits in from the right side
# create two de bruijn sequences, one of Z2 and one of Z5

# p(x) = x^4 + x + 1

Z2.append(1)
Z2.append(0)
Z2.append(0)
Z2.append(0)
Z5.append(1)
Z5.append(0)
Z5.append(0)
Z5.append(0)

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

test1 = []
for i in range(len(Z2)-3):
	test1.append(tuple([Z2[i], Z2[i+1], Z2[i+2], Z2[i+3]]))

file = open(outputFile, "w")

for i in range(len(Z2)):
	x = Z2[i]
	y = Z5[i]

	codeDigit = 2*y + x

	DeBruin.append(codeDigit)
	file.write("%s" % codeDigit)

test = []
for i in range(len(DeBruin)-3):
	test.append(tuple([DeBruin[i], DeBruin[i+1], DeBruin[i+2], DeBruin[i+3]]))

file.close()