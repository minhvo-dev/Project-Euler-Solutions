# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# How many different ways can £2 be made using any number of coins?


def no_math_solution(v: int, coins: list):
    ways = [0] * (v+1)
    ways[0] = 1  # 1 way to make 0
    for c in coins:
        for i in range(v+1):
            if(i >= c):
                ways[i] += ways[i - c]
    return ways[v]


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    v = 200
    print(no_math_solution(v, coins))
