import math
import random
import subprocess
from decimal import *


N = 457*673

# Number of primes we are bounded by
B = 1000
L = 10000

table = [] # table to hold j, k, r, and r^2modn values
factorBase = []	#use set for factorbase when checking factors, faster checking time
rValues = []
rFactors = []
binMatrix = []

newRValues = []
newRFactors = []

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
	# parsing file for n primes
	file = open(s)
	result = []
	parsing = True
	
	while(parsing):
		tmp = file.readline().strip()
		line = tmp.split(" ")

		for i in line:
			result.append(int(i))

		if(len(result) > n):
			parsing = False

	file.close()
	return result

# contains primes up to a certain number, for quickly calculating prime factorization
primes = readFile("prim_2_24.txt", B)

# creating matrix of 1s and 0s corresponding to primes up to B
def createMatrix():

	# generating r values and placing in list

	for j in range (0, math.floor(math.sqrt(L))):
		for k in range (0, math.floor(math.sqrt(L))):

			if (len(rValues) > 1000 ):
				break;

			array = []
			r = math.floor(math.sqrt(k * N)) + j
			modVal = (r * r) % N
			
			# make factors
			factor = primeFactor(n)

			#make row

			row = [0 for prime in range(len(primes))]
			for col in range(len(primes)):
				if(prime[col] in factor):
					row[col] = factor.count(primes[col] % 2 )


			if(bSmooth( modVal) and (not row in binMatrix)):
				rValues.append(r)
				rFactors.append(factor)
				binMatrix.append(row)

	# Dummy Code to create the correct rFactors
	"""
	for r in rValues:
		modVal = (r * r) % N
		bSmooth( modVal)
	"""
	# creating matrix result
	result = []
	"""
	# check which factors are primes, set bits in matrix for those primes
	for x in range(len(rValues)):
		row = [0 for primes in range(len(primes))]
		for y in range(len(primes)):
			if(primes[y] in rFactors[x]):
				row[y] = (rFactors[x].count(primes[y]) % 2 )

		if not row in result:
			result.append(row)
			newRValues.append(x)
			newRFactors.append(rFactors[x])
	print("Number of Rs %s " % len(newRValues))
	# print(len(newRFactors))
	# print(len(result))
	print("Size of factorbase %s " % len(primes))

	# for x in range(len(rValues)):
	# 	for y in range(B):
	# 		# print(str(primes[y]) + " " + str(rFactors[y]) + " " + str(primes[y] in rFactors[y]))
	# 		# print("x: %s, y: %s" % (x, y))
	# 		# print ("factor: %s %s" %(primes[y], rFactors[x]) ) 
	# 		if(primes[y] in rFactors[x]):
	# 			# Very inefficient function below 

	# 			# print(str(x) + " " + str(y))
	# 			result[x][y] = (rFactors[x].count(primes[y]) % 2 )
	"""Debugging code
	print("result matrix: ")
	printMatrix(result)
	"""
	return result

# trial division using list of primes to find prime factorization of number
def primeFactor(n):
	result = []

	if (n == 0):
		return result
	for p in primes:
		while(n % p == 0):
			n = n / p
			result.append(p)

			if (n <= 1):
				break

	return result

# decide if number is b-smooth
def bSmooth(factor):
	
	"""
	print("prime: %s" % n)
	print("factors: %s" % factor)
	"""
	if(max(factor, default=0) < primes[len(primes)-1] ) :
		return True
	else:
		return False

def basicQuadraticSieve( N, x, y ):

	if ( ((x * x) % N) == ( (y * y) % N) and x != y): 
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
						
# Testing code
# basicQuadraticSieve(457 * 673)

# Add parameters later for matrix input 
def createMatrixInput ( matrix ):
	# Matrix Dimensions with dummy values

	# Test matrix

	# matrix2 = generateRNG(M,N)
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

	""" Debugging for matrixInput creator
	print("matrixInput.txt:")
	subprocess.call("cat matrixInput.txt", shell=True)
	print("\n")
	"""

	return

# reads in the output file from GaussBin
def readMatrixOutput (filename):
	file = open(filename, "r")

	dimensions=file.readline()
	dim = dimensions.split()
	
	# read single line of matrix output
	# file.readline()
	# strMatrix = file.readline().split()
	# matrix = [int(i) for i in strMatrix]
	
	""" print matrix dimensions
	print("M: %s \n" % dim[0])
	print("N: %s" % dim[1])
	"""

	strMatrix = [ file.readline().split()  for i in range( int(dim[0])) ] 
	matrix = [ [int(i) for i in line] for line in strMatrix] 

	""" Print input matrix
	for line in matrix:
		print("%s \n" % line)
	"""

	return matrix

# Wrapper for the GaussBin program
def GaussianElimination ():

	""" Testing code """
	# args = ["./a.out "+ descriptionExample + " " + outputFile]

	""" Final code """
	args = ["./a.out ./matrixInput.txt ./matrixOutput.txt"]

	subprocess.call( args, shell=True )
	""" Debug code
	print("matrixOutput.txt")
	subprocess.call( ["cat", "matrixOutput.txt"])
	"""
	return
""" Sebastian's Code
# systems the actual r values we use to create an x^2 value
# indicator equations from the system to actually use.
# Dependency: Uses the global variable primes (first N primes)
def createSystem (systems, indicator):
	# printMatrix(systems)
	for prime in systems:
"""
"""
		print("prime:")
		print(prime)
"""
"""
		# print(inversePrime(prime))

# Convert a matrix row to a 
def inversePrime (row):
	primeNum=1
	# print("prime")
	# print(row)
	for i in range(len(row)):
		if(row[i] == 1):
			
			# print("prime %s: %s" % (i, primes[i]))
			
			primeNum = primeNum * primes[i]
	# print()
	return primeNum

"""

""" Nick's Code - Working solution """

def createX(matrix, matrix2):
	running = True
	
	#Check each solution
	for line in matrix2:

		# r values unmodded
		rVal = 1
		# r values modded
		rModTotal = 1

		# print(line)
		# Multiply by each number specified
		for i in range(0, len(line)):
			if(line[i] == 1):
				rVal = (rVal * rValues[i]) % N
				for factor in rFactors[i]:
					rModTotal = rModTotal * factor	

		# use decimal for square root to avoid overflow
		dec = Decimal(rModTotal)
		if (basicQuadraticSieve(N, rVal, int(Decimal.sqrt(dec)) % N)):
			return


# Testing function calls

# Create matrix of factored numbers.
matrix = createMatrix()

# rValues=newRValues
# rFactors=newRFactors

# print(rValues)
# print()
# print(rFactors)

# Creates input file for GaussBin
createMatrixInput(matrix)

# Runs Gauss Bin 
GaussianElimination()

# Reads the result of GaussBin
matrix = readMatrixOutput(inputFile)
matrix2 = readMatrixOutput(outputFile)

createX(matrix, matrix2)

# DEBUGGING Prints the result of GaussBin
# printMatrix(matrix2)
# for i in range(M):
# 	if ( matrix[i] != matrix2[i]):
# 		print("Original matrix: \n")
# 		print ("%s \n" % matrix[i])
# 		print("readMatrixOutput: \n")
# 		print ( "%s \n\n" % matrix2[i])