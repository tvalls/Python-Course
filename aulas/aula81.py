#Função lambda em python
lista=[
    {'nome':'joao','idade':18},
    {'nome':'maria','idade':20},
    {'nome':'jose','idade':30},
    {'nome':'pedro','idade':40},
]
print(sorted(lista, key=lambda item: item['idade'], reverse=True)) #ordena a lista por idade sem precisar definir função (lambda define função dentro da linha)

