# How many continued fractions for N <= 10000 have an odd period?

import math


def calculate_continued_fractions_of_n(n: int):
    cf = []
    r = math.isqrt(n)
    cf.append(r)
    if(r ** 2 == n):
        return cf
    numerator = n - r ** 2
    cf.append(2 * r // numerator)
    denominator = cf[0] - cf[1] * numerator
    while(numerator != 1):
        numerator = (n - denominator ** 2) / numerator
        r = (cf[0] - denominator) // numerator
        cf.append(r)
        denominator = math.fabs(denominator) - r * numerator
    return cf


def math_solution(n: int):
    return sum(1 for i in range(2, n+1) if (len(calculate_continued_fractions_of_n(i)) - 1) % 2 == 1)


if __name__ == "__main__":
    # n = int(input())
    n = 10_000
    print(math_solution(n))
