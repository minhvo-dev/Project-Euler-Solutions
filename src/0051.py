# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

import math


def is_prime(n: int, primes: tuple):
    r = math.floor(math.sqrt(n))
    if(r > primes[-1]):
        print("is_prime: root > max")
    isPrime = True
    for p in primes:
        if(p > r):
            break
        if(n % p == 0):
            isPrime = False
            break
    return isPrime


def get_primes_less_than_n(n: int):
    primes = [2]
    for i in range(3, n, 2):
        if(is_prime(i, primes)):
            primes.append(i)
    return primes


def binary_search(arr: list, left: int, right: int, value: int):
    if(left > right):
        return -1
    mid = left + (right - left) // 2
    if(arr[mid] == value):
        return mid
    if(arr[mid] > value):
        return binary_search(arr, left, mid - 1, value)
    return binary_search(arr, mid + 1, right, value)


def get_digit_positions(n: int):
    count = {
        '0': [],
        '1': [],
        '2': [],
        '3': [],
        '4': [],
        '5': [],
        '6': [],
        '7': [],
        '8': [],
        '9': []
    }
    s = str(n)
    for i in range(len(s)):
        count[s[i]].append(i)
    return count


def get_combination_list(arr: list):
    N = len(arr)
    if(N == 2):
        return [arr]
    comb = []
    for i in range(2**N):
        tmp = []
        for j in range(N):
            if(i >> j) % 2 == 1:
                tmp.append(arr[j])
        comb.append(tmp)
    return comb


def get_family_numbers(n: int, pos: list):
    family = []
    for i in range(10):
        l = list(str(n))
        for p in pos:
            l[p] = str(i)
        ss = "".join(l)
        if(ss[0] != '0' and int(ss) <= n):
            family.append(int(ss))
    return family


def no_math_solution():
    primes = get_primes_less_than_n(56000)
    n = 56001
    found = 0
    while(found == 0):
        if(is_prime(n, primes)):
            primes.append(n)
            pos = get_digit_positions(n)
            for i in range(7, 10):
                d = str(i)
                if(len(pos[d]) > 1):
                    comb = [c for c in get_combination_list(
                        pos[d]) if len(c) >= 2]
                    for c in comb:
                        family = get_family_numbers(n, c)
                        if(len(family) >= 8):
                            count = 0
                            smallest = -1
                            for f in family:
                                if(binary_search(primes, 0, len(primes) - 1, f) != -1):
                                    count += 1
                                    if(smallest == -1):
                                        smallest = f
                            if(count == 8):
                                found = smallest
        n += 2
    return found


if __name__ == "__main__":
    print(no_math_solution())
