import numpy as np
from math_core import fast_pow, gcd
from crypto_utils import generate_prime

import numpy as np
from math_core import fast_pow, gcd
from crypto_utils import generate_prime


def generate_rsa_keys(p=None, q=None, d=None, mode="random"):
    if mode == "manual":
        if p is None:
            p = int(input("Введите простое число p: "))
        if q is None:
            q = int(input("Введите простое число q: "))

        N = p * q
        phi = (p - 1) * (q - 1)

        if d is None:
            d = int(input(f"Введите d (взаимно простое с {phi}): "))
    else:
        p = generate_prime(low=100, high=500)
        while True:
            q = generate_prime(low=100, high=500)
            if q != p:
                break

        N = p * q
        phi = (p - 1) * (q - 1)

        # Choose popular exp d in popular num's list
        for candidate_d in [3, 5, 17, 257, 65537]:
            if candidate_d < phi and gcd(candidate_d, phi)[0][0] == 1:
                d = candidate_d
                break
        else:
            # If not success, so perebor
            d = 3
            while gcd(d, phi)[0][0] != 1:
                d += 2

    # Secret key (Secret exp)
    res_gcd, _, _ = gcd(phi, d)
    c = res_gcd[2]

    if c < 0:
        c += phi

    return p, q, N, d, c


def rsa_encrypt_file(input_path, output_path, d, N):
    with open(input_path, "rb") as f:
        data = f.read()

    encrypted_bytes = []
    for byte in data:
        enc_block = fast_pow(byte, d, N)[0]
        encrypted_bytes.append(enc_block)

    with open(output_path, "wb") as f:
        f.write(np.array(encrypted_bytes, dtype=np.uint32).tobytes())


def rsa_decrypt_file(input_path, output_path, c, N):
    with open(input_path, "rb") as f:
        encrypted_data = np.frombuffer(f.read(), dtype=np.uint32)

    decrypted_bytes = bytearray()
    for enc_block in encrypted_data:
        dec_byte = fast_pow(int(enc_block), c, N)[0]
        decrypted_bytes.append(dec_byte)

    with open(output_path, "wb") as f:
        f.write(decrypted_bytes)
