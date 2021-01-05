# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.


def get_first_100_sequence():
    seq = [2, 1, 2]
    k = 2
    while(len(seq) <= 100):
        seq += [1, 1, k*2]
        k += 1
    return seq

def get_numerator_of_100th():
    seq = get_first_100_sequence()
    [num, den] = [seq[99], 1]
    for i in range(98, -1, -1):
        [num, den] = [den, num]
        num += den * seq[i]
    return num

def sum_digits_of_n(n: int):
    return sum(i for i in map(int, str(n)))

if __name__ == "__main__":
    print(sum_digits_of_n(get_numerator_of_100th()))
