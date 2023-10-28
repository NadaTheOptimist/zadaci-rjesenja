def palindrom(x):
    for i in range(len(x)//2):
        if x[i]!=x[-(i+1)]:
            return False
    return True
