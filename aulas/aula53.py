lista=['thiago','gabi','pato']
item1, item2, item3 = lista #substituivel por item1, item2, item3 = ['thiago', 'gabi', 'pato']
print(item1, item2, item3)
item1, *_ =['thiago', 'gabi', 'pato']
print(item1)
_, item2, *_=['thiago', 'gabi', 'pato'] # *_ empacota o 'resto' dos itens da lista

#tuplas são listas IMUTAVEIS
#listas sem colchetes são tuplas

tupla='thiago', 'gabi', 'pato' #se eu tentar alterar tipo tuplas[1]='qualquer' retorna erro
print(tupla)
tuplaconvertida=tuple(lista) #converte list em tuple
listaconvertida=list(tupla) #converte tuple em list

lista_enumerada=enumerate(lista)
print(list(enumerate(lista)))

i=0
for i in lista_enumerada:
    indice,nome=i
    print(indice,nome)
