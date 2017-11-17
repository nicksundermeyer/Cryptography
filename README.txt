Exercise 1:

In our best case scenario we have to process, sqrt(N) numbers. So (10^25)^(.5) = (10^12.5). We can perform 1 million of these calculations per second which is (10^12.5)/(10^6) = (10^6.5), which is about 3 million seconds or 36 days.

Exercise 2:


The number of primes less than (10^12.5) is lower bounded by x/ln(x) so (10^12.5)/ln(10^12.5) ~= 10^11 which is about 109 billion numbers. 1.09x10^11 number will take about 10^5 seconds or 1 day to complete. Using 64 bit unsigned encoding we would need 8 * 109 = 872 billion bytes of storage to implement this improvement. This is equivalent to about 2^40 in base two which is around a terabyte of storage.  
This is about 261.25 ￡ on the provided website.

Exercise 3: 

N=184208651242126473140033 should factorize to 
p is 388117391953
q is 474620965361.

It takes 148.16 seconds to find this answer.
Sample Output:
-------------------------------------------------------------------
Rejected rows: 0
The number of solutions is too many (2^28) ... trancated to 2^12!
p is 388117391953
q is 474620965361
-------------------------------------------------------------------

We will look to optimize the code more before the presentation. Especially with regards to our factoring algorithms for our R values.



Exercise 5: 

Time to finish 15 hours. 
