from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

f = open("../plaintext.txt", "r")
message = f.read().encode()

random_key = get_random_bytes(16)
f = open("key.txt", "wb")
f.write(random_key)

key = random_key
cipher = AES.new(key, AES.MODE_CBC)
cipher_byte = cipher.encrypt(pad(message, AES.block_size))
initial_vector = cipher.iv;

f = open("cipher.txt", "wb")
f.write(cipher_byte)

f = open("init_vector.txt", "wb")
f.write(initial_vector)

