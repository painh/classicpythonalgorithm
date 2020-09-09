from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_byes: bytes = original.encode()
    dummy: int = random_key(len(original_byes))
    original_byes: int = int.from_bytes(original_byes, "big")
    encrypted: int = original_byes ^ dummy

    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2  # xor
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()

key1, key2 = encrypt("one time pad!")
result: str = decrypt(key1, key2)
print(result)
