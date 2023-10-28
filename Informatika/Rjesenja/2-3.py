#2.3.
s = input()

samoglasnici = 0

for i in s:
    if i in "aeiouAEIOU": # operator in provjerava je li ono s njegove lijeve strane u nizu s njegove desne
        samoglasnici+=1   # zadatak se može riješiti i pješke, s 10 ifova

print(samoglasnici)
