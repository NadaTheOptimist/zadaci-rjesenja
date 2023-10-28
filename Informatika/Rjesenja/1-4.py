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
