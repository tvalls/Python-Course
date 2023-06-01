contador=0
maximo=input('Digite o número máximo: ')
try:
    maximo=int(maximo)
    while contador<=maximo:
        print(contador)
        contador=contador+1
    print('Acabou')
except:
    print('Não reconheço esse número.')