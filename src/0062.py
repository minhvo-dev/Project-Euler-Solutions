# Find the smallest cube for which exactly five permutations of its digits are cube.

import math


def convert_number_to_digit_count(n: int):
    c = [0] * 10
    while(n > 0):
        c[n % 10] += 1
        n = n // 10
    return c


def no_math_solution(nP: int):
    found = -1
    nDigits = 1
    n = 1
    while(found == -1):
        upperBound = (10**nDigits) ** (1 / 3)
        cubes = []
        while(n < upperBound):
            cubes.append(n ** 3)
            n += 1
        digitCounts = [convert_number_to_digit_count(i) for i in cubes]
        nCubes = len(digitCounts)
        for i in range(nCubes):
            count = 1
            for j in range(i + 1, nCubes):
                if(digitCounts[i] == digitCounts[j]):
                    count += 1
            if(count == nP):
                found = i
                break
        if(found != -1):
            found = cubes[i]
        nDigits += 1
    return found


if __name__ == "__main__":
    print(no_math_solution(5))
