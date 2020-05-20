#!/usr/bin/env python3
import sys
import collections

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, K: int, Q: int, A: "List[int]"):
    d = collections.Counter(A)
    for i in range(N):
        print(YES if K - Q + d[i + 1] > 0 else NO)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, K, Q, A)

if __name__ == '__main__':
    main()
