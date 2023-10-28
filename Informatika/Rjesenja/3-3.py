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

print(round(korijen,2)) 
# round(x, n) -> zaokruži x na n-tu decimalu
