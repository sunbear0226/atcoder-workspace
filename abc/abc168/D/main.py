import sys
from collections import deque
 
 
N, M = [int(i) for i in input().split()]
A = []
B = []
for i in range(M):
    l = [int(i) for i in input().split()]
    A.append(l[0])
    B.append(l[1])
 
# BFS
G = [[] for _ in range(N)]
for i in range(M):
    G[A[i] - 1].append(B[i] - 1)
    G[B[i] - 1].append(A[i] - 1)
G = [list(set(x)) for x in G]
 
q = deque([])
ans = [-1] * N
ans[0] = 0
q.appendleft(0)
while(len(q) > 0):
    v = q.pop()
    for nv in G[v]:
        if not ans[nv] == -1:
            continue
        ans[nv] = v
        q.appendleft(nv)

# 問題文に「全ての部屋を行き来可能」という旨の記述があるので、実はこの確認は不要。
for i in ans[1:]:
    if i == -1:
        print('No')
        sys.exit()
 
for i, v in enumerate(ans):
    if i == 0:
        print('Yes')
        continue
    print(v + 1)