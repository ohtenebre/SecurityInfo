import math
import numpy as np
from math_core import fast_pow, generate_prime, ferma


def velikan(a=0, y=0, p=1, mode="manual"):
    if mode == "random":
        p = int(generate_prime())
        a = int(np.random.randint(2, p))
        x_secret = int(np.random.randint(1, p))
        y = fast_pow(a, x_secret, p, mode="manual")[0]

        print(f"Сгенерировано: a={a}, y={y}, p={p} Загадано x={x_secret}")

    m = math.isqrt(p) + 1
    baby_steps = {}
    giant_steps = {}

    current_baby = y % p
    current_giant = 1
    a_to_m = fast_pow(a, m, p)[0]

    # Baby && Giant steps
    for k in range(0, m):
        baby_steps[current_baby] = k
        current_giant = (current_giant * a_to_m) % p
        giant_steps[current_giant] = k + 1

        current_baby = (current_baby * a) % p

    # Find Match
    for val in giant_steps:
        if val in baby_steps:
            i = giant_steps[val]
            j = baby_steps[val]
            return i * m - j, a, y, p

    return -1, a, y, p


def diffie_hellman(p=10, g=5, Xa=0, Xb=0, mode="manual"):
    if mode == "random":
        while True:
            q = generate_prime()
            p = 2 * q + 1
            if ferma(p):
                break

        g = 2
        while fast_pow(g, q, p)[0] == 1:
            g += 1

        Xa = int(np.random.randint(2, p))
        Xb = int(np.random.randint(2, p))

        print(f"Сгенерировано: p={p}, g={g}, Xa={Xa}, Xb={Xb}")

    Ya = fast_pow(g, Xa, p)[0]
    Yb = fast_pow(g, Xb, p)[0]

    Za = fast_pow(Yb, Xa, p)[0]
    Zb = fast_pow(Ya, Xb, p)[0]

    return Ya, Yb, Za, Zb, p, g, Xa, Xb
