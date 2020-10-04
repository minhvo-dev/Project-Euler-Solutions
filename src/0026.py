# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


def recurring_cycle_length(n: int):
    remainders = []
    r = 1
    while(r not in remainders):
        remainders.append(r)
        r = (r * 10) % n
    if(r == 0):
        return 0
    else:
        return len(remainders) - remainders.index(r)


def no_math_solution(d: int):
    lengths = [recurring_cycle_length(i) for i in range(2, d + 1)]
    return lengths.index(max(lengths)) + 2  # since we start at 2


if __name__ == "__main__":
    # n = int(input())
    n = 1_000 - 1
    print(no_math_solution(n))
