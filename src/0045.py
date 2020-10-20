# Find the next triangle number that is also pentagonal and hexagonal.

import math


def is_triangle(n: int):
    r = math.floor(math.sqrt(n*2))
    return r*(r+1) == n*2


def is_pentagontal(n: int):
    delta = 1 + 24*n
    r = math.floor(math.sqrt(delta))
    if r**2 == delta:
        return (1 + r) % 6 == 0
    return False


def is_hexagonal(n: int):
    delta = 1 + 8*n
    r = math.floor(math.sqrt(delta))
    if r**2 == delta:
        return (1 + r) % 4 == 0
    return False


def no_math_solution(nth: int):
    count = 1  # 1 is the first number
    i = 2
    while(True):
        h = i*(2*i - 1)
        if(is_triangle(h) and is_pentagontal(h)):
            count += 1
            if(count == nth):
                break
        i += 1
    return i*(2*i - 1)


if __name__ == "__main__":
    print(no_math_solution(3))  # 1 is the first number
