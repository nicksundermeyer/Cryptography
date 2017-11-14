# Basic Quadratic Sieve Function 
# Works for small numbers

# Version 1.0
# O(N^2)
def basicQuadraticSieve( N ):
	for x in range(0, N)
		for y in range(0, N)
			if ((x - y)*(x + y) % N) == 0
				print(x-y)
				print(x+y)
