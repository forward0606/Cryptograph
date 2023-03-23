import random
from math import floor

table = "123456789abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ,.?&%!@#^&()     \n\n\n\n\n"

target = 200000000
n = len(table)

s = ""
for i in range(0, target):
	x = floor(n * random.random())
	s += table[x]

f = open("plaintext.txt", "w")
f.write(s)



