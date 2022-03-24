from pwn import *

context(arch='amd64', os='linux', log_level='error')

sh = ssh('col', 'pwnable.kr', password='guest', port=2222)
# Make collision
p = sh.process(['col','!0gx!0gx!0gx!0gxhI@@'])
# Read flag file
flag = p.recv()
print(flag)

