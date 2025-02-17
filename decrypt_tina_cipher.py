import random

KEY = "337"
LETTER_DISTANCE = 4


def read_cipher_file(filename: str) -> list[str]:
    ct_list: list[str] = []
    with open(filename, "r") as ct_file:
        ct_list = ct_file.read().split("-")
    return ct_list


def decode_to_int(ct_token_list: list[str]) -> list[int]:
    return [ord(ct[0].upper()) + 10 - ord('A') if ct[0] > '9' else int(ct) for ct in ct_token_list]


def decrypt(filename: str, key: str) -> str:
    ct_codes = decode_to_int(read_cipher_file(filename))
    decrypted = [ct_codes[i] - int(key[i % len(key)]) for i in range(len(ct_codes))]
    return "".join([chr(decrypted[i] * 16 + decrypted[i + 1]) for i in range(0, len(decrypted), 2)])


def encrypt(message_filename: str, ct_filename: str, key: str, separator: str):
    msg: str = ""
    with open(message_filename, "r") as msg_file:
        msg = msg_file.read()
    nibble_list = [nibble for tup in [(ord(ch) // 16, ord(ch) % 16) for ch in msg] for nibble in tup]
    encrypted = [nibble_list[i] + int(key[i % len(key)]) for i in range(len(nibble_list))]
    index = random.randint(1, 2 * LETTER_DISTANCE)
    letter_indices = []
    while index < len(encrypted):
        letter_indices.append(index)
        index += random.randint(1, LETTER_DISTANCE)
    enc_with_letters = [chr(encrypted[i] + ord('A') - 10) if i in letter_indices and encrypted[i] > 9 else encrypted[i] for i in range(len(encrypted))]
    cipher_text = "".join([f'{nib}-' for nib in enc_with_letters])[:-1]
    with open(ct_filename, "w") as ct_file:
        ct_file.write(cipher_text)


def main():
    print(decrypt("tina_cipher_text.txt", KEY))
    # encrypt("msg_to_tina4.txt", "ct_to_tina4.txt", KEY, "-")
    # print(decrypt("ct_to_tina4.txt", KEY))


if __name__ == "__main__":
    main()
