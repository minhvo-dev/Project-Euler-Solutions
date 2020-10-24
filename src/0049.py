# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?


def create_sieve(n: int):
    sieve = [-1] * (n + 1)  # -1 is unset
    for i in range(2, n+1):
        if(sieve[i] == -1):
            sieve[i] = 1  # 1 is prime
            for j in range(2*i, n+1, i):
                sieve[j] = 0  # 0 is not prime
    return sieve


def get_all_permutations(s: str):
    perms = [s[0]]
    for c in s[1:]:
        tmp = []
        for p in perms:
            for i in range(len(p)):
                tmp.append(p[:i] + c + p[i:])
            tmp.append(p + c)
        perms = tmp
    return set(perms)


def get_greater_permutations(n: int):
    return [int(p) for p in get_all_permutations(str(n)) if int(p) > n]


def no_math_solution():
    sieve = create_sieve(9999)
    for i in range(1000, 10000):
        if(sieve[i] == 1):
            perms = get_greater_permutations(i)
            l = [i]
            for j in range(len(perms)):
                if(sieve[perms[j]] == 1):
                    diff = perms[j] - i
                    n = perms[j] + diff
                    if(n in perms and sieve[n] == 1):
                        l.append(perms[j])
                        l.append(n)
            if(len(l) > 2):
                print(l)


if __name__ == "__main__":
    print(no_math_solution())
