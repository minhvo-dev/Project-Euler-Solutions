# What is the largest n-digit pandigital prime that exists?

import math


def is_prime(primes: list, n: int):
    r = math.floor(math.sqrt(n))
    isPrime = True
    for p in primes:
        if(p > r):
            break
        if(n % p == 0):
            isPrime = False
            break
    return isPrime


def get_primes_less_than_n(n: int):
    primes = [2]
    i = 3
    for i in range(3, n, 2):
        if(is_prime(primes, i)):
            primes.append(i)
    return primes


def get_pandigitals_max_n_digits(n: int):
    """Get all pandigital numbers that have no more than n digits

    Args:
        n (int): n must be from 1 to 9
    """
    pandigitals = ['1']
    last = ['1']
    for d in range(2, n+1):
        cur = []
        for num in last:
            s = str(num)
            nDigits = len(s)
            for i in range(0, nDigits+1):
                p = s[:i] + str(d) + s[i:]
                cur.append(p)

        pandigitals += cur
        last = cur
    return [int(p) for p in pandigitals]


def no_math_solution():
    primes = get_primes_less_than_n(math.floor(math.sqrt(1_000_000_000)))
    pandigitals = get_pandigitals_max_n_digits(9)
    maxPandigitals = 0
    for p in pandigitals:
        if(is_prime(primes, p)):
            maxPandigitals = maxPandigitals if maxPandigitals > p else p
    return maxPandigitals


if __name__ == "__main__":
    print(no_math_solution())
