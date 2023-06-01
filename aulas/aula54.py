'''
Faça uma lista de compras com listas
o usuário deve ter a possibilidade de [i]nserir [a]pagar e [l]istar
não permita que o programa quebre com erros de índices inexistentes na lista
'''
import os
lista=[]
print('Bem vindo(a) à sua Lista de Compras!\n')
saida=0
while not saida:
    entrada=input('Escolha uma opção:\n[L]istar, [I]nserir, [A]pagar ou [S]air\n')
    entrada=entrada.upper()
    os.system('cls')
    if entrada=='S':
        if not lista:
            print('Sua lista está vazia. Até mais!')
            saida=1
            continue
        else:
            print('Aqui está sua lista:')
            i=0
            for indice in lista:
                print(i,indice)
                i+=1
            print('Até mais!')
            saida=1
            continue
    elif entrada=='I':
        item=input('O que deseja adicionar à lista? \n')
        lista.append(item)
        os.system('cls')
        print('Adicionado.')
    elif entrada=='A':
        i=0
        for indice in lista:
            print(i,indice)
            i+=1
        apagar=input('Qual número deseja apagar?\n')
        os.system('cls')
        if apagar.isnumeric==False:
            print('Digite um número')
            continue
        elif int(apagar)>len(lista):
            print('Digite um número presente na lista')
            continue
        else:
            apagar=int(apagar)
            del lista[apagar]
            i=0
            print('Sua nova lista:\n')
            for indice in lista:
                print(i,indice)
                i+=1
    elif entrada=="L":
        i=0
        for indice in lista:
            print(i,indice)
            i+=1
        continue
    else:
        print('Não entendi o seu comando. Por favor, tente novamente!')
        continue
