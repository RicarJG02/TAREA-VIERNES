def convertirABaseDiez(n,b):
    if n<b:
        return n 
    else:
        (n//b,b) + convertirABaseDiez[n%b]


