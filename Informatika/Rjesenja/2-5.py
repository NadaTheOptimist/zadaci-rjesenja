#2.5
s1 = input()
s2 = input()

output=""

for i in range(len(s1)):
    print(i)
    if i%2==0:
        output+=s1[i]
    else:
        output+=s2[i]

print(output)
