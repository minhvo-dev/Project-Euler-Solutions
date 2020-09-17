# Evaluate the sum of all the amicable numbers under 10000.


def no_math_solution(n: int):
    d = [sum(d for d in range(1, i//2 + 1) if i % d == 0) for i in range(0, n)]
    return sum(i for i in range(2, n) if i != d[i] and d[i] < n and i == d[d[i]])


if __name__ == "__main__":
    # n = int(input())
    n = 10000
    print(no_math_solution(n))
