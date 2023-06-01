'''
Exercício
Peça ao usuário para digitar seu nome
peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    exiba:
        seu nome é (nome)
        seu nome invertido é (nome invertido)
        seu nome contém (ou não) espaços
        seu nome tem (n) letras
        a primeira letra do seu nome é (letra)
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
'''
nome = input('Digite seu nome: ')  
idade = input('Digite sua idade: ')
if not nome or not idade:
    print('Desculpe, você deixou campos vazios')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    elif ' ' not in nome:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
    print('-'*20)