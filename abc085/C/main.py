#!/usr/bin/env python3
import sys


def solve(N: int, Y: int):
    for i in range(N + 1):
        for j in range(N - i + 1):
            k = N - i - j
            if 10000 * i + 5000 * j + 1000 * k == Y:
                print(i, j, k)
                return
    print('-1 -1 -1')
    return


# Generated by 1.1.5 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(N, Y)

if __name__ == '__main__':
    main()
