# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


def is_leap_year(y: int):
    if(y % 4 == 0):
        if(y % 100 == 0):
            if(y % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(m: int, y: int):
    if(is_leap_year(y)):
        return (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[m]
    else:
        return (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[m]


def no_math_solution():
    sundayCount = 0
    # 1 Jan 1900 was a Monday
    # so 1 Jan 1901 was a Tuesday (1900 was not a leap year)
    d = 2  # start at Sunday
    for y in range(1901, 2001):
        for m in range(1, 13):
            d = (d + days_in_month(m, y)) % 7
            sundayCount += (1 if d == 0 else 0)
    return sundayCount


if __name__ == "__main__":
    print(no_math_solution())
