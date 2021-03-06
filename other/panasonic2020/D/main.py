#!/usr/bin/env python3
import sys


def solve(N: int):
    ans = []
    if N == 1:
        print('a')
        return
    if N == 2:
        print('aa')
        print('ab')
        return
    for i in range(2**(N-1)):
        s = str(format(i, 'b')).zfill(N-1).replace('0', 'a').replace('1', 'b')
        ans.append('a' + s)
    last = ''
    for i in range(N):
        last += chr(ord('a') + i)
    for i in sorted(ans):
        print(i)
    print(last)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
