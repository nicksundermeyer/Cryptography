import math

N = 77
B = 30

primes = []
values = []

def readFile():
    # parsing file for prime primes up to B
    file = open("prim_2_24.txt")
    parsing = True
    while(parsing):
        line = file.readline().strip()
        tmp = line.split(" ")
        for i in tmp:
            if(int(i) < B):
                primes.append(int(i))
            
        if(int(tmp[0]) > B):
            parsing = False
    file.close()

def findValues():
    for j in range (0, N):
        for k in range (0, N):
            r = math.floor(math.sqrt(k * N)) + j
            values.append(r)

findValues()