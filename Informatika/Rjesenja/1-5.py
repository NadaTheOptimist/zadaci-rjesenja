#1.5.
# idejni ishod zadatka je korištenje "alternativnih" parametara for-a
n = int(input())

for i in range(n, 0, -1): # varijabla for-a, rekoh,
    if n%i==0:            # nikad neće poprimiti vrijednost  
        print(i)          # drugog parametra (u ovom slučaju 0)
