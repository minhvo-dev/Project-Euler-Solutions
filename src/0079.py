# A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.


def load_data(path: str):
    f = open(path, 'r')
    s = f.read()
    f.close()
    return s.split('\n')


def no_math_solution():
    path = "./data/p079_keylog.txt"
    nums = set(load_data(path)[:-1])  # last item in load_data is empty string

    suffix = [set() for _ in range(0, 10)]

    for n in nums:
        # first digit
        d = int(n[0])
        suffix[d].add(int(n[1]))
        suffix[d].add(int(n[2]))
        # second digit
        d = int(n[1])
        suffix[d].add(int(n[2]))

    # sort based on the number of suffix a digit has
    x = [i for i in zip(range(0, 10), suffix) if len(i[1]) > 0]
    x.sort(key=lambda x: len(x[1]), reverse=True)
    ans = [i[0] for i in x]
    # the last suffix shoud be added to the result since it does not have a suffix
    ans.append(list(x[-1][1])[0])
    print(ans)


if __name__ == "__main__":
    no_math_solution()
