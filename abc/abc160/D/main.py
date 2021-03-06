#!/usr/bin/env python3
import sys
import collections
from collections import deque


def solve(N: int, X: int, Y: int):
    seen = [[False] * N] * N
    X -= 1
    Y -= 1
    cnt = []
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if seen[i][j]:
                continue
            seen[j][i] = True
            cnt.append(min(abs(j - i), abs(X - i) + 1 + abs(j - Y)))
    counter = collections.Counter(cnt)
    keys = counter.keys()
    for i in range(N):
        if i not in keys:
            print(0)
            continue
        print(counter[i])
    return


def solve2(N: int, X: int, Y: int):
    # BFS
    X -= 1
    Y -= 1
    G = [[] for _ in range(N)]
    for i in range(N):
        if not i == N - 1:
            G[i].append(i+1)
            G[i+1].append(i)
        if i == X:
            G[i].append(Y)
            G[Y].append(i)
        if i == Y:
            G[i].append(X)
            G[X].append(i)
    G = [list(set(x)) for x in G]
    q = deque([])
    ans = [0] * N
    # 各頂点をスタート地点として、他の点への移動にかかる最短距離を求めて集計する
    for i in range(N):
        dist = [-1] * N
        dist[i] = 0
        q.appendleft(i)
        while(len(q) > 0):
            v = q.pop()
            for nv in G[v]:
                if not dist[nv] == -1:
                    continue
                dist[nv] = dist[v] + 1
                q.appendleft(nv)
        for d in dist:
            ans[d] += 1
    for i in range(N):
        ans[i] //= 2
    for i in range(1, N):
        print(ans[i])
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve2(N, X, Y)

if __name__ == '__main__':
    main()
