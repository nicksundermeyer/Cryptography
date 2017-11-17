import math
import random
import subprocess


N = 457*673

# Number of primes we are bounded by
B = 1000
L = 10000

factorBase = []
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
			
		if(int(tmp[0]) > n or primeCount > 1000):
			parsing = False
	file.close()
	return result

# contains primes up to N, for calculating factorization of numbers
primes = readFile("prim_2_24.txt", N)

# creating matrix of 1s and 0s corresponding to primes up to B
def createMatrix():

	# generating r values and placing in list

	for j in range (0, math.floor(math.sqrt(L))):
		for k in range (0, math.floor(math.sqrt(L))):

			if (len(rValues) > 1000 ):
				break;

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

	# Tests factorization
	# print("prime: %s" % n)

	if (n == 0):
		return result
	for p in primes:
		while(n % p == 0):
			n = n / p
			result.append(p)

			if (n <= 1):
				break

	# Tests factorization
	# print("factors: %s \n" % result)
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
		# Debugging code 
		"""
		print('initials')
		print (a)
		print (b)
		"""

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
	
	# read single line of matrix output
	# file.readline()
	# strMatrix = file.readline().split()
	# matrix = [int(i) for i in strMatrix]
	
	""" print matrix dimensions
	print("M: %s \n" % dim[0])
	print("N: %s" % dim[1])
	"""
	# print("readMatrixOutput: \n")
	strMatrix = [ file.readline().split()  for i in range( int(dim[0])) ] 
	# for i in strMatrix:
	# 	print(i)
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
				# print("prime: " + str(i) + ": " + str(primes[i]))
				rVal *= rValues[i]
				#print(rFactors[i])
				for factor in rFactors[i]:
					rModTotal = ((rModTotal * factor ) % N)	
		# print(rVal % N)
		# print(int(math.sqrt(rModTotal) % N))
		if (basicQuadraticSieve(N, rVal, int(math.sqrt(rModTotal) % N) )):
			return


		# print(x)

		# Calculate gcd, if it's correct then return, otherwise continue the loop


# Testing function calls
# M=10
# N=10
# matrix = generateRNG(M, N)
# createMatrixInput(matrix)

# Create matrix of factored numbers.
# rValues = [225, 261, 291, 292, 317, 343, 413, 431, 458, 469, 473, 490]
matrix = createMatrix()

rValues=newRValues
rFactors=newRFactors

print(len(rValues))
print(len(rFactors))
# printMatrix(matrix)
# print()

# Creates input file for GaussBin
createMatrixInput(matrix)

# Runs Gauss Bin 
GaussianElimination()

# Reads the result of GaussBin
matrix = readMatrixOutput(inputFile)
matrix2 = readMatrixOutput(outputFile)

"""
#Debugging code
print("matrix")
printMatrix(matrix)
print("matrix2")
printMatrix(matrix2)
"""

# createSystem(matrix, matrix2)



# print(rValues)

createX(matrix, matrix2)
"""
print("rValues:")
print(rValues)
print("rFactors")
print(rFactors)
"""

# printMatrix(matrix2)

# DEBUGGING Prints the result of GaussBin
# printMatrix(matrix2)
# for i in range(M):
# 	if ( matrix[i] != matrix2[i]):
# 		print("Original matrix: \n")
# 		print ("%s \n" % matrix[i])
# 		print("readMatrixOutput: \n")
# 		print ( "%s \n\n" % matrix2[i])

# print(rFactors)
# print()
# print(rValues)
# print(rFactors)