from Crypto.Random import get_random_bytes
from Crypto.Cipher import ChaCha20
from Crypto.Util.Padding import pad

f = open("../plaintext.txt", "r")
message = f.read().encode()

random_key = get_random_bytes(32)
f = open("key.txt", "wb")
f.write(random_key)

key = random_key
cipher = ChaCha20.new(key=key)
cipher_byte = cipher.encrypt(message)
nonce = cipher.nonce;

f = open("cipher.txt", "wb")
f.write(cipher_byte)

f = open("nonce.txt", "wb")
f.write(nonce)

