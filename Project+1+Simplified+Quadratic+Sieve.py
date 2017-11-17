
# coding: utf-8

# ## Project 1: Simplified Quadratic Sieve
# #### Group 14: Gonzalo Gómez and Evan Reierson

# In[33]:


# import some stuff
import math
import numpy as np
import os
import sympy
import seaborn as sns
import matplotlib.pyplot as plt
import time


# ### Exercise 1: Brute Force Trial Division
# The product of two 12-digit numbers is a 23 or 24-digit number, so we can assume that the factors are no larger than $10^{12}$.
# <br>
# Since we need to complete at most $10^{12}$ trial divisions to find a factor and we can do $10^6$ tests per second, it would take $10^6$ seconds, or about $11.6$ days, to factor the number. This time could be halved by simply avoiding even numbers.

# ### Exercise 2: Improved Trial Division
# Let's say we store all the prime numbers smaller than $\sqrt{10}\cdot 10^{12}$ in memory. There are about $\frac{3\cdot 10^{12}}{ln(3\cdot 10^{12})} = 10^{11}$ prime numbers, so using this "improved" trial division would take no more than $10^5 s = 1.2$ days to factor a 25-digit number, speeding the procces by a factor of about $ln(10^{12}) = 28$.
# <br>
# However, the memory required to store those primes would be about $10^{11}$ numbers times $ log_2 (3\cdot 10^{12}) = 42$ bits per number, that is, $4.2$ terabits or $0.5$ terabytes. This is the size of a big USB drive or a small hard drive, so it would not be too expensive. It is worth considering that the memory required grows more or less linearly with the size of the number to factor, and we could have sped up the trial division by a factor of 4 just by avoiding multiples of 2, 3, 5 and 7 as potential divisors.

# ### Exercise 3: Simplified Quadratic Sieve

# #### Import and initialize

# In[34]:


sns.set_style("darkgrid")

# load some primes
primes_to_10000 = np.loadtxt('prim_2_24.txt', delimiter='\t')
primes_to_10000 = primes_to_10000.flatten().astype(int)

# pick an n to factor where n=pq 
n = 196097436898174954190359
#n = 92434447339770015548544881401


# choose a factorbase maximum B
B = 2500

# get a factorbase with primes up to B and store its size
F = primes_to_10000[primes_to_10000 < B].tolist()
mag_F = len(F)


# #### Define some helper functions

# In[35]:


