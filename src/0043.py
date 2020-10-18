# Find the sum of all 0 to 9 pandigital numbers with this property.


def is_first_three_digits_divisible_by_n(s: str, n: int):
    i = int(s[0:3])
    return i % n == 0


def generate_numbers(nums: list, divisor: int):
    """[summary]

    Args:
        nums (list): list of string of numbers
        divisor (int): divisor
    """
    res = []
    for n in nums:
        for d in range(0, 10):
            d = str(d)
            if d not in n:
                tmp = d + n
                if(is_first_three_digits_divisible_by_n(tmp, divisor)):
                    res.append(tmp)

    return res


def no_math_solution():
    n = 17
    seed = []
    while(n < 1000):
        s = str(n)
        if(len(s) == 2):
            s = '0' + s
        if(s[0] != s[1] and s[0] != s[2] and s[1] != s[2]):
            seed.append(s)
        n += 17

    divisors = [13, 11, 7, 5, 3, 2]
    for d in divisors:
        seed = generate_numbers(seed, d)

    res = []
    for s in seed:
        d = 45 - sum([int(c) for c in s])
        if(d != 0):
            res.append(str(d) + s)

    return res


if __name__ == "__main__":
    res = no_math_solution()
    print(res)
    print(sum([int(s) for s in res]))
