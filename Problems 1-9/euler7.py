"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

"""
Method: Sieve of Eratosthenes

For the method, refer to the sieve of Eratosthenes which is surprisingly good at
finding primes up to a limit.

Fortunately, the limit here is 10,001.
"""
import math

limit = 10001
counter = 1 # 2 is prime so we start at 1 rather than 0

def isPrime(n):
    if n == 1:
        return False
    elif n < 4: # take 2, 3 and move straight onto 4
        return True
    elif n % 2 == 0:
        return False # skips 4, 6, 8
    elif n < 9: # takes 5, 7
        return True
    elif n % 3 == 0:
        return False
    else:
        # account for anything above 9. Recall that all primes > 3 can be written as 6k+1 or 6k-1.
        # recall also that is prime if there exists no prime factors < sqrt(n)
        r = math.sqrt(n) # r for real no., n for natural no.
        f = 5 # the next prime on the sieve
        while f <= r:
            if n % f == 0: # this is for the 6k - 1
                return False
                break
            elif n % (f+2) == 0: # this is for 6k + 1
                return False
                break
            f += 6 # increment by 6 for the 6k loop
        return True # if it passes both those cases then there are no factors meaning number is automatically prime

number = 1
while counter < limit:
    number += 2 # we're adding 2 to skip all even numbers, we already accounted for 2 on line 18
    if isPrime(number):
        counter += 1

print(number)
