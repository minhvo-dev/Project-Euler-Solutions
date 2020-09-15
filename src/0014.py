# Which starting number, under one million, produces the longest chain in Collatz sequence?


def cal_next_number(i: int):
    # Calculate the next number of Collatz sequence started at i
    return i//2 if i % 2 == 0 else 3*i + 1


def cal_chain_length(i: int, d: dict):
    # Calculate the number of elements in Collatz sequence started at i
    if i in d:
        return d[i]
    d[i] = cal_chain_length(cal_next_number(i), d) + 1
    return d[i]


def no_math_solution(n: int):
    """Find the starting number of a Collatz sequence that produces the longest chain

    Args:
        n (int): max starting number (excluding)

    Returns:
        int: starting number
    """
    lookup = {1: 1}
    # Calculate the chain's length of all Collatz sequences started below n
    for i in range(2, n):
        cal_chain_length(i, lookup)
    # Find the longest chain
    longestChain = 1
    for i in range(2, n):
        if (lookup[i] > lookup[longestChain]):
            longestChain = i

    return longestChain


if __name__ == "__main__":
    # n = int(input())
    n = 1_000_000
    print(no_math_solution(n))
