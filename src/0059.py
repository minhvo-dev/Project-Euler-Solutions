# XOR decryption
import string


def is_common_english_charactor(i: int):
    return i >= 32 and i <= 126


def is_common_english_word(word: str):
    if(word[0].isnumeric()):
        # number does not count as a word
        return True
    # common english word has length less than 15
    if(len(word) > 15):
        return False
    return True


def load_data(path: str):
    f = open(path, 'r')
    s = f.read()
    f.close()
    return s.split(',')


def no_math_solution():
    path = "./data/p059_cipher.txt"
    data = load_data(path)
    chars = string.ascii_lowercase
    common_words = ["a", "A", "an", "An", "the", "The"]
    for k0 in chars:
        for k1 in chars:
            for k2 in chars:
                keys = [k0, k1, k2]
                iKey = 0
                text = ""
                word = ""
                foundText = True
                foundCommonWords = False
                for d in data:
                    decrypted = (int(d) ^ ord(keys[iKey]))
                    if(is_common_english_charactor(decrypted) == False):
                        foundText = False
                        break
                    if(decrypted == 32):
                        # found a space
                        if(word == ""):
                            foundText = False
                            break
                        if(is_common_english_word(word)):
                            if(word in common_words):
                                foundCommonWords = True
                            text += word + " "
                            word = ""
                        else:
                            foundText = False
                            break
                    else:
                        word += chr(decrypted)
                    iKey += 1
                    if(iKey == 3):
                        iKey = 0
                # last check
                if(word == "" or is_common_english_word(word) == False):
                    foundText = False
                else:
                    text += word
                if(foundText == True and foundCommonWords == True):
                    print("".join(keys), text, sum(ord(c) for c in text))


if __name__ == "__main__":
    no_math_solution()
