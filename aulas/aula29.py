#try/except - try: tenta executar o código - except: ocorreu algum erro ao tentar executar
numero=input('Digite um número: ')
try:
    print(f'O dobro de {float(numero)} é {2*float(numero)}')
except:
    print(f'{numero} não é um número válido.')