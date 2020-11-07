# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

def get_next_expansion(numerator: int, denominator: int):
    return [numerator + denominator * 2, numerator + denominator]

def get_number_digits(n: int):
    return len(str(n))

def no_math_solution(n: int):
    count = 0
    i = 1
    [num, den] = [3, 2]
    while(i <= n):
        nDigits = get_number_digits(num)
        dDigits = get_number_digits(den)
        if(dDigits < nDigits):
            count += 1
        [num, den] = get_next_expansion(num, den)
        i += 1
    return count

if __name__ == "__main__":
    # n = int(input())
    n = 1_000
    print(no_math_solution(n))