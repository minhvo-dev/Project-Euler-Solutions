# What is the sum of the digits of the number 2^1000?


def cal_russian_peasant_exponent(x: int, exp: int):
    """Calculate exponent x^exp

    Args:
        x (int): base
        exp (int): exponent

    Returns:
        int: x^exp
    """
    while(exp % 2 == 0):
        x *= x
        exp //= 2
    p = x
    exp //= 2
    while(exp > 0):
        x *= x
        if(exp % 2 != 0):
            p *= x
        exp //= 2
    return p


def no_math_solution(x: int, exp: int):
    res = cal_russian_peasant_exponent(x, exp)
    return sum((int(d) for d in str(res)))


if __name__ == "__main__":
    x, exp = map(int, input().strip().split())
    print(no_math_solution(x, exp))
