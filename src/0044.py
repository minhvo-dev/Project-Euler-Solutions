# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?


def get_first_n_pentagonals(n: int):
    return [i*(3*i-1)//2 for i in range(1, n+1)]


def no_math_solution():
    n = 10_000
    pentagonals = get_first_n_pentagonals(n)
    s = set(pentagonals)
    dif = pentagonals[-1] - pentagonals[0]
    for i in range(0, n):
        for j in range(i+1, n):
            sumPiPj = pentagonals[i] + pentagonals[j]
            difPiPj = pentagonals[j] - pentagonals[i]
            if(sumPiPj in s and difPiPj in s):
                dif = difPiPj if difPiPj < dif else dif
                print(pentagonals[i], pentagonals[j])
    return dif


if __name__ == "__main__":
    print(no_math_solution())
