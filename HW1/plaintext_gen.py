import random
from math import floor

table = "123456789abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ,.?&%!@#^&()"

target = 200000000
n = len(table)

s = ""
for i in range(0, target):
	x = floor(n * random.random())
	s += table[x]

print(s)



