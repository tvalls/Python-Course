value1=input('Digite um valor: ')
value2=input('Digite outro valor: ')
if value1!=value2:
    if value1>value2:
        print('O primeiro valor é maior')
    elif value2>value1:
        print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')