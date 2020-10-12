# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

import math


def no_math_solution():
    primes = [2, 3, 5, 7]
    primesSet = set(primes)
    truncatePrimes = []
    num = 11
    while(len(truncatePrimes) < 11):
        r = math.floor(math.sqrt(num))
        isPrime = True
        for p in primes:
            if(p > r):
                break
            if(num % p == 0):
                isPrime = False
                break
        if(isPrime):
            primes.append(num)
            primesSet.add(num)
            isTruncatePrime = True
            s = str(num)
            for i in range(len(s)):
                truncated = s[i:]
                if(int(truncated) not in primesSet):
                    isTruncatePrime = False
                    break
                truncated = s[:i+1]
                if(int(truncated) not in primesSet):
                    isTruncatePrime = False
                    break
            if(isTruncatePrime):
                truncatePrimes.append(num)
        num += 2
    return sum(truncatePrimes)


if __name__ == "__main__":
    print(no_math_solution())
