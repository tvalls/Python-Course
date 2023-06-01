#operadores in e not in
#str são iteráveis
#0 1 2 3 4 5
#T H I A G O
#-6-5-4-3-2-1

# nome='Thiago'
# print(nome[1])
# print(nome[-2])
# print('g' in nome)
# print('j' in nome)
# print('Thi' in nome)
# print('Jao' not in nome)

frase=input('Digite a frase: ')
encontrar=input('Digite a pesquisa: ')

if encontrar in frase:
    print('A palavra {} está na frase'.format(encontrar))
else:
    print('A palavra {} não está na frase'.format(encontrar))