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
