
def str_xor(secret, key):
    # Extend key to match secret length
    new_key = key
    i = 0

    while len(new_key) < len(secret):
        new_key += key[i]
        i = (i + 1) % len(key)

    return "".join(
        chr(ord(s) ^ ord(k))
        for s, k in zip(secret, new_key)
    )


flag_enc = bytes.fromhex(
    "04 0d 0a 0d 01 18 1c 15 5a 07 00 46 "
    "0b 1a 5a 1d 1d 2a 06 1c 5a 5c 55 40 "
    "3a 08 5d 5a 53 40 52 0f 0f 14"
).decode("latin-1")

flag = str_xor(flag_enc, "enkidu")

print("That is correct! Here's your flag: " + flag)
