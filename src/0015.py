# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

def cal_route(r: int, c: int, n: int, grid: list):
    if(r > n or c > n):
        return 0
    if(grid[r][c] != 0):
        return grid[r][c]
    grid[r][c] = cal_route(r+1, c, n, grid) + cal_route(r, c+1, n, grid)
    return grid[r][c]

def no_math_solution(n: int):
    grid = [[0 for _ in range(n+1)] for _ in range(n+1)]
    grid[-1][-1] = 1
    return cal_route(0, 0, n, grid)

if __name__ == "__main__":
    # n = int(input())
    n = 20
    print(no_math_solution(n))