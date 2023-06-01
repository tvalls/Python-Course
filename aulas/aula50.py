lista1=[1,2,3]
lista2=[]
lista2.extend(lista1)
lista1[0]=2
print(lista2)
#lista1=lista2 aponta as duas variáveis para o mesmo ID, então alterar qualquer uma das listas altera as duas
#lista1=lista2.copy() copia os valores da lista 2 pra lista 1 criando uma nova lista