import subprocess

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

					print('initials')
					print (a)
					print (b)
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
def createMatrixInput ():
	# Matrix Dimensions with dummy values
	M = 10
	N = 10

	# Matrix to
	matrix = [ [ (x-y) % 2 for x in range(M) ] for y in range(N) ]
	print(str(matrix))
	line1 = [ 0, 1, 2, 3, 4 ]
	file  = open("matrixInput.txt", "w")

	file.write(str(M) + " " + str(N) + "\n")
	for line in matrix:
		for item in line:
			file.write( "%s "  % item )
		file.write("\n")
	file.close()
	return



def GaussianElimination ():
	print("\n\n\n")
	args = ["~/Desktop/EDIN01/Project1/GaussBin.exe", "matrixInput.txt", "matrixOutput.txt"]
	subprocess.call( args, shell=True )
	return

createMatrixInput()
GaussianElimination()