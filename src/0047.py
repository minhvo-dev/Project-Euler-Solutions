# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

import math


def get_primes_less_than_n(n: int):
    primes = [2]
    for i in range(3, n, 2):
        r = math.floor(math.sqrt(i))
        isPrime = True
        for p in primes:
            if(p > r):
                break
            if(i % p == 0):
                isPrime = False
                break
        if(isPrime):
            primes.append(i)
    return primes


def get_factor_set(n: int, primes: list):
    factors = set()
    for p in primes:
        if(n % p == 0):
            factors.add(p)
            while(n % p == 0):
                n //= p
        if(n == 1):
            break
    return factors


def no_math_solution(nC: int, nF: int):
    nums = list(range(2, nC+2))
    primes = get_primes_less_than_n(1_000_000)
    l = [get_factor_set(n, primes) for n in nums]
    while(True):
        found = True
        for fs in l:
            if(len(fs) != nF):
                found = False
                break
        if(found == True):
            break
        # find the first n in nums that all nums follow n have 4 distinct factors
        # except the first number (infinite loop)
        i4 = nF
        while(len(l[i4 - 1]) == nF):
            i4 -= 1

        if(i4 == nF):
            # all previous numbers do not have nF distinct factors
            # update all
            nums = [nums[nC-1] + i for i in range(1, nC+1)]
            l = [get_factor_set(n, primes) for n in nums]
        else:
            # found
            # update the rest but not the number
            nums = [nums[i4]+i for i in range(0, nC)]
            for i in range(i4, nC):
                l[i - i4] = l[i]

            for i in range(0, i4):
                l[nC-i4+i] = get_factor_set(nums[nC-i4+i], primes)

    return nums[0]


if __name__ == "__main__":
    print(no_math_solution(4, 4))
