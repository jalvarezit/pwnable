from pwn import *


context(arch='arm', os='linux', log_level='error')

'''
Pwntools version must be 4.11 or higher to use ssh with qemu
see this issue for more info https://github.com/Gallopsled/pwntools/issues/1937

Additionally raw mode must be enabled.
'''

sh = ssh('leg', 'pwnable.kr', password='guest', port=2222, raw=True)


'''
To get the solution number just run the binary with qemu and check what value is
compared with the input
'''
solution = b'108400'

'''
Somehow sh.system with qemu does not properly run the binary but I used to get
access to a ssh_channel and interact with the connection
'''
io = sh.system('does not matter', tty=True, raw=True)


'''
There is remanining data from qemu initialization that must be read before
'''
while io.can_recv(timeout=10):
    io.recv()

io.sendline(b'/leg')
io.recv(timeout=10)
io.sendline(solution)

# io.recvline().decode()
# io.recvline().decode()
# io.recvline().decode()

io.recvuntil(b'Congratz!')
# receive empty line
io.recvline()

# print flag
print(io.recvline().decode())
