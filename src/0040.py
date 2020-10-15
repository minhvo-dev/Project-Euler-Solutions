# Champernowne's constant


def get_nth_digit(n: int):
    if(n < 10):
        return n
    down = 10  # including
    up = 100  # excluding
    nDigits = 2
    totalDigits = 9 + (up - down) * nDigits
    while(totalDigits < n):
        down, up = up, up * 10
        nDigits += 1
        totalDigits += (up - down) * nDigits
    # roll back
    totalDigits -= (up - down) * nDigits
    remainingDigits = n - totalDigits - 1
    nthNumber = remainingDigits // nDigits
    nthDigit = remainingDigits % nDigits
    number = down + nthNumber
    return int(str(number)[nthDigit])


def no_math_solution(ds: list):
    res = 1
    for d in ds:
        res *= get_nth_digit(d)
    return res


if __name__ == "__main__":
    ds = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]
    print(no_math_solution(ds))
