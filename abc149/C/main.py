#!/usr/bin/env python3
import sys


def solve(X: int):
    primes = get_prime_numbers_array(2 * (10**5))
    for i, v in enumerate(primes):
        if v and i >= X:
            print(i)
            return
    return


def get_prime_numbers_array(n: int):
    """エラトステネスのふるいを用いてnまでの素数判定を行うための配列を返す"""
    N = n + 1
    is_prime = [1] * N
    is_prime[0] = is_prime[1] = 0
    for i in range(2, N):
        if not is_prime[i]:
            continue
        for j in range(i * 2, N, i):
            is_prime[j] = 0
    return is_prime


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)

if __name__ == '__main__':
    main()
