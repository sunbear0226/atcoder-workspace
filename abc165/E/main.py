#!/usr/bin/env python3
import sys


def solve(N: int, M: int):
    if N % 2:
        for i in range(M):
            print(str(i + 1) + ' ' + str(N - 1 - i))
    else:
        for i in range(M):
            print(str(N / 2 + i) + ' ' + str(N / 2 + 1 + i))
        
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)

if __name__ == '__main__':
    main()
