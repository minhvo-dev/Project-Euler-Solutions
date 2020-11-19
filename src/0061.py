# Find the sum of the only ordered set of six cyclic 4-digit numbers
# for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal,
# and octagonal, is represented by a different number in the set.


def get_triangles(n: int):
    return n * (n + 1) // 2


def get_square(n: int):
    return n * n


def get_pentagonal(n: int):
    return n * (3 * n - 1) // 2


def get_hexagonal(n: int):
    return n * (2 * n - 1)


def get_heptagonal(n: int):
    return n * (5 * n - 3) // 2


def get_octagonal(n: int):
    return n * (3 * n - 2)


def get_polygonal_with_4_digits(f: object):
    n = 2
    p = 1
    while(p < 1000):
        p = f(n)
        n += 1
    l = []
    while(p < 10_000):
        l.append(p)
        p = f(n)
        n += 1
    return l


def get_first_two_digits(n: int):
    return n // 100


def get_last_two_digits(n: int):
    return n % 100


def recursive(table: dict, nums: list, left: list):
    if(len(left) == 0):
        return nums
    for f in left:
        ps = [i for i in table[f] if get_last_two_digits(
            nums[-1]) == get_first_two_digits(i) and i not in nums]
        if(len(ps) > 0):
            newLeft = [ff for ff in left if ff != f]
            for p in ps:
                nums.append(p)
                res = recursive(table, nums, newLeft)
                if(len(res) == 6):
                    if(get_last_two_digits(nums[-1]) == get_first_two_digits(nums[0])):
                        return nums
                nums.pop()
    return []


def no_math_solution():
    table = {
        get_triangles: get_polygonal_with_4_digits(get_triangles),
        get_square: get_polygonal_with_4_digits(get_square),
        get_pentagonal: get_polygonal_with_4_digits(get_pentagonal),
        get_hexagonal: get_polygonal_with_4_digits(get_hexagonal),
        get_heptagonal: get_polygonal_with_4_digits(get_heptagonal),
        get_octagonal: get_polygonal_with_4_digits(get_octagonal)
    }

    polygonals = [get_triangles, get_square, get_pentagonal,
                  get_hexagonal, get_heptagonal, get_octagonal]

    for p in polygonals:
        for n in table[p]:
            left = [f for f in polygonals if f != p]
            res = recursive(table, [n], left)
            if(len(res) > 0):
                return res
    return []


if __name__ == "__main__":
    res = no_math_solution()
    print(res, sum(res))
