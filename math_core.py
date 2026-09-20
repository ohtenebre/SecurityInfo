import numpy as np


# y = a^x % p
def fast_pow(a=0, x=0, p=1, mode="manual"):
    if mode == "random":
        p = int(np.random.randint(100, 10000))
        a = int(np.random.randint(2, p))
        x = int(np.random.randint(1, p))
    elif mode == "prime":
        p = generate_prime()
        a = generate_prime()
        x = generate_prime()

    res = 1
    base = a % p
    temp_x = x
    while temp_x > 0:
        if temp_x & 1:
            res = (res * base) % p
        base = (base * base) % p
        temp_x >>= 1
    return res, a, x, p


# a^p-1 % p
def ferma(p, iterations=10):
    if p <= 1:
        return False
    if p == 2 or p == 3:
        return True
    if p % 2 == 0:
        return False

    for _ in range(iterations):
        a = np.random.randint(2, p - 1)

        if gcd(a, p)[0][0] != 1:
            return False

        if fast_pow(a, p - 1, p)[0] != 1:
            return False

    return True


def gcd(a=0, b=0, mode="manual"):
    if mode == "random":
        a = int(np.random.randint(100, 10000))
        b = int(np.random.randint(100, 10000))
    elif mode == "prime":
        a = generate_prime()
        b = generate_prime()

    u = [a, 1, 0]
    v = [b, 0, 1]

    if a > b:
        u, v = v, u

    while v[0] != 0:
        q = u[0] // v[0]
        T = [u[0] % v[0], u[1] - q * v[1], u[2] - q * v[2]]
        u = v
        v = T

    return u, a, b


def generate_prime(low=100, high=10000):
    while True:
        num = np.random.randint(low, high)
        if ferma(num):
            return num
