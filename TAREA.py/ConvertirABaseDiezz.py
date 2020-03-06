def convertirAbasediezprueba(n,b):
    return aux_b10(n,b,0,0)

def aux_b10(n,b,x,y):
    if n>0:
        return aux_b10(n//10,b,x+1,((b**x)*(n%10)+y))
    else:
        return y 

print(convertirAbasediezprueba(315,7))