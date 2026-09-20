import numpy as np
from math_core import gcd, fast_pow


def generate_shamir_keys(p):
    p = np.abs(p)
    phi = p - 1

    while True:
        c = np.random.randint(2, phi - 1)

        res_gcd, _, _ = gcd(c, phi)
        if res_gcd[0] == 1:
            d = res_gcd[1]
            if d < 0:
                d += phi
            return c, d


def shamir_encrypt_file(input_path, output_path, Ca, Cb, p):
    with open(input_path, "rb") as f:
        data = f.read()

    with open(output_path, "wb") as f_out:
        for M in data:
            x1 = fast_pow(M, Ca, p)[0]
            x2 = fast_pow(x1, Cb, p)[0]

            f_out.write(x2.to_bytes(2, byteorder="big"))


def shamir_decrypt_file(input_path, output_path, Da, Db, p):
    with open(input_path, "rb") as f:
        data = f.read()

    decrypted_bytes = []

    for i in range(0, len(data), 2):
        two_bytes = data[i : i + 2]
        M_encrypted = int.from_bytes(two_bytes, byteorder="big")

        x3 = fast_pow(M_encrypted, Da, p)[0]
        x4 = fast_pow(x3, Db, p)[0]

        decrypted_bytes.append(x4)

    with open(output_path, "wb") as f:
        f.write(bytes(decrypted_bytes))
