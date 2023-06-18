#Higher order functions
def soma(*args):
    return sum(args)
def executa(funcao, *args):
    return funcao(*args)

v=executa(soma,1,2,3,4,5)
print(v) 