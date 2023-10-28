#3.2.
import random

n = int(input())

manji_od_n = 0

for i in range(10):
    x = random.randint(1, 2*n)
    if x<=n:
        manji_od_n += 1
print(manji_od_n)
