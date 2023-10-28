"""# I - Osnovne naredbe
# 1.1.
n = int(input())
print(0-n) # moguće je napisati print(-n)

#1.2.
x = input()
n = int(input())

if int(x)/n > n:
    print("DA")
else:
    print("NE")

#1.3.
# Je li broj prost? == Ima li broj točno dva djelitelja?
n = int(input())

djelitelji = 0 # pomoćne varijable za više-manje sve slučajeve gdje treba brojati nešto

for i in range(1, n+1): # sjeti se parametara for-a, redom, 
    if n%i==0:          # početna vrijednost, 
        djelitelji+=1   # zadnja vrijednost (neuključivo)
                        # i korak (za koliko se mijenja i)
if djelitelji == 2:
    print("DA")
else:
    print("NE")

#1.4.
# idejni ishod zadatka je korištenje while petlje
n = int(input())

nadeni = 0  # pomoćna varijabla za brojanje dosad ispisanih prostih brojeva
x = 1       # varijabla za iteraciju - trenutni prirodni prosti broj koji provjeravamo

while nadeni < n:
    djelitelji = 0
    
    for i in range(1, x+1):
        if x%i==0:
            djelitelji+=1

    if djelitelji==2:
        print(x)    # x je prost -> ispiši i
        nadeni+=1   # za jedan prosti broj smo bliži kraju while-a
    x+=1    # u sljedećem ponavljanju while-a provjeravaj broj za 1 veći od prošlog

#1.5.
# idejni ishod zadatka je korištenje "alternativnih" parametara for-a
n = int(input())

for i in range(n, 0, -1): # varijabla for-a, rekoh,
    if n%i==0:            # nikad neće poprimiti vrijednost  
        print(i)          # drugog parametra (u ovom slučaju 0)

#1.6.
# zadatak je postavljen više kao mozgalica, jer je prvi zadatak moguće riješiti u jednoj
# liniji
print(-int(input()))
# ovo funkcionira jer se s vrijednosti int(input())-a, makar malo kontraintuitivno, može
# računati bez da se njegov return sprema u varijablu

# II - Manipulacija nizovima znakova
#2.1.
s = input()

for i in range(len(s)):
    if i%2==0:  # i je indeks trenutnog znaka
        print(s[i])

#2.2.
s = input()

suma = 0    # pomoćna varijabla za zbrajanje

for i in s:
    suma += ord(i)  # i je znak, funkcija ord vraća ASCII vrijednost znaka

print(suma)

Ovaj zadatak možda predstavlja novi koncept; for i in (niz znakova).
Lijeniji mogu zapamtiti da ovo čini da varijabla i poprima vrijednost svakog znaka
u nizu znakova.

Za one znatiželjnije, doduše, korisno je znati da je to jer for općenito *isključivo*
poprima vrijednosti iz niza - bilo znakova ili brojeva.
U primjerima tipa
for i in range(n, m, s):
For isto prolazi kroz sve elemente niza, samo što je range funkcija koja generira niz brojeva.
Za dokaz čitatelju:
Ispiši niz brojeva koristeći funkciju range od 1 do upisanog prirodnog broja n.


#2.3.
s = input()

samoglasnici = 0

for i in s:
    if i in "aeiouAEIOU": # operator in provjerava je li ono s njegove lijeve strane u nizu s njegove desne
        samoglasnici+=1   # zadatak se može riješiti i pješke, s 10 ifova

print(samoglasnici)

#2.4.
s = input()

output = "" # pomoćna varijabla za izlazni niz znakova

for i in range(len(s)-1, -1, -1):   # drugi operator mora biti -1 kako bi i došao do 0
    output += s[i]                  # budući da indeksi kreću od 0, len(s) je uvijek
                                    # za jedan prevelik

print(output)

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

#2.6.
s = input()

slog1 = ""
slog2 = ""
trenutni_slog = 1
for i in s:
    if i in "aeiouAEIOU" and trenutni_slog==1:  # ako je trenutni znak samoglasnik, 
        slog1+=i
        trenutni_slog=2                         # znači da smo naišli na kraj jednog sloga -> ako je trenutni_slog = 1, 
    elif i in "aeiouAEIOU":                     # znači da je kraj prvog sloga, ako je samoglasnik a nije prvi slog, onda
        slog2+=i                                # treba na kraj drugog sloga dodati samoglasnik
    elif trenutni_slog==1:                      # ako i nije samoglasnik, a trenutni_slog je 1, treba dodati i na kraj prvog sloga
        slog1+=i                                # inače, treba dodati i na kraj drugog sloga
    else:
        slog2+=i

print(slog2+slog1)  # na kraju ispisati slog2+slog1

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
"""
# III - Funkcije, vlastite, predefinirane, vanjske
#3.1.b)
from funkcije import palindrom
s = input()
print(palindrom(s))
#3.2.
import random

n = int(input())

manji_od_n = 0

for i in range(10):
    x = random.randint(1, 2*n)
    if x<=n:
        manji_od_n += 1
print(manji_od_n)

#3.3.
import math

n = int(input())
x = int(input())

korijen = n     # pomoćna varijabla koju ćemo iznova i iznova korijenovati

                # budući da je x 2^m, znači da je broj korijena koji trebamo obaviti m,
                # kojeg ćemo dobiti tako da x dijelimo 2^m sa 2 dokle god moguće

while x>1:
    korijen = math.sqrt(korijen)
    x = x//2

print(round(korijen,2))     # round(x, n) -> zaokruži x na n-tu decimalu

#3.4.
n = int(input())

print(oct(n)[1:]) # oct -> vraća niz znakova, oktalnu reprezentaciju n, u obliku 0b00000
