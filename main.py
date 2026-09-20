import math_core
import algorithms
import shamir_cypher
import crypto_utils

## Лаба 1
# res, a, x, p = math_core.fast_pow(mode="random")
# print(f"a: {a}, x: {x}, p: {p}, res: {res}")

# print(math_core.ferma(17))

# res_gcd, a, b = math_core.gcd(mode="random")
# print(f"a: {a}, b: {b}, nod: {res_gcd[0]}, x: {res_gcd[1]}, y: {res_gcd[2]}")

## Лаба 2

# x_found, a, y, p = algorithms.velikan(mode="random")
# print(f"a: {a}, y: {y}, p: {p}, x: {x_found}")

## Лаба 3

# Ya, Yb, Za, Zb, p, g, Xa, Xb = algorithms.diffie_hellman(mode="random")
# print(f"p: {p}, g: {g}")
# print(f"Секреты: Xa={Xa}, Xb={Xb}")
# print(f"Открытые ключи: Ya={Ya}, Yb={Yb}")
# print(f"Общий секрет у Алисы (Za): {Za}")
# print(f"Общий секрет у Боба (Zb): {Zb}")

## Лаба 4

p = crypto_utils.generate_prime(low=300, high=10000)

Ca, Da = shamir_cypher.generate_shamir_keys(p)
Cb, Db = shamir_cypher.generate_shamir_keys(p)

# shamir_cypher.shamir_encrypt_file("files/text.txt", "files/encr_text.txt", Ca, Cb, p)
# shamir_cypher.shamir_decrypt_file("files/encr_text.txt", "files/restored_text.txt", Da, Db, p)

shamir_cypher.shamir_encrypt_file("files/kitty.png", "files/encr_kitty.png", Ca, Cb, p)
shamir_cypher.shamir_decrypt_file("files/encr_kitty.png", "files/restored_kitty.png", Da, Db, p)


print(f"Ключи 1: C={Ca}, D={Da}. Ключи 2: C={Cb}, D={Db}")
