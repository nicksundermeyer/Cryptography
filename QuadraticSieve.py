import subprocess
from random import *

# Basic Quadratic Sieve Function 
# Works for small numbers

# Version 1.0
# O(N^2)
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

	#
	filename="matrixInput.txt"
	file = open(filename, "r")

	dimensions=file.readline() 
	dim = dimensions.split()
	
	""" print matrix dimensions
	print("M: %s \n" % dim[0])
	print("N: %s" % dim[1])
	"""

	print("readMatrixOutput: \n")
	strMatrix = [ file.readline().split()  for i in range( int(dim[1])) ] 
	for i in strMatrix:
		print(i)
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
matrix = generateRNG(M, N)
# createMatrixInput(matrix)
GaussianElimination()
matrix2 = readMatrixOutput()
for i in range(M):
	if ( matrix[i] != matrix2[i]):
		print("Original matrix: \n")
		print ("%s \n" % matrix[i])
		print("readMatrixOutput: \n")
		print ( "%s \n\n" % matrix2[i])
