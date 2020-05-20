#!/usr/bin/env python3
import sys


def solve(X: int):
    f = lambda x, y: x**5 - y**5
    for i in range(-200, 200):
        for j in range(-200, 200):
            if f(i, j) == X:
                print(str(i) + ' ' + str(j))
                return
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)

if __name__ == '__main__':
    main()