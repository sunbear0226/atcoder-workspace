#!/usr/bin/env python3
import sys


def solve(X: int, Y: int, A: int, B: int, C: int, p: "List[int]", q: "List[int]", r: "List[int]"):
    pp = sorted(p, reverse=True)[:X]
    qq = sorted(q, reverse=True)[:Y]
    apples = sorted(pp + qq)
    rr = sorted(r, reverse=True)
    for i, v in enumerate(apples):
        if len(rr) > i and rr[i] > v:
            apples[i] = rr[i]
        else:
            break
    print(sum(apples))
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    q = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    r = [int(next(tokens)) for _ in range(C)]  # type: "List[int]"
    solve(X, Y, A, B, C, p, q, r)

if __name__ == '__main__':
    main()
