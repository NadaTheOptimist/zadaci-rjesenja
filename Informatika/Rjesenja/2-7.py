#2.7.
# idejni ishod, između ostalih, je da int() može imati dva parametra
s = input()

binarni = ""    # pomoćna varijabla za spremanje "binariziranog" niza znakova

for i in s:
    if i in "aeiouAEIOU":   # i je samoglasnik, treba dodati "1" na binarni
        binarni+="1"
    else:
        binarni+="0"
print(binarni)
print(int(binarni, 2)) # int(x, n) pretvara x iz baze n
