#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, t: "List[int]", x: "List[int]", y: "List[int]"):
    pre_t, pre_x, pre_y = [0] * 3
    for i in range(N):
        dt = t[i] - pre_t
        move = x[i] - pre_x + y[i] - pre_y
        if dt < move or dt % 2 != move % 2: 
            print(NO)
            return
        pre_t = t[i]
        pre_x = x[i]
        pre_y = y[i]

    print(YES)
    return


# Generated by 1.1.5 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    t = [int()] * (N)  # type: "List[int]"
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        t[i] = int(next(tokens))
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, t, x, y)

if __name__ == '__main__':
    main()
