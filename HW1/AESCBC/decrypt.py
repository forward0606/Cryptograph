from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

f = open("key.txt", "rb")
key = f.read()

f = open("init_vector.txt", "rb")
init_vector = f.read()

f = open("cipher.txt", "rb")
ct = f.read()

cipher = AES.new(key, AES.MODE_CBC, init_vector)
pt = unpad(cipher.decrypt(ct), AES.block_size)

f = open("retrive.txt", "w")
f.write(pt.decode())
