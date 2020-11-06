# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

def sum_digits(n: int):
    return sum([int(d) for d in str(n)])

def no_math_solution():
    maxSum = 0
    for a in range(2, 100):
        p = 1
        for b in range(1, 100):
            p *= a
            s = sum_digits(p)
            maxSum = s if s > maxSum else maxSum
    return maxSum

if __name__ == "__main__":
    print(no_math_solution())