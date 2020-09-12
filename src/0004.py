# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(n: int):
    """Check if a number is a palindrome

    Args:
        n (int): a number

    Returns:
        boolean: True if the number is palindrome, false otherwise
    """
    return str(n) == str(n)[::-1]


def no_math_solution(digits: int):
    """Find the largest palindrom of the product of two numbers.

    Args:
        digits (int): the number of digits of each numbers

    Returns:
        int: palindrome number
    """
    maxPalindrome = 0
    for i in range(10**(digits - 1), 10**digits, 1):
        for j in range(i, 10**digits, 1):
            mul = i * j
            if(mul > maxPalindrome):
                maxPalindrome = mul if is_palindrome(mul) else maxPalindrome
    return maxPalindrome

def math_solution():
    pass

if __name__ == "__main__":
    # n = int(input())
    n = 3
    print(no_math_solution(n))
