# what is the side length of the square spiral
# for which the ratio of primes along both diagonals first falls below 10%?

import math


def is_prime(n: int):
    r = math.floor(math.sqrt(n))
    for i in range(2, r+1):
        if(n % i == 0):
            return False
    return True


def no_math_solution(threshold: float):
    last = 49
    total = 13
    sideLength = 7
    countPrime = 8
    while(total * threshold <= countPrime):
        sideLength += 2
        spirals = [last + i*(sideLength - 1) for i in range(1, 5)]
        total += 4
        countPrime += sum([1 for s in spirals if is_prime(s) == True])
        last = spirals[3]
    return sideLength


if __name__ == "__main__":
    print(no_math_solution(0.1))
