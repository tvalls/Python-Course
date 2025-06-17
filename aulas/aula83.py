#empacotamento e desempacotamento de dicionários

pessoa = {
    'nome': 'João',
    'idade': 25,
    'sexo': 'M'
}

(a1,a2),(b1,b2),(c1,c2)=pessoa.items()
print(a1,a2,b1,b2,c1,c2)

dados_pessoa={
    'nome': 'João',
    'idade': 25,
    'sexo': 'M',
    'altura': 1.75
}

#juntar dicionarios
pessoa_completa={**pessoa, **dados_pessoa}
print('')
print(pessoa_completa)