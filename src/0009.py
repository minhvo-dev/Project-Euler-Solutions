# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def no_math_solution(n: int):
    # loop and hope
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            c = n - a - b
            if(c**2 == a**2 + b**2):
                return a*b*c
    # not found
    return -1


def math_solution(n: int):
    for a in range(1, n):
        b = n * (n-2*a) / (n-a) / 2
        if(b == int(b)):
            c = n - a - b
            return int(a*b*c)
    return -1


if __name__ == "__main__":
    # n = int(input())
    n = 1000
    print(math_solution(n))
