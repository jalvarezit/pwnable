from pwn import *

context(arch='amd64', os='linux', log_level='error')

sh = ssh('random', 'pwnable.kr', password='guest', port=2222)

p = sh.process('random')

p.sendline(b'3039230856')

p.recvline()
flag = p.recv()
print(flag)

