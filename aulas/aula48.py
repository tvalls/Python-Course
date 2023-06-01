#listas em python - tipo list - mutável
#metodos uteis: append, insert, pop, del, clear, extend, +
# lista=[123,True,'Thiago',1.2,[]]
# print(len(lista))
# print(lista)
# print(lista[2], type(lista[2]))
# lista[2]='Valls'
# print(lista[2])
# print(lista)
# #append insere ao final da lista
# #pop remove da lista com possibilidade de puxar pra variavel var=lista.pop(indice)
# #del lisa[indice ou -indice] remove o item selecionado da lista
# #clear limpa a lista
# #insert insere com dois argumentos, indice e valor a inserir
# indice=2
# valor='teste'
# lista.insert(indice,valor) 

lista_a=[1,2,3]
lista_b=[4,5,6]
lista_c=lista_a+lista_b #sinal de + concatena e da resultado
lista_a.extend(lista_b) #extend aplica resultado na lista sendo extendida (não joga pra outra variavel)
print(lista_a,lista_c)