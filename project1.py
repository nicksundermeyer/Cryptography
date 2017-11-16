import math
import random
import subprocess

N = 16637
B = 30
L = 60

factorBase = []
rValues = []
rFactors = []

# helper method to print matrix in readable way
def printMatrix(matrix):
    for row in matrix:
        print(' '.join(map(str,row)))

def readFile(s, n):
    # parsing file for primes up to n
    file = open(s)
    result = []
    parsing = True
    while(parsing):
        line = file.readline().strip()
        tmp = line.split(" ")
        for i in tmp:
            if(int(i) < n):
                result.append(int(i))
            
        if(int(tmp[0]) > n):
            parsing = False
    file.close()
    return result

# contains primes up to N, for calculating factorization of numbers
primes = readFile("prim_2_24.txt", N)

# creating matrix of 1s and 0s corresponding to primes up to B
def createMatrix():
    # generating r values and placing in list
    for j in range (0, L):
        for k in range (0, L):
            r = math.floor(math.sqrt(k * N)) + j
            if(bSmooth(r)):
                rValues.append(r)

    # creating matrix result
    result = [[0 for x in range(B)] for x in range(B)]

    # check which factors are primes, set bits in matrix for those primes
    for x in range(B):
        for y in range(B):
            # print(str(primes[y]) + " " + str(rFactors[y]) + " " + str(primes[y] in rFactors[y]))
            if(primes[y] in rFactors[x]):
                # print(str(x) + " " + str(y))
                result[x][y] = 1
    
    return result

# trial division using list of primes to find prime factorization of number
def primeFactor(n):
    result = []
    for p in primes:
        if(n % p == 0):
            result.append(p)
    return result

# decide if number is b-smooth
def bSmooth(n):
    factor = primeFactor(n)
    if(max(factor, default=0) < B):
        rFactors.append(factor)
        return True
    else:
        return False

def basicQuadraticSieve( N ):
	print(N)
	for x in range(1, N):
		for y in range(1, N):
			if ( (x * x) == ( (y * y) % N) and x != y): 
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
						if ( a == 0 ):
							p = b
							q = N/b
							print ('p is ' + str(p) )
							print ('q is ' + str(q) )
							return
						c = b % a
						b = a
						a = c
						
# Testing code
# basicQuadraticSieve(457 * 673)

# Add parameters later for matrix input 
def createMatrixInput ( matrix ):
	# Matrix Dimensions with dummy values

	# Test matrix

	# matrix2 = generateRNG(M,N)
	M=len(matrix)
	N = len(matrix[0])
	line1 = [ 0, 1, 2, 3, 4 ]
	file  = open("matrixInput.txt", "w")

	file.write(str(M) + " " + str(N) + "\n")
	for line in matrix:
		for item in line:
			if (item == 0 ):
				file.write( "%s "  % 1)
			else:
				file.write( str(0) + " " )
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
def readMatrixOutput ():
	filename="matrixOutput.txt"
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
	args = ["./a.out ./matrixInput.txt ./matrixOutput.txt"]
	subprocess.call( args, shell=True )
	""" Debug code
	print("matrixOutput.txt")
	subprocess.call( ["cat", "matrixOutput.txt"])
	"""
	return

# Testing function calls
M=10
N=10
# matrix = generateRNG(M, N)
# createMatrixInput(matrix)
matrix = createMatrix()
# printMatrix(matrix)
# print()
createMatrixInput(matrix)
GaussianElimination()
matrix2 = readMatrixOutput()
printMatrix(matrix2)
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