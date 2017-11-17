import math
import random
import subprocess
from decimal import *
import sympy

N = 392742364277

# Number of primes we are bounded by
B = 1000

L = 1000
# Number of solutions to have
Lvals = 1010

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
	for j in range (0, math.floor(Lvals)):
			for k in range (j):

				if (len(r_dict) > Lvals ):
					return binMatrix

				r = math.floor(math.sqrt(k * N)) + j

				modVal = (r * r) % N
				
				# make factors
				dFactor = primeFactor(modVal)

				factor = dFactor[0]
				power = dFactor[1]

				#make row
				row = [0 for prime in range(len(primes))]
				for col in range(len(primes)):
					if(primes[col] in factor):
						row[col] = factor.count(primes[col]) % 2

				if(bSmooth(factor) and (not tuple(row) in r_dict) ):
					binMatrix.append(row)
					row = tuple(row)

					r_dict[row] = [r, modVal, factor, power]
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

	if (n == 0):
		return result
	for p in primes:
		while(n % p == 0):
			n = n / p
			
			if p not in result:
				result.append(p)
				result2.append(1)
			else:
				result2[result.index(p)] += 1

			if (n <= 1):
				break

	return [result, result2]

# decide if number is b-smooth
def bSmooth(factor):
	
	
	if(max(factor, default=0) < primes[len(primes)-1] ) :
		return True
	else:
		return False

def basicQuadraticSieve( N, xSqu, ySqu ):
	getcontext().prec = 2000
	x = int(Decimal.sqrt(Decimal(xSqu)))
	y = int(Decimal.sqrt(Decimal(ySqu)))

	if ( ((xSqu) % N) == ( (ySqu) % N)): 
		if (x != y):
			print("Problems")
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
	print(powers)
	print(newPowers)
def createX(matrix, matrix2):
	running = True
	
	#Check each solution
	for line in matrix2:

		# r values unmodded
		rVal = 1
		# r values modded
		rModTotal = 1

		rModHalf = 1

		# Multiply by each number specified

		for i in range(len(line)):

			rArray = r_dict[tuple(matrix[i])]
			
			if(line[i] == 1):
				# Make new powers for the factors
				
				newPowers = [ 0 for i in range(len(rArray[3])) ]
				for i in len(rArray[3]):
					newPowers[i] = int(rArray[3][i] / 2)

				rVal *= rArray[0]

				for 
				rModTotal *= rArray[1]
			
		
		if (basicQuadraticSieve(N, rVal*rVal, rModTotal)):
			return


def proj1():
	matrix = createMatrix()
	createMatrixInput(matrix)
	GaussianElimination()
	matrix2 = readMatrixOutput(outputFile)
	createX(matrix,matrix2)
	return
sandBox()
# proj1()