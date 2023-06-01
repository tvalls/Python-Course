'''
interpolação de strings
s - string
d e i - int
f - float
x e X - hex

pode ser utilizado format ou fstring em vez disso
'''
nome='Thiago'
preco=1000.958472
variavel='%s, o preço é R$%.2f' %(nome,preco)
print(variavel)
print('O hex de %d é %04x' %(1500,1500))