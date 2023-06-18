#exercício - sistema de perguntas e respostas
perguntas=[
    {
        'Pergunta':'Quanto é 2+2?',
        'Opções':['1','2','4','5'],
        'Resposta':'2',
    },
    {
        'Pergunta':'Quanto é 5*5?',
        'Opções':['25','55','10','51'],
        'Resposta':'0',
    },
    {
        'Pergunta':'Quanto é 10/2?',
        'Opções':['4','5','2','1'],
        'Resposta':'1',
    },
]
contador=0
for questao in perguntas:
    print(questao['Pergunta'])
    alternativa=0
    for opcao in questao['Opções']:
        print(f'{alternativa}) {opcao}')
        alternativa+=1
    resposta=str(input('Escolha uma opção: '))
    if resposta == questao['Resposta']:
        print('Resposta correta.')
        contador+=1
    else:
        print('Resposta incorreta.')
print(f'Você acertou {contador} de 3 perguntas.')
