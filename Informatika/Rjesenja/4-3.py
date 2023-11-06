# 4.3.

s = input()

min_dodaci = 0

for i in range(0, len(s)//2):
    if s[i] != s[-(i+1)]:
        min_dodaci+=1
print(min_dodaci)
