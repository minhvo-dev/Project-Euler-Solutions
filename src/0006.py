# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def no_math_solution(n: int):
    return sum(range(1, n+1))**2 - sum((i**2 for i in range(1, n+1)))


def math_solution():
    pass


if __name__ == "__main__":
    # n = int(input())
    n = 100
    print(no_math_solution(n))
