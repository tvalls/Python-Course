#sets - conjuntos mutáveis
s1=set('Thiago') #set com parenteses itera a string
print(s1)
s2=  {'Thiago'} #set com chaves não itera a string
print (s2)
#são eficientes para remover valores duplicados
s3={1,3,3,5,2,1}
l1=[1,3,3,5,2,1] #lista não remove duplicados
print(l1,s3)

'''
Exemplo para remover itens duplicados de listas
l1=[1,3,3,5,2,1]
s1=set(l1)
l2=list(s1)
print(l2) #resultado = l1 sem duplicados, porém não garante ordem
set não aceita valores mutáveis como listas e dicionários (ou sets dentro de sets)
s1={1,2,3,[4,5,6]} #erro
'''

#metodos de sets
#add - adiciona um item ao set
#update - adiciona vários itens ao set
#clear - limpa o set
#discard - remove um item do set

#operadores de sets
#union - une dois sets   |
#intersection - retorna os itens em comum entre dois sets  &
#difference - retorna os itens que não estão em comum entre dois sets   -
#symmetric_difference - retorna os itens que não estão em comum entre dois sets   ^

s1={1,2,3}
s2={2,3,4}
s3=s1|s2 #union
s4=s1&s2 #intersection
s5=s1-s2 #difference
s6=s1^s2 #symmetric_difference
print(s3,s4,s5,s6, sep='\n')