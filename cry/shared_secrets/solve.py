
from pathlib import Path

# Parse the challenge transcript
data = {}
for line in Path("message.txt").read_text().splitlines():
    key, value = line.split(" = ", 1)
    data[key] = value

p = int(data["p"])
A = int(data["A"])
b = int(data["b"])
enc = bytes.fromhex(data["enc"])

# Recover Diffie-Hellman shared secret
shared = pow(A, b, p)

# The encryption key is one byte
key = shared % 256

# Decrypt the ciphertext
flag = bytes(c ^ key for c in enc)

print("[+] Shared secret recovered")
print(f"[+] Key byte: {key}")
print(f"[+] Flag: {flag.decode()}")
