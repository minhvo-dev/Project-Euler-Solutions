# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def sum_fifth_power_digits(n: int):
    return sum(int(d)**5 for d in str(n))


def no_math_solution():
    l = (i for i in range(2, ((9**5) * 6)) if i == sum_fifth_power_digits(i))
    return sum(l)


if __name__ == "__main__":
    print(no_math_solution())
