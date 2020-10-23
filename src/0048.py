# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


def get_last_10_digits_of_power(n: int, e: int):
    p = 1
    c = 10**10
    for i in range(e):
        p *= n
        p %= c
    return p


def no_math_solution():
    c = 10**10
    res = 0
    for i in range(1, 1001):
        res += get_last_10_digits_of_power(i, i)
        res %= c
    return res


if __name__ == "__main__":
    print(no_math_solution())
