# How many Lychrel numbers are there below ten-thousand?

MAX_ITER = 50

def is_palindrome(n: int):
    s = str(n)
    return s == s[::-1]

def get_reverse_number(n: int):
    s = str(n)
    return int(s[::-1])

def no_math_solution(maxN: int):
    global MAX_ITER
    countLychrelNumber = 0
    num = 1
    while(num < maxN):
        countIter = 0
        s = num
        while(countIter < MAX_ITER):
            s += get_reverse_number(s)
            if(is_palindrome(s)):
                break
            countIter += 1
        if(countIter == MAX_ITER):
            countLychrelNumber += 1
        num += 1
    return countLychrelNumber
        


if __name__ == "__main__":
    # n = int(input())
    n = 10_000
    print(no_math_solution(n))