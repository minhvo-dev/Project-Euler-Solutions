# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
# F1 = 1, F2 = 1

def no_math_solution(digits: int):
    if(digits == 1):
        return 1
    [f1, f2] = [1, 1]
    count = 2
    while(len(str(f2)) < digits):
        [f1, f2] = [f2, f1 + f2]
        count += 1
    return count


if __name__ == "__main__":
    # n = int(input())
    n = 1_000
    print(no_math_solution(n))
    