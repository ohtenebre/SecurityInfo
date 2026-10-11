import numpy as np
import algorithms


def generate_vernam_key(length, mode="random"):
    if mode == "dh":
        _, _, Za, _, _, _, _, _ = algorithms.diffie_hellman(mode="random")
        rng = np.random.default_rng(seed=Za)
        key = rng.integers(0, 256, size=length, dtype=np.uint8).tobytes()
    else:
        key = np.random.randint(0, 256, size=length, dtype=np.uint8).tobytes()

    return key


def vernam_encrypt_file(input_path, output_path, key=None, mode="random"):
    with open(input_path, "rb") as f:
        data = bytearray(f.read())

    file_len = len(data)

    if key is None:
        key = generate_vernam_key(file_len, mode=mode)

    encrypted_bytes = bytearray(file_len)
    for i in range(file_len):
        encrypted_bytes[i] = data[i] ^ key[i]

    with open(output_path, "wb") as f:
        f.write(encrypted_bytes)

    return key


def vernam_decrypt_file(input_path, output_path, key):
    with open(input_path, "rb") as f:
        encrypted_data = bytearray(f.read())

    decrypted_bytes = bytearray(len(encrypted_data))
    for i in range(len(encrypted_data)):
        decrypted_bytes[i] = encrypted_data[i] ^ key[i]

    with open(output_path, "wb") as f:
        f.write(decrypted_bytes)
