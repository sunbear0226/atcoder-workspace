#!/usr/bin/env python3


def get_prime_numbers_array(n: int):
    """エラトステネスのふるいを用いてnまでの素数判定を行うための配列を返す"""
    N = n + 1
    is_prime = [1] * N
    is_prime[0] = is_prime[1] = 0
    for i in range(2, N):
        if not is_prime[i]:
            continue
        for j in range(i * 2, N, i):
            is_prime[j] = 0
    return is_prime


def cumsum(data: "List[int]"):
    """dataの累積和の配列を返す"""
    a = [0] * (len(data) + 1)
    for i in range(len(data)):
        a[i + 1] = a[i] + data[i]
    return a


# math.gcd()を使え！！
def gcd(x: int, y: int):
    """xとyの最大公約数を求める"""
    return gcd(y, x % y) if y else x


# 同上！！
def lcm(x, y):
    """xとyの最小公倍数を求める"""
    return (x * y) // gcd(x, y)


def factorize(n: int):
    """nの素因数分解を求める"""
    res = []
    for i in range(2, int(n ** 0.5//1 + 2)):
        if n % i:
            continue
        s = 0
        while n % i == 0:
            n /= i
            s += 1
        res.append([i, s])
    if n != 1:
        res.append([n, 1])
    return res


def comb(n, a, p=None):
    """nからa個選ぶ場合の選び方が何通りあるかを返す。pを指定した場合、mod pを返す。"""
    x = y = 1  # xが分子、yが分母
    for i in range(a):
        x *= n - i
        if not p:
            x %= p
        y *= i + 1
        if not p:
            y %= p
    return x * pow(y, p-2, p) % p if p else x / y


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


def Base_10_to_n(X, n):
    if (int(X / n)):
        return Base_10_to_n(int(X / n), n)+str(X % n)
    return str(X % n)