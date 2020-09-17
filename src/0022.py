# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?


def read_names_from_file(path: str):
    f = open(path, "r")
    names = f.read()
    f.close()
    return [name.strip()[1:-1] for name in names.strip().split(",")]



def no_math_solution(names: list):
    names = sorted(names)
    return sum((sum(ord(c)-ord('A')+1 for c in names[i-1]) * i for i in range(1, len(names)+1)))
    

if __name__ == "__main__":
    filePath = "./data/p022_names.txt"
    names = read_names_from_file(filePath)
    print(no_math_solution(names))