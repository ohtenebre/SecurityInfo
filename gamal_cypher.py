import numpy as np
from math_core import fast_pow
from crypto_utils import generate_prime


def find_divisors(N):
    div = []
    if N % 2 == 0:
        div.append(2)
        while N % 2 == 0:
            N //= 2

    i = 3
    while i * i <= N:
        if N % i == 0:
            div.append(i)
            while N % i == 0:
                N //= i
        i += 2

    if N > 2:
        div.append(N)

    return div


def find_primitive_root(p):
    if p == 2:
        return 1

    divisors = find_divisors(p - 1)

    for g in range(2, p):
        is_primitive = True

        for q in divisors:
            power = (p - 1) // q

            if fast_pow(g, power, p) == 1:
                is_primitive = False
                break
        if is_primitive:
            return g

    return 0


def generate_gamel_keys(p):
    g = find_primitive_root(p)

    c_B = np.random.randint(2, p - 2)  # секрктный ключ
    d_B = fast_pow(g, c_B, p)[0]  # открытый ключи

    return g, c_B, d_B


def gamal_encrypt_file(input_path, output_path, mode="random"):
    if mode == "manual":
        p = int(input("p: "))
        g = int(input(f"g (от 2 до {p-1}): "))
        c_B = int(input(f"(от 2 до {p-2}): "))

        d_B = fast_pow(g, c_B, p)[0]
    else:
        p = generate_prime(low=300, high=10000)

        g = find_primitive_root(p)

        c_B = int(np.random.randint(2, p - 2))
        d_B = fast_pow(g, c_B, p)[0]

    with open(input_path, "rb") as inf, open(output_path, "wb") as outf:
        while True:
            byte = inf.read(1)

            if not byte:
                break

            m = byte[0]
            k = int(np.random.randint(1, p - 2, dtype="int32"))  # сессионный ключ
            r = fast_pow(g, k, p)[0]  # первая часть шифртекста

            mask = fast_pow(d_B, k, p)[0]
            e = (m * mask) % p  # вторая часть шифртекста

            r_bytes = r.to_bytes(2, byteorder="big")
            e_bytes = e.to_bytes(2, byteorder="big")

            outf.write(r_bytes)
            outf.write(e_bytes)

    return p, g, c_B, d_B


def gamal_decrypt_file(input_path, output_path, p, c_B):
    with open(input_path, "rb") as inf, open(output_path, "wb") as outf:
        while True:
            four_bytes = inf.read(4)

            if not four_bytes or len(four_bytes) < 4:
                break

            r_bytes = four_bytes[0:2]
            e_bytes = four_bytes[2:4]

            r = int.from_bytes(r_bytes, byteorder="big")
            e = int.from_bytes(e_bytes, byteorder="big")

            decrypt_power = p - 1 - c_B

            remedy = fast_pow(r, decrypt_power, p)[0]
            m = (e * remedy) % p

            outf.write(bytes([m]))
