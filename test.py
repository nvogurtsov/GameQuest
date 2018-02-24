from random import randint
import os

i, j = 0, 0

while 1:
    i = i + 1
    if randint(1, 10) == 7:
        print("YES, trys", i)
        break

while 1:
    j = j + 1
    if 1 < randint(1, 100) < 10:
        print("YES, trys", j)
        break
