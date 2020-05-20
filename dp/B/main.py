#!/usr/bin/env python3
import sys


def solve(N: int, K: int, h: "List[int]"):
    # 漸化式
    # 足場Nに到達するためのルートはK種類あり、到達コストが最小になるルートを選ぶ。
    # dp[N] = dp[N-1] + abs(h[N-1] - h[N])
    # dp[N] = dp[N-2] + abs(h[N-2] - h[N])
    # ...
    # dp[N] = dp[N-K] + abs(h[N-K] - h[N])
    #
    # dp[i] = min(候補ルートのコストの配列) とすれば良い。
    # 候補ルートのコストの配列はループ処理で生成する。

    INF = 100100100
    dp = [INF] * N
    dp[0] = 0
    for i in range(1, N):
        for j in range(1, K):
            s = max(0, i-K)
            dp[i] = min(dp[i], dp[s] + abs(h[s] - h[i]))
    # for i in range(1, N):
    #     s = max(0, i - K)
    #     dp[i] = min([tc + abs(th - h[i]) for tc, th in zip(dp[s:i], h[s:i])])
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
    K = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, h)

if __name__ == '__main__':
    main()
