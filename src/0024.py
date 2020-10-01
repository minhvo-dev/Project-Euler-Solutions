# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools
import math

def no_math_solution(nth: int):
    # generate permutations and count
    count = 0
    for perm in itertools.permutations(range(0, 10)):
        count += 1
        if(count == nth):
            return list(perm)
    return list(range(0, 10))

def math_solution(nth: int):
    perm = [0] * 10
    digits = list(range(0, 10))
    nth -= 1 # convert to zero-indexed base
    for i in range(0, 10):
        p = math.perm(10 - i - 1) # number of permutations from n items
        perm[i] = digits[nth // p]
        nth = nth % p
        digits.remove(perm[i])
    return perm



if __name__ == "__main__":
    # n = int(input())
    n = 1_000_000
    print(math_solution(n))
    print(no_math_solution(n))