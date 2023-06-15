#Escopo pode ser Global ou Local
y=2 #esta variável foi definida global, então pode ser callable dentro do def ou fora
def escopo():
    x=1 #esta variável não está definida fora da função então só é callable dentro da função
    global y #permite alterar valor do Y global por dentro da função
    y+=1
    print(x,y)

escopo()