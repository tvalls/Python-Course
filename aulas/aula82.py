def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x+y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return multiplicador*numero
    return multiplica

#lambda soma
print(executa(lambda x,y: x+y, 1, 2))

