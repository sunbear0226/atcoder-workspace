#!/usr/bin/env python3
import sys


def solve(K: int, S: int):
    cnt = 0
    for x in range(K+1):
        for y in range(K+1):
            z = S - x - y
            if z >= 0 and z <= K:
                cnt += 1
    print(cnt)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    solve(K, S)

if __name__ == '__main__':
    main()