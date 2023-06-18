#exercícios
#crie funções que duplicam, triplicam e quadruplicam o número recebido como parametro

# def duplicar(numero):
#     return numero * 2
# def triplicar(numero):
#     return numero * 3
# def quadruplicar(numero):
#     return numero * 4

# n= int(input('Digite um número: '))
# print(f'O dobro de {n} é {duplicar(n)}')
# print(f'O triplo de {n} é {triplicar(n)}')
# print(f'O quadruplo de {n} é {quadruplicar(n)}')

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
duplicar=criar_multiplicador(2)
triplicar=criar_multiplicador(3)
quadruplicar=criar_multiplicador(4)
print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
