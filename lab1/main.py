from cycler import U
import numpy as np


# y = a^x % p
def fast_pow(a, x, p):
    res = 1

    a = a % p

    while x > 0:
        if x & 1:
            res = (res * a) % p

        a = (a * a) % p

        x >>= 1

    return res


# a^p-1 % p
def ferma(a, p):
    if p <= 1:
        return False
    return fast_pow(a, p - 1, p) == 1


def gcd(a, b):
    u = [a, 1, 0]
    v = [b, 0, 1]

    if a > b:
        u, v = v, u

    while v[0] != 0:
        q = u[0] // v[0]

        T = [u[0] % v[0], u[1] - q * v[1], u[2] - q * v[2]]

        u = v
        v = T

    return u


def simple_rand():
    while 1:
        num = np.random.randint(0, 10000)

        if ferma(2, num):
            return num


print("Введите тип: \n1 - с клавы\n2 - рандом\n3 - рандом простые")
type = int(input())

if type == 1:
    a = int(input())
    b = int(input())
elif type == 2:
    a = np.random.randint(0, 10000)
    b = np.random.randint(0, 10000)
else:
    a = simple_rand()
    b = simple_rand()

print(f"a: {a}\nb: {b}")

c = gcd(a, b)
print(f"нод: {c[0]}, x: {c[1]}, y: {c[2]}")
