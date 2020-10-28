# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


def count_digit(n: int):
    count = [0] * 10
    while(n > 0):
        count[n % 10] += 1
        n //= 10
    return count


def no_math_solution():
    exp = 0
    found = 0
    while(found == 0):
        lower = 10**exp
        upper = 10**(exp + 1) // 6
        for i in range(lower, upper + 1):
            counts = [count_digit(i * m) for m in range(1, 7)]
            if all([counts[0] == c for c in counts[1:]]):
                found = i
        exp += 1
    return found


if __name__ == "__main__":
    print(no_math_solution())
