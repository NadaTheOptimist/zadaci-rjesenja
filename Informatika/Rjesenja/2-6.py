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

