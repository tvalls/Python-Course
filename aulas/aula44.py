#for+ range == range(start,stop,step)
#tabuada
base=input('Tabuada de qual número? ')
base=int(base)
intervalo=range(0,100,base)
for numero in intervalo:
    print(numero)