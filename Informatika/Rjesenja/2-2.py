#2.2.
s = input()

suma = 0    # pomoćna varijabla za zbrajanje

for i in s:
    suma += ord(i)  # i je znak, funkcija ord vraća ASCII vrijednost znaka

print(suma)
"""
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
"""
