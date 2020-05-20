#!/usr/bin/env python3
import sys


def solve(N: int, h: "List[int]"):
    # [漸化式]
    # i+1かi+2の足場にしか行けないという事は、ゴールNから逆算して考えると、
    # N-1の足場にたどり着く最小コスト+|hN-1 - hN| と、
    # N-2の足場にたどり着く最小コスト+|hN-2 - hN| のうち、コストが小さい方が答えになる。
    # dp[i] = iの足場にたどり着くための最小コスト、と定義すれば良い。

    INF = 1001001001
    dp = [INF] * N
    for i in range(N):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = dp[i-1] + abs(h[i-1] - h[i])
        else:
            dp[i] = min(dp[i-1] + abs(h[i-1] - h[i]), dp[i-2] + abs(h[i-2] - h[i]))
    print(dp[N-1])
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, h)

if __name__ == '__main__':
    main()
