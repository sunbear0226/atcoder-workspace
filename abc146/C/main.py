#!/usr/bin/env python3
import sys


def solve(A: int, B: int, X: int):
    # 二分探索
    N = ans = last = 10**9
    first = 0
    for i in range(10**5):
        s = A * ans + B * len(str(ans))
        if s > X:
            last = int(ans)
        else:
            first = int(ans)
        ans = (last - first) // 2 + first
        if last - first <= 1:
            break
    print(ans)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(A, B, X)

if __name__ == '__main__':
    main()
