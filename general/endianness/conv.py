import struct

def find_little_endian(word):
    return "".join(f"{ord(c):02X}" for c in word[::-1])

def find_big_endian(word):
    return "".join(f"{ord(c):02X}" for c in word)

word = input("Enter the generated word: ")
little = find_little_endian(word)
big = find_big_endian(word)

print(f"Little-endian: {little}")
print(f"Big-endian: {big}")