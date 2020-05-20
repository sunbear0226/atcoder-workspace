#!/usr/bin/env python3
import sys

def solve(N, M, A, B, C):
    key = []  # type: "List[List[int, int]]"
    for i in range(M):
        s = 0 # i個目の鍵で開けられる宝箱を2進数で示す ex) 01 => 1個目の宝箱, 10 => 2個目の宝箱, 11 => 1個目と2個目の宝箱
        for j in range(B[i]): # 開けられる宝箱が複数あるときは、論理和を取ることでそれを表現できる ex) 01 | 10 = 11
            s |= 1 << (C[i][j] - 1) # ex) 2番目の宝箱を開けられる場合 s = s | 1 << (2 - 1) = s | 10  s = 01なら、01 | 10 = 11 
        key.append([s, A[i]]) # どの宝箱を開けられるか と 鍵の値段 をマッピング
    
    INF = 1001001001 # A <= 10^5, M <= 10^3 なので10^8より大きければOK
    dp = [INF] * (1 << N)  # 使用していないインデックスが分かるようにするためINFで埋める。1 << Nは、例えばN=3なら1000となり、1000までの2進数を扱える
    dp[0] = 0 # 初期値は、何も鍵を開けられない状態なので0
    for s in range(1 << N):
        for i in range(M):
            t = s | key[i][0] # tは遷移先。key[i][0]はどの宝箱を開けられるかの2進数。s(遷移元)との論理和を取ると新しい状態に遷移できる
            cost = dp[s] + key[i][1] # dp[s]は遷移元に至るまでのコスト。key[i][1]は遷移元から遷移先へのコスト。合計することで0地点からのコストになる
            dp[t] = min(dp[t], cost) # dp[t]は0地点から遷移先までのコスト。遷移先に至るルートは複数あるので、その中で最小のコストを選択していくための処理。
    ans = dp[-1] # dp[-1]は、N=3の場合であれば1000の一個前なので111となる。すべて1で埋まっている状態は、すべての宝箱を開けられる状態を示す。
    print(-1 if ans == INF else ans) # すべての宝箱を開けられる状態を示す箇所に値が入っていない(=INF)ということは、すべての宝箱を開けられないということ。
    pass


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A, B, C = [], [], []
    for _  in range(M):
        A.append(int(next(tokens)))
        B.append(int(next(tokens)))
        C.append([int(next(tokens)) for _ in range(B[-1])])
    solve(N, M, A, B, C)

if __name__ == '__main__':
    main()
