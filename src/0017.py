# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


def convert_number_to_english(n: int):
    dMap = (
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten")
    teenMap = (
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen"
    )
    tenMap = (
        "",
        "ten",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety"
    )
    if(n <= 10):
        return dMap[n]
    if(n < 20):
        return teenMap[n-10]
    if(n < 100):
        return tenMap[n//10] + ((" " + dMap[n % 10]) if n % 10 != 0 else "")
    if(n < 1000):
        return dMap[n//100] + " hundred" + ((" and " + convert_number_to_english(n % 100)) if n % 100 != 0 else "")
    return "one thousand"


def no_math_solution():
    countLetters = 0
    for i in range(1, 1001):
        countLetters += sum(len(word)
                            for word in convert_number_to_english(i).split(" "))
    return countLetters


if __name__ == "__main__":
    print(no_math_solution())
