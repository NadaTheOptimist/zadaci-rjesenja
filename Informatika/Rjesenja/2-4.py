#2.4.
s = input()

output = "" # pomoćna varijabla za izlazni niz znakova

for i in range(len(s)-1, -1, -1):   # drugi operator mora biti -1 kako bi i došao do 0
    output += s[i]                  # budući da indeksi kreću od 0, len(s) je uvijek
                                    # za jedan prevelik

print(output)
