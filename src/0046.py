# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import math


def is_prime(n: int, primes: list):
    r = math.floor(math.sqrt(n))
    isPrime = True
    for p in primes:
        if(p > r):
            break
        if(n % p == 0):
            isPrime = False
            break
    return isPrime


def no_math_solution():
    primes = [2]
    primeSet = set(primes)
    i = 3
    comp = -1
    while(comp < 0):
        if(is_prime(i, primes)):
            primes.append(i)
            primeSet.add(i)
        else:
            j = 1
            dif = i - 2*(j**2)
            found = False
            while(dif > 0):
                if(dif in primeSet):
                    found = True
                    break
                j += 1
                dif = i - 2*(j**2)
            if(found == False):
                comp = i
        i += 2
    return comp


if __name__ == "__main__":
    print(no_math_solution())
