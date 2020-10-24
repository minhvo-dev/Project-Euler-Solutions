# Which prime, below one-million, can be written as the sum of the most consecutive primes?


def get_sieve(n: int):
    sieve = [-1] * n
    for i in range(2, n):
        if(sieve[i] == -1):
            sieve[i] = 1
            for j in range(2 * i, n, i):
                sieve[j] = 0
    return sieve


def no_math_solution(n: int):
    sieve = get_sieve(n)
    accumulateSum = [0]  # first sum is 0

    for i in range(2, n):
        if(sieve[i] == 1):
            accumulateSum.append(accumulateSum[-1] + i)

    nSums = len(accumulateSum)
    longest = 0
    res = 0
    for i in range(1, nSums):
        for j in range(i + longest, nSums):
            diff = accumulateSum[j] - accumulateSum[i - 1]
            if(diff < n and sieve[diff] == 1):
                l = j - i + 1
                if(l > longest):
                    longest = l
                    res = diff

    return res


if __name__ == "__main__":
    # n = int(input())
    n = 1_000_000
    print(no_math_solution(n))
