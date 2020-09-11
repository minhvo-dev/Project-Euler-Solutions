# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def no_math_solution(n: int):
    root = math.floor(math.sqrt(n))
    maxP = 1
    p = 2
    if(n % p == 0):
        maxP = p
        while(n % p == 0):
            n = n // p
    p = 3
    while(p <= root):
        if(n % p == 0):
            maxP = p
            while(n % p == 0):
                n = n // p
        p += 2
    if(maxP == 1):
        # n is prime number so it is the largest prime factor
        return n
    # return the largest prime factor
    return maxP if maxP > n else n


def math_solution():
    pass


if __name__ == "__main__":
    # n = int(input())
    n = 600_851_475_143
    print(no_math_solution(n))
