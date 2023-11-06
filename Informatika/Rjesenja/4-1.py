# 4.1.
s = input()

niz = ""
output = ""

for i in s:
    if not i in "123456890":
        niz+=i
    else:
        output += niz*int(i)
        niz = ""
print(output)
