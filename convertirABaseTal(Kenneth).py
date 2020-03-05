def convertirABaseTal (n,b):
    if n<b:
        return n
    else:
        c=n//b
        d=n%b
        return d+10*convertirABaseTal(c,b)
print (convertirABaseTal(2048,16))