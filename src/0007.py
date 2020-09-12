# What is the 10001st prime number?

import math


def no_math_solution(n: int):
    """Calculate the n-th prime number

    Args:
        n (int): n-th

    Returns:
        int: n-th prime number
    """
    primes = [2]
    nPrime = 1
    i = 3
    while(nPrime != n):
        root = math.sqrt(i)
        isPrime = True
        for p in primes:
            if(i % p == 0):
                isPrime = False
                break
            if(p > root):
                break
        if(isPrime):
            primes.append(i)
            nPrime += 1
        i += 2
    return primes[n-1]


def math_solution():
    pass


if __name__ == "__main__":
    # n = int(input())
    n = 10001
    print(no_math_solution(n))
