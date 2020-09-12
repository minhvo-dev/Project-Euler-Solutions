# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def no_math_solution(n: int):
    """Calculate the smallest number that is evenly divisible by all the numbers
        from 1 to n

    Args:
        n (int): max divisor (including)

    Returns:
        int: smallest number
    """
    if(n == 1):
        return 1
    ans = 2
    while(True):
        # loop and hope
        d = n
        while(d > 1):
            if(ans % d != 0):
                break
            d -= 1
        if(d == 1):
            break
        ans += 2
    return ans


def gcd(a: int, b: int):
    """Calculate greatest common divisor of two positive numbers
        based on euclidean algorithms

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: greatest common divisor
    """
    if(a < b):
        a, b = b, a
    while(b > 0):
        a, b = b, a % b
    return a


def math_solution(n: int):
    """Calculate the smallest number that is evenly divisible by all the numbers
        from 1 to n

    Args:
        n (int): max divisor (including)

    Returns:
        int: smallest number
    """
    lcm = 1
    for i in range(1, n+1, 1):
        # there is no integer overflow in python (I think so)
        lcm = lcm * i // gcd(lcm, i)
    return lcm


if __name__ == "__main__":
    # n = int(input())
    n = 20
    print(math_solution(n))
