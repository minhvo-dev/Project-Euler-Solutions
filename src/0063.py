# How many n-digit positive integers exist which are also an nth power?

import math


def get_total_n_digit_number_equal_n_power(n: int):
    lower = math.ceil((10**(n-1)) ** (1/n))
    return 9 - lower + 1 if lower < 10 else 0


def math_solution():
    i = 1
    total = 0
    r = get_total_n_digit_number_equal_n_power(i)
    while(r > 0):
        total += r
        i += 1
        r = get_total_n_digit_number_equal_n_power(i)
    return total


if __name__ == "__main__":
    print(math_solution())
