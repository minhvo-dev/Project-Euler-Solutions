# How many are triangle words?

import math


def convert_word_to_number(word: str):
    word = word.upper()
    a = ord('A')
    total = 0
    for w in word:
        total += ord(w) - a + 1
    return total


def is_triangle_number(n: int):
    r = math.floor(math.sqrt(n*2))
    return True if r * (r + 1) == 2 * n else False


def read_words_from_file(path: str):
    f = open(path, "r")
    words = f.read()
    f.close()
    return [w[1:-1] for w in words.split(",")]


def no_math_solution():
    path = "./data/p042_words.txt"
    words = read_words_from_file(path)
    total = 0
    for w in words:
        n = convert_word_to_number(w)
        if(is_triangle_number(n)):
            total += 1
    return total


if __name__ == "__main__":
    print(no_math_solution())
