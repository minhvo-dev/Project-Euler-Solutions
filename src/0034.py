# Find the sum of all numbers which are equal to the sum of the factorial of their digits.


def get_factorial_list():
    f = [1] * 10
    for i in range(1, 10):
        f[i] = f[i-1] * i
    return f


def no_math_solution():
    f = get_factorial_list()
    res = 0
    for i in range(3, 7 * f[9]):
        s = 0
        for d in str(i):
            s += f[int(d)]
        if(s == i):
            res += s
            # print(i)
    return res


if __name__ == "__main__":
    print(no_math_solution())
