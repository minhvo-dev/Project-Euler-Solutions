# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


def no_math_solution():
    maxPandigital = 0
    for i in range(9, 10000):
        s = str(i)
        m = 2
        while(len(s) < 9):
            s += str(i * m)
            m += 1
        ss = set(s)
        if(len(s) == 9 and len(ss) == 9 and '0' not in s):
            if(int(s) > maxPandigital):
                # print(i)
                maxPandigital = int(s)
    return maxPandigital


if __name__ == "__main__":
    print(no_math_solution())
