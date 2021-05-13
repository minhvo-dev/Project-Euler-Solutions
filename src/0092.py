# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
# What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
# How many starting numbers below ten million will arrive at 89?


def sum_square_digits(n: int):
    s = 0
    while n:
        d = n % 10
        s, n = s + d*d, n // 10
    return s


def recursive_cal(t: list, n: int):
    """Determine if the number will end at 1 or 89 based on the
    precalculated values from the table

    Args:
        t (list): table
        n (int): number
    """
    if(n == 1):
        t[1] = 0
    elif(n == 89):
        t[89] = 1  # what we are counting
    else:
        s = sum_square_digits(n)
        if(t[s] != -1):
            t[n] = t[s]
        else:
            recursive_cal(t, s)
            t[n] = t[s]


def pre_cal():
    """Generate a table which holds precalculated results for each
    number from 1 to 9*9*7 (since 9_999_999 gives the greatest sum)
    """

    table = [-1] * (9*9*7 + 1)  # max sum is of 9_999_999
    for i in range(1, len(table)):
        recursive_cal(table, i)
    return table


def no_math_solution():
    table = pre_cal()
    return sum(table[sum_square_digits(i)] for i in range(1, 10_000_000))


if __name__ == "__main__":
    print(no_math_solution())
