#!/usr/bin/env python3
import sys
import collections


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    cur = 1
    c = {}
    route = []
    second_f = None
    while (True):
        if cur in c:
            second_f = cur
            break
        route.append(cur)
        c[cur] = 1
        cur = A[cur - 1]
    idx = route.index(second_f)
    if K <= idx:
        print(route[K])
        return
    roop = route[idx:]
    print(route[(K - idx) % (len(route) - idx) + idx])
    return


if __name__ == '__main__':
    main()
