# How many, not necessarily distinct, value of combination (n, r) for 1 <= n <= 100, are greater than one-million?


def calc_factorial(n: int):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


def no_math_solution(mn: int, lb: int):
    count = 0
    for r in range(1, mn+1):
        rf = calc_factorial(r)
        n = r
        nf = calc_factorial(n)
        nrf = calc_factorial(n - r)
        while(n <= mn):
            d = rf * nrf
            if(nf > lb * d):
                break
            n += 1
            nf *= n
            nrf *= (n - r)
        count += (mn - n + 1)
    return count


if __name__ == "__main__":
    print(no_math_solution(100, 1_000_000))
