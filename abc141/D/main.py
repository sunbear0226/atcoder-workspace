#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]"):
    l = sorted(A, reverse=True)
    for _ in range(M):
        m = max(l)
        l[l.index(m)] = m // 2
    print(sum(l))
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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()
