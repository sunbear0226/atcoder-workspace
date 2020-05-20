#!/usr/bin/env python3
import sys


def solve(K: int, N: int, A: "List[int]"):
    m = 0
    for i in range(N):
        d = A[i] if i == 0 else A[i] - A[i - 1]
        m = max(m, d)
        if i == N - 1:
            m = max(m, K + A[0] - A[i])
    print(K - m)

    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(K, N, A)

if __name__ == '__main__':
    main()
