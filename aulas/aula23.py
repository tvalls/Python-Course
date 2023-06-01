#operador not para inverter bool: not True = False | not False = True

senha=input('Senha: ')

if not senha:
    print('Senha Vazia')
elif senha=='admin':
    print('Entra')
else:
    print('Senha Invalida')
