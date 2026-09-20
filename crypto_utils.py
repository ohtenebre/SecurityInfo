import numpy as np
from math_core import fast_pow, gcd


# a^p-1 % p
def ferma(p):
    if p <= 1:
        return False
    if p == 2 or p == 3:
        return True
    if p % 2 == 0:
        return False

    for _ in range(10):
        a = np.random.randint(2, p - 1)

        if gcd(a, p)[0][0] != 1:
            return False

        if fast_pow(a, p - 1, p)[0] != 1:
            return False

    return True


def generate_prime(low=100, high=10000):
    while True:
        num = np.random.randint(low, high)
        if ferma(num):
            return num


# p = 2q + 1 q и p simle nums
def generate_dh_params(low=100, high=5000):
    while True:
        q = generate_prime(low, high)
        p = 2 * q + 1
        if ferma(p):
            for g in range(2, p - 1):
                if fast_pow(g, q, p) != 1:
                    return p, g
