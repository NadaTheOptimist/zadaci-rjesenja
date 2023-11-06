# 4.2.

def oktalno(x):
    output = ""
    while x>=1:
        output += str(x % 8)
        x = x // 8
    return output[::-1]

def binarno(x):
    output = ""
    while x>=1:
        output += str(x % 2)
        x = x // 2
    return output[::-1] # podsjetnik - [::-1] obrće string

n = int(input())
print(round(int(binarno(n)) / int(oktalno(n)), 2))

# podsjetnik - round(x, a) zaokružuje decimalni broj x na a-tu decimalu
