from cryptography.fernet import Fernet


f = open("plaintext", "r")
s = f.read()

###################################
#          AES-CBC mode           #
###################################
# https://cryptography.io/en/latest/fernet/

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(s.encode())

f = open("cipher_AESCBC.txt", "w")
f.write(token.decode())

f = open("key_AESCBC.txt", "w")
f.write(key.decode())
#retrive = f.decrypt(token)


###################################
#		  AES-CTR mode            #
###################################

