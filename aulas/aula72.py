#Exercícios com funções

#crie uma função que multiplica todos os argumentos não nomeado recebidos
#retorne o total para uma variável e mostre o valor da variável

#crie uma função que fala se um número é par ou ímpar
#retorne se o número é par ou ímpar

def multiplica(*args):
    total=1
    for n in args:
        total*=n
    return total
resultado=multiplica(1,2,3,4,5,6,7,8,9,10)
print(resultado)

def par_ou_impar(n):
    if n%2==0:
        return 'par'
    return 'ímpar'

try:
    numero=int(input('Digite um número: '))
except ValueError:
    print('Digite apenas números inteiros.')
else:
    print(f'O número {numero} é {par_ou_impar(numero)}')