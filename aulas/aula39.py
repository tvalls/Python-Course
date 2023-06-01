'''
iterando strings com while
'''
nome="Thiago Valls"
tamanho_nome=len(nome)
print(nome)
print(f'{nome} tem {tamanho_nome} letras')
indice=0
string='*'
while indice<tamanho_nome:
    string+=nome[indice]
    string+='*'
    indice+=1
print(string)
