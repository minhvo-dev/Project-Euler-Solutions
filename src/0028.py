# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def sum_diagonals(matrix: list):
    # matrix must have odd length
    n = len(matrix)
    s = 0
    for i in range(n // 2):
        s += matrix[i][i]  # top-left
        s += matrix[i][n - i - 1]  # top-right
        s += matrix[n - i - 1][i]  # bottom-left
        s += matrix[n - i - 1][n - i - 1]  # bottom-right
    s += matrix[n // 2][n // 2]  # center
    return s


_seed = 1


def get_next_number():
    global _seed
    res = _seed
    _seed += 1
    return res


def get_spiral(n: int):
    # n must be an odd number

    spiral = [[0 for _ in range(n)] for _ in range(n)]
    r = n // 2
    c = n // 2
    spiral[r][c] = get_next_number()

    for i in range(2, n, 2):
        # down
        c += 1
        for j in range(i):
            spiral[r][c] = get_next_number()
            r += 1
        r -= 1
        # left
        c -= 1
        for j in range(i):
            spiral[r][c] = get_next_number()
            c -= 1
        c += 1
        # up
        r -= 1
        for j in range(i):
            spiral[r][c] = get_next_number()
            r -= 1
        r += 1
        # right
        c += 1
        for j in range(i):
            spiral[r][c] = get_next_number()
            c += 1
        c -= 1

    return spiral


def no_math_solution(n: int):
    spiral = [[0] * n] * n


def math_solution(n: int):
    seed = 1
    diagonal_sum = seed
    for i in range(n//2):
        for j in range(4):
            seed += 2 * (i + 1)
            diagonal_sum += seed
    return diagonal_sum


if __name__ == "__main__":
    # n = int(input())
    n = 1001
    print(sum_diagonals(get_spiral(n)))
    print(math_solution(n))