'''
iterate over factorbase looking for divisors and recursivly return
the quotient until n is 1 or there are no factors left in the factorbase
'''
def is_b_smooth(n, d={}):
    if (n == 1):
        return d
    for f in F:
        if (n % f == 0):
            if (f in d.keys()):
                d[f] += 1
            else:
                d[f] = 1
            return is_b_smooth(n//f, d)
    return False


# In[36]:


'''
write factorbase to a file that is readable by GaussBin.cpp
'''
def write_factors(factors):
    with open('gauss_input', 'w') as file:
        file.write('{} {}\n'.format(str(len(factors)), str(mag_F)))
        for r in factors:
            file.write(' '.join([str(x) for x in r]) + '\n')  


# In[37]:


'''
get the cumulative product of a list mod n
'''
def prodmod(a):
    p = 1
    for i in a:
        p *= i
        p %= n
    return int(p)


# #### Fill in the factor base

# In[38]:


ks = []
js = []

def get_factorbase():
    # successful r-values
    rs = []
    # successful factors
    factors = []
    # successful factors mod 2
    factors_mod2 = []

    for k in range(2,B):
        n_root_k = int(math.sqrt(k*n))
        for j in range(2, k):
            ks.append(k)
            js.append(j)
            
            # calculate likely b-smooth r value from j and k 
            r = n_root_k + j
            r2 = pow(r, 2) % n
            
            t = is_b_smooth(r2)
            # check if r^2 mod n is b smooth
            if (t):
                # get the factors
                #factorization = sympy.ntheory.factorint(r2)
                factorization = t
                factorbase_powers = [0] * mag_F
                
                # set the position in F to its corresponding power 
                for key in factorization:
                    factorbase_powers[F.index(key)] = factorization[key]
                
                factorbase_powers_mod2 = [x % 2 for x in factorbase_powers]
                
                # make sure the factorbase powers are valid
                if (sum(factorbase_powers) > 0 and
                    factorbase_powers_mod2 not in factors_mod2):
                    
                    # keep track of valid factors
                    factors.append(factorbase_powers)
                    factors_mod2.append(factorbase_powers_mod2)
                    rs.append(r)
                    
                    # return when we have enough factors
                    if (len(factors) >= mag_F + 5):
                        return factors, rs
    return factors, rs


# #### Check if the solutions from GaussBin.cpp give us a factor for n

# In[39]:


def check_solutions():
    for s in solutions:
        rs_in_solution = []
        
        # get r values corresponding to the solution vector
        for si, ri in zip(s, rs):
            if (si):
                rs_in_solution.append(ri)
        
        # get product of r's mod n
        r_prod_modn = prodmod(rs_in_solution)
        
        powers = [0] * mag_F
        
        for r in rs_in_solution:
            index = rs.index(r)
            # add powers in in factors for each r
            for i, f in enumerate(factors[index]):
                powers[i] += f
        
        # take out a power of 2
        powers = [x // 2 for x in powers]
        
        # sum all the factors in each r to their appropriate power
        right = []
        for f, p in zip(F, powers):
            right.append(pow(f, p))
        
        # get the product mod n
        right = prodmod(right)
        
        fac = math.gcd(right - r_prod_modn, n)
        
        if (fac > 1 and fac != n):
            return fac


# #### Run and measure execution time

# In[40]:


start_time = time.time()
factors, rs = get_factorbase()

# write file for GaussBin.cpp
write_factors(factors)

# run GaussBin.cpp
get_ipython().getoutput('./gauss1 gauss_input gauss_output')

# load solutions from GaussBin.cpp
solutions = np.loadtxt('gauss_output', skiprows=1, dtype=int)

f1 = check_solutions()
f2 = n // f1
ellapsed_time = time.time() - start_time

print('The factors of {} are {} and {}.'.format(n, f1, f2))
print('It took {} seconds to find the factors.'.format(ellapsed_time))


# #### Some fun stuff now

# In[ ]:


# reset values to something reasonable for displaying j and k
n = 307561
B = 30
F = primes_to_10000[primes_to_10000 < B].tolist()
mag_F = len(F)

ks = []
js = []
get_factorbase();


# In[ ]:


plt.plot(ks, js, linewidth=.5, marker='o', markersize=5)
plt.ylabel('j  values')
plt.xlabel('k  values')
plt.title('Getting j and k Values')
plt.show()


# In[ ]:


test_bs = list(range(1500, 6000, 500))
test_bs


# In[ ]:


# performance depending on B value
base_sizes = []
times = []
n = 196097436898174954190359
for B in test_bs:
    F = primes_to_10000[primes_to_10000 < B].tolist()
    mag_F = len(F)
    
    start_time = time.time()
    factors, rs = get_factorbase()
    write_factors(factors)
    get_ipython().getoutput('./gauss1 gauss_input gauss_output')
    solutions = np.loadtxt('gauss_output', skiprows=1, dtype=int)
    f1 = check_solutions()
    f2 = n // f1
    ellapsed_time = time.time() - start_time
    
    base_sizes.append(mag_F)
    times.append(ellapsed_time)


# In[ ]:


times


# In[ ]:


sns.barplot(test_bs, times)

plt.ylabel('Time in seconds')
plt.xlabel('B-smooth number')
plt.title('B Number and Completion time')

plt.show()


# ### Exercise 4: n = 92434447339770015548544881401

# In[ ]:


n = 92434447339770015548544881401
B = 8000
F = primes_to_10000[primes_to_10000 < B].tolist()
mag_F = len(F)

start_time = time.time()
factors, rs = get_factorbase()

# write file for GaussBin.cpp
write_factors(factors)

get_ipython().getoutput('./gauss1 gauss_input gauss_output')

# load solutions from GaussBin.cpp
solutions = np.loadtxt('gauss_output', skiprows=1, dtype=int)

f1 = check_solutions()
f2 = n // f1
ellapsed_time = time.time() - start_time

print('The factors of {} are {} and {}.'.format(n, f1, f2))
print('It took {} seconds to find the factors.'.format(ellapsed_time))

