# Find the sum of the digits in the number 100!


def no_math_solution(n: int):
    m = 1
    for i in range(1, n+1):
        m *= i
    return sum(int(d) for d in str(m))


if __name__ == "__main__":
    n = int(input())
    print(no_math_solution(n))
