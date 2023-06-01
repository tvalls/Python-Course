'''
flag(bandeira)-marcar local
none=não valor
is e is not = é ou não é (tipo, valor, identidade)
id=identidade
'''

v1='a'
v2='a'
print(id(v1), id(v2), sep="\n") 
print('identidade na memória é a mesma porque o valor literal é igual')

variavel=None

if v1=='a':
    variavel=True
    print('passou no if')
else:
    print('não passou no if')

if variavel is None:
    print('não passou no if')
if variavel is not None:
    print('Passou no if')
    