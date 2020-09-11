# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# ref: https://projecteuler.net/problem=1

def no_math_solution(n: int, muls: tuple):
    """Calculate the sum of all the multiples of muls that less than n

    Args:
        n (int): max number (excluding)
        muls (tuple): list of multiples of

    Returns:
        int: sum
    """
    # loop through all numbers and check
    return sum([i for i in range(1, n) if any(i % m == 0 for m in muls)])

def sum_muls(n: int, m: int):
    """Sum of all multiples of m that less than n

    Args:
        n (int): max number (excluding)
        m (int): multiple of

    Returns:
        int: sum
    """
    maxMul = (n // m) * m
    return int((m + maxMul) * ((maxMul - m) / m + 1) / 2)

def math_solution(n: int):
    # only work with 3 and 5
    return sum_muls(n, 3) + sum_muls(n, 5) - sum_muls(n, 15)

if __name__ == "__main__":
    # n, *muls = map(int, input().strip().split())
    n = 1000
    muls = (3, 5)
    print(no_math_solution(n, muls))
    print(math_solution(n))

    
