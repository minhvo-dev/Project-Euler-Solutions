# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.


def no_math_solution(n: int):
    l = []
    for i in range(1, n):
        if(str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[:1:-1]):
            l.append(i)
    return sum(l)


if __name__ == "__main__":
    # n = int(input())
    n = 1_000_000
    print(no_math_solution(n))
