# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433 × 2^7830457 + 1.
# Find the last ten digits of this prime number.


def fast_exp(n: int, e: int, m: int):
  if(e == 0):
    return 1
  if(e == 1):
    return n
  if(e % 2 == 0):
    return fast_exp(n * n % m, e // 2, m) % m
  return (n * fast_exp(n * n % m, e // 2, m)) % m

def math_solution():
  m = 10**10
  return (28_433 * fast_exp(2, 7_830_457, m) + 1) % m

if __name__ == "__main__":
  print(math_solution())