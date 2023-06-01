'''
repetições
while
executa ação enquanto condição for verdadeira
'''
string='1'
tamanho=input('Qual o tamanho da piramide? ')
tamanho=int(tamanho)
while len(string)<tamanho:
    print(string)
    string=string+'1'
condicao=True
while condicao:
        nome=input('Qual o seu nome: ')
        if nome=='Sair':
            break
        print(f'Seu nome é {nome}')
