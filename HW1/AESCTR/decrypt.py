from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

f = open("key.txt", "rb")
key = f.read()

f = open("nonce.txt", "rb")
nonce = f.read()

f = open("cipher.txt", "rb")
ct = f.read()

cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

pt = cipher.decrypt(ct)

f = open("retrive.txt", "w")
f.write(pt.decode())
