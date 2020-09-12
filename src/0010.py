# Find the sum of all the primes below two million.

import math


def no_math_solution(n: int):
    """Calculate the sum of all the primes below n

    Args:
        n (int): max value

    Returns:
        int: sum of all primes
    """
    primes = [2]
    i = 3
    while(i < n):
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
        i += 2
    return sum(primes)


def math_solution():
    pass


if __name__ == "__main__":
    # n = int(input())
    n = 2_000_000
    print(no_math_solution(n))
