# For which value of p ≤ 1000, is the number of solutions maximised?

import math


def no_math_solution(p: int):
    count = [0] * (p + 1)
    for a in range(1, p//2 + 1):
        for b in range(a, p//2 + 1):
            c = math.sqrt(a*a + b*b)
            if (c == math.floor(c)):
                perimeter = a + b + math.floor(c)
                if(perimeter <= p):
                    count[perimeter] += 1
    maxP = 0
    for i in range(1, p + 1):
        if(count[i] > count[maxP]):
            maxP = i

    return maxP


if __name__ == "__main__":
    p = int(input())
    print(no_math_solution(p))
