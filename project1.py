import math
import random
import subprocess
from decimal import *

N = 184208651242126473140033

# Number of primes we are bounded by
B =700

L = 1000
# Number of solutions to have
Lvals = 700

testR = [225, 261, 291, 292, 317, 343, 413, 431, 458, 469, 473, 490]

factorBase = []
rValues = []
rFactors = []
rModValues=[]
binMatrix = []

r_dict=dict()


# Filenames 
# GaussBin input file
inputFile = "./matrixInput.txt"
descriptionExample = "./descriptionExample.txt"
# GaussBin outputfile
outputFile = "matrixOutput.txt"
# helper method to print matrix in readable way
def printMatrix(matrix):
    for row in matrix:
        print(' '.join(map(str,row)))

def readFile(s, n):
	# parsing file for primes up to n
	file = open(s)
	result = []
	parsing = True
	primeCount = 0;
	while(parsing):
		line = file.readline().strip()
		tmp = line.split(" ")
		for i in tmp:
			if(int(i) < n):
				result.append(int(i))
				primeCount = primeCount + 1
		if(int(tmp[0]) > n or primeCount > B):
			parsing = False
	file.close()

	return result

# contains primes up to N, for calculating factorization of numbers
primes = readFile("prim_2_24.txt", N)

# creating matrix of 1s and 0s corresponding to primes up to B
def createMatrix():

	# generating r values and placing in list

	for k in range (L):
		for j in range(k):
	#for i in range(len(testR)):
			if (len(r_dict) > Lvals ):
				return binMatrix
			#r = testR[i]
			r = math.floor(math.sqrt(k * N)) + j

			modVal = ((r * r) % N)
			
			# make factors
			dFactor = primeFactor(modVal)

			if (modVal == 0):
				continue
			factor = dFactor[0]
			power = dFactor[1]

			#make row
			row = [0 for prime in range(len(primes))]
			for col in range(len(primes)):
				for i in range(len(factor)):
					if(primes[col] == factor[i]):
						row[col] = power[i] % 2

			if(bSmooth(modVal) and (not tuple(row) in r_dict) ):
				binMatrix.append(row)
				row = tuple(row)

				r_dict[row] = [r, modVal, factor, power]
				"""
				print(r)
				print("modVal: %s" % modVal)
				print(factor)
				print(power)
				"""
			#print(r_dict[tuple(binMatrix[i])])	
			#printMatrix(binMatrix)
			#print(len(primes))
	return binMatrix
"""
# decide if number is b-smooth
def bSmooth(number):
	if(number == 1):
		return True
	for p in primes:
		if(number % p == 0):
			return bSmooth(number // p)
	return False

# creating matrix of 1s and 0s corresponding to primes up to B
def createMatrix():

	for k in range (2, B):
		rootNK = int(math.sqrt(N * k))

		for j in range (2, k):
			
			r = rootNK + j
			modVal = (r * r) % N

			if(bSmooth(modVal)):
				factors = primeFactor(modVal)
				
				# find binary representation of factors
				line = [0] * len(primes)

				# for each prime factor, set that bit in the line to 1
				for x in factors:
					line[primes.index(x)] = 1

				tLine = tuple(line)
				if not tLine in r_dict:
					r_dict[tLine] = [modVal, factors]
"""




# trial division using list of primes to find prime factorization of number
def primeFactor(n):
	result = []
	result2 = []
	# print(n)
	if (n == 0):
		return result
	for p in primes:
		# print(p)
		while(n % p == 0):
			n = n / p
			
			if p not in result:
				result.append(p)
				result2.append(1)
			else:
				result2[result.index(p)] += 1

			if (n <= 1):
				break
	# print(result)
	# print(result2)
	return [result, result2]

# decide if number is b-smooth
def bSmooth(n):
	if (n == 1):
		return True
	for f in primes:
		if (n % f == 0):
			return bSmooth(n//f)
	return False

def basicQuadraticSieve( N, xSqu, ySqu ):
	getcontext().prec = 2000
	
	"""
	x = int(Decimal.sqrt(Decimal(xSqu)))
	y = int(Decimal.sqrt(Decimal(ySqu)))
	"""
	x = xSqu
	y = ySqu

	if ( ((x * x) % N) == ( (y * y) % N)): 
		if (x == y):
			print("if")
			return False
		a = x+y
		b = N

		# Gets the gcd of N and x+y
		while ( 1 ):
			# Gets q given p which is gcd.
			if ( a == 0):
				if (b == 1 or b == N):
					return False
				p = b
				q = int(N/b)
				print ('p is ' + str(p) )
				print ('q is ' + str(q) )
				return True
			c = b % a
			b = a
			a = c
	return False
						

def createMatrixInput ( matrix ):

	M=len(matrix)
	N = len(matrix[0])
	file  = open(inputFile, "w")

	file.write(str(M) + " " + str(N) + "\n")
	for line in matrix:
		for item in line:
			if (item == 0 ):
				file.write( "%s "  % 0)
			else:
				file.write( "%s "  % 1)
		file.write("\n")
	file.close()

	return

# Generates a random matrix for testing
def generateRNG (M, N):
	seed(256)
	matrix = [ [ randint(0, 1) for x in range(M) ] for y in range(N) ]
	return matrix

# reads in the output file from GaussBin
def readMatrixOutput (filename):
	file = open(filename, "r")

	dimensions=file.readline()
	dim = dimensions.split()

	strMatrix = [ file.readline().split()  for i in range( int(dim[0])) ] 

	matrix = [ [int(i) for i in line] for line in strMatrix] 



	return matrix

# Wrapper for the GaussBin program
def GaussianElimination ():


	args = ["./a.out ./matrixInput.txt ./matrixOutput.txt"]

	subprocess.call( args, shell=True )
	
	return


""" Nick's Code - Working solution """

def sandBox():
	# newPowers = [ 0 for i in len(rArray[3]) ]
	powers = [i*2 for i in range(100)]
	newPowers = [0 for i in range(100)]
	for i in range(len(powers)):
		newPowers[i] = int(powers[i] / 2)
	#print(powers)
	#print(newPowers)

def createX(matrix, matrix2):
	running = True
	
	#Check each solution
	# Determines which lines in matrix1 to use
	for line in matrix2:

		# r values unmodded
		rVal = 1
		# r values modded
		rModTotal = 1

		rModHalf = 1

		factorDict = dict()

		
		# Multiply by each number specified
		# newPowers = [ 0 for j in range(len(rArray[3])) ]

		# Use this line in matrix1
		for col in range(len(line)):

			if (line[col] == 1):
				rArray = r_dict[tuple(matrix[col])]
				#print(rArray)
				# Make new powers for the factors
				"""
				print('set')
				print(rArray[1])
				print(rArray[2])
				print(rArray[3])
				"""
				# rArray 2 list of factors
				# rArray 3 list of multiplicities
				for j in range(len(rArray[2])):
					if rArray[2][j] not in factorDict:
						factorDict[rArray[2][j]] = rArray[3][j]
					else: 
						factorDict[rArray[2][j]] += rArray[3][j]
					#print(factorDict)
				#print(rArray[0])
				rVal *= rArray[0]
				rModHalf *= rArray[1]
				"""
				print(rArray[1])
				print(rArray[2])
				print(rArray[3])
				"""

		#print(factorDict)
		for key in factorDict:
			# print(factorDict[key]/2)
			for i in range(int(math.floor(factorDict[key]/2))):
				rModTotal *= key
		if(rModHalf != (rModTotal* rModTotal)) :
			# print("die")
			# print(factorDict)
			return
		# else:
			# print("win")
		#print(rModHalf % N)
		#print((rModTotal * rModTotal) % N)

		if (basicQuadraticSieve(N, rVal, rModTotal)):
			return


def proj1():
	matrix = createMatrix()
	createMatrixInput(matrix)
	GaussianElimination()
	matrix2 = readMatrixOutput(outputFile)
	createX(matrix,matrix2)
	return
#sandBox()
proj1()
