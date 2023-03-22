from cryptography.fernet import Fernet


f = open("key_AESCBC.txt", "r")
key = f.read().encode()

f = open("cipher_AESCBC.txt", "r")
s = f.read().encode()


f = Fernet(key)
cipher = f.encrypt(s)


retrive = f.decrypt(cipher)

f = open("AES_CBC_retrive.txt", "w")
f.write(retrive.decode())
