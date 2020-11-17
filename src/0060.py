# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

import math


def get_sieve(n: int):
    sieve = [-1] * (n + 1)
    for i in range(2, n+1):
        if(sieve[i] == -1):
            sieve[i] = 1
            for j in range(2*i, n+1, i):
                sieve[j] = 0
    return sieve


def is_prime(n: int, sieve: list):
    l = len(sieve)
    if(n < l):
        return sieve[n] == 1

    r = math.floor(math.sqrt(n))
    for i in range(2, r+1):
        if(sieve[i] == 1 and n % i == 0):
            return False
    return True


def concat_two_numbers(a: int, b: int):
    a = str(a)
    b = str(b)
    return [int(a + b), int(b + a)]


def get_pair_prime_list_of_n(n: int, sieve: list):
    ret = []
    for i in range(n, len(sieve)):
        if(sieve[i] == 1):
            if(all(is_prime(c, sieve) for c in concat_two_numbers(n, i))):
                ret.append(i)
    return ret


def get_pair_primes(sieve: list):
    return {x: set(get_pair_prime_list_of_n(x, sieve)) for x in range(3, len(sieve)) if sieve[x] == 1}


def recursive(primes: list, sieve: list, pair_primes: dict):
    if(len(primes) == 5):
        return primes
    for i in range(primes[-1], len(sieve)):
        if(sieve[i] == 1):
            makeASet = True
            for p in primes:
                if(i not in pair_primes[p]):
                    makeASet = False
                    break
            if(makeASet):
                primes.append(i)
                res = recursive(primes, sieve, pair_primes)
                if(len(res) == 5):
                    return res
                primes.remove(i)
    return []


if __name__ == "__main__":
    sieve = get_sieve(10000)
    pair_primes = get_pair_primes(sieve)
    for i in range(3, len(sieve)):
        if(sieve[i] == 1):
            res = recursive([i], sieve, pair_primes)
            if(len(res) == 5):
                print(res)
                break
