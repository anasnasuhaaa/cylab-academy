import subprocess

CHALLENGE = "challenge.py"  # Sesuaikan nama file
WORDLIST = "passwords.txt"

with open(WORDLIST, "r") as f:
    passwords = [line.strip() for line in f if line.strip()]

print(f"[*] Total passwords: {len(passwords)}")

for i, password in enumerate(passwords, 1):
    try:
        result = subprocess.run(
            ["python3", CHALLENGE],
            input=password + "\n",
            capture_output=True,
            text=True,
            timeout=5
        )

        output = result.stdout + result.stderr
        output_lower = output.lower()

        print(f"\r[{i}/{len(passwords)}] Trying: {password}", end="", flush=True)

        # Abaikan password yang salah
        if "password is incorrect" in output_lower:
            continue

        # Deteksi flag yang valid
        if "picoctf{" in output_lower or "academy{" in output_lower:
            print(f"\n\n[+] Password found: {password}")
            print(f"[+] Output:\n{output}")
            break

        # Tampilkan respons lain untuk diperiksa
        print(f"\n[?] Unexpected response for {password}: {output.strip()}")

    except subprocess.TimeoutExpired:
        print(f"\n[-] Timeout: {password}")

else:
    print("\n[-] Password not found.")
