
def gcd(a: int, b: int):
    if(a < b):
        a, b = b, a
    while(b > 0):
        a, b = b, a % b
    return a


def no_math_solution():
    numerators = []
    denominators = []
    for i in range(10, 100):
        for j in range(i+1, 100):
            num = str(i)[::-1]
            den = str(j)[::-1]
            if(num[0] == den[0] and num[0] != '0'):
                if((i//10) * j == (j//10) * i):
                    numerators.append(i)
                    denominators.append(j)
                    continue
            if(num[0] == den[1]):
                if((i//10) * j == (j % 10) * i):
                    numerators.append(i)
                    denominators.append(j)
                    continue
            if(num[1] == den[0]):
                if((i % 10) * j == (j//10) * i):
                    numerators.append(i)
                    denominators.append(j)
                    continue
            if(num[1] == den[1]):
                if((i % 10) * j == (j % 10) * i):
                    numerators.append(i)
                    denominators.append(j)

    n = 1
    for i in numerators:
        n *= i
    d = 1
    for i in denominators:
        d *= i
    return d // gcd(n, d)


if __name__ == "__main__":
    print(no_math_solution())
