from Crypto.Cipher import ChaCha20
from Crypto.Util.Padding import unpad

f = open("key.txt", "rb")
key = f.read()

f = open("nonce.txt", "rb")
nonce = f.read()

f = open("cipher.txt", "rb")
ct = f.read()

cipher = ChaCha20.new(key=key, nonce=nonce)

pt = cipher.decrypt(ct)

f = open("retrive.txt", "w")
f.write(pt.decode())
