# How many circular primes are there below one million?

import math


def is_prime(primes: list, n: int):
    r = math.floor(math.sqrt(n))
    for i in primes:
        if(i > r):
            break
        if(n % i == 0):
            return False
    return True


def get_primes_less_than_n(n: int):
    primes = [2]
    for i in range(3, n, 2):
        if(is_prime(primes, i)):
            primes.append(i)
    return primes


def get_circular_rotations(n: int):
    rotations = []
    s = str(n)
    for i in range(len(s)):
        rotations.append(s[i:] + s[:i])
    return list(map(int, rotations))


def get_circular_primes_less_than_n(n: int):
    primes = set(get_primes_less_than_n(n))
    circularPrimes = []
    for p in primes:
        if(all(r in primes for r in get_circular_rotations(p))):
            circularPrimes.append(p)
    return circularPrimes


def no_math_solution():
    n = 1_000_000
    return len(get_circular_primes_less_than_n(n))


if __name__ == "__main__":
    print(no_math_solution())
