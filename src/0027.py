# Considering quadratics of the form: n^2 + an + b where |a| < 1000, |b| < 1000
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with.

import math


def is_prime(n: int, primes: list):
    root = math.floor(math.sqrt(n))
    res = True
    for i in primes:
        if(i > root):
            break
        if(n % i == 0):
            res = False
            break
    return res


def prepare_primes(n: int):
    primes = [2]
    for i in range(3, n, 2):
        if(is_prime(i, primes)):
            primes.append(i)
    return primes


def cal_value(a: int, b: int, n: int):
    return n**2 + a*n + b


def no_math_solution():
    primes = prepare_primes(cal_value(1000, 1000, 1000))

    maxNumberPrimes = 0
    p = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):        
                n = 0
                v = cal_value(a, b, n)
                nPrimes = 0
                while(v > 1 and is_prime(v, primes)):
                    nPrimes += 1
                    n += 1
                    v = cal_value(a, b, n)
                if(nPrimes > maxNumberPrimes):
                    maxNumberPrimes = nPrimes
                    p = a * b

    return p


if __name__ == "__main__":
    print(no_math_solution())