# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

def get_nums(digits: list, maxDigit: int):
    """Generate list of all numbers that are combination of digits

    Args:
        digits (list): list of unique digits in ascending order
        maxDigit (int): max number of digits of generated number

    Returns:
        list: list of all generated digits
    """
    nDigits = len(digits)
    nums = [d for d in digits]
    last = nums
    for i in range(1, nDigits):
        tmp = []
        for d in digits:
            for n in last:
                if d not in n:
                    tmp.append(d + n)
        if(len(tmp[0]) > maxDigit):
            break
        nums += tmp
        last = tmp

    return [int(n) for n in nums]

def is_pandigital(multiplicand: int, multiplier: int):
    nums = [multiplicand, multiplier, multiplicand * multiplier]
    count = [0] * 10
    for n in nums:
        for d in str(n):
            count[int(d)] += 1
    if(count[0] > 0):
        return False
    for i in range(1, 10):
        if(count[i] != 1):
            return False
    return True
    
def no_math_solution():
    nums = get_nums([str(i) for i in range(1, 10)], 5)
    products = set()
    for a in nums:
        for b in nums:
            if(len(str(a)) + len(str(b)) > 5):
                break
            if(is_pandigital(a, b)):
                print(a, b, a * b)
                products.add(a * b)
    
    s = 0
    for i in products:
        s += i
    return s


if __name__ == "__main__":
    print(no_math_solution())
    