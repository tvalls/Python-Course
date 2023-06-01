"""
EXERCÍCIO

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero=input('Digite um número inteiro: ')
try:
    numero=int(numero)
    verif_par=numero%2
    if verif_par==0:
        print(f'O número {numero} é um número par')
    else:
        print(f'O número {numero} é um número ímpar')
except:
    print('Este não é um número inteiro válido!')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario=input('Que horas são?')
try:
    horario=int(horario)
    manha=horario>=0 and horario<12
    tarde=horario>=12 and horario<18
    noite=horario>=18 and horario<24

    if manha:
        print('Bom dia!')
    elif tarde:
        print('Boa tarde!')
    elif noite:
        print('Boa noite!')
    else:
        print('{horario} não é um horário válido.')
except:
    print(f'{horario} não é um horário válido. Digite apenas a hora, sem minutos, no formato 24 horas')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome=input('Qual seu primeiro nome?')
if nome:
    qtd_letras=len(nome)
    curto=qtd_letras<=4
    normal=qtd_letras>=5 and qtd_letras<=6
    grande=qtd_letras>6

    if curto:
        print(f'Seu nome, {nome}, é curto.')
    elif normal:
        print(f'Seu nome, {nome}, é normal.')
    elif grande:
        print(f'Seu nome, {nome}, é muito grande.')
else:
    print('Não reconheci seu nome.')


