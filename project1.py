import math
import random

N = 16637
B = 30
L = 60

factorBase = []
rValues = []
rFactors = []

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
    result = [[0 for x in range(B)] for x in range(B)]

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

def findValues():
    for j in range (0, L):
        for k in range (0, L):
            r = math.floor(math.sqrt(k * N)) + j
            if(bSmooth(r)):
                rValues.append(r)
    
    matrix = createMatrix()
    # print(matrix)

findValues()
# print(rFactors)
# print()
# print(rValues)
# print(rFactors)