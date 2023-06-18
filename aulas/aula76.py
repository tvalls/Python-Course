#dicionários em python (tipo dict)
pessoa={
    'nome':'Thiago',
    'sobrenome':'Valls',
    'idade':31,
    'sexo':'M',
    'peso':92.0,
    'altura':1.86,
    'endereços':[
        {'Rua 1, 123'},
        {'Rua 2, 456'},
    ],

}
# for chave in pessoa:
#     print(chave,':',pessoa[chave])

# print(pessoa)

#métodos de dicionários
#len - quantas chaves
#keys - iterável com as chaves
#values - iterável com os valores
#items - iterável com os itens (chave, valor)
#setdefault - adiciona valor se a chave não existe
#copy - copia o dicionário
#get - retorna o valor da chave, se não existir retorna None
#pop - remove a chave e retorna o valor
#popitem - remove o último item e retorna o valor
#update - atualiza o dicionário com outro dicionário
#clear - limpa o dicionário

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

