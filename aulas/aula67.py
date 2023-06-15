#valores padrão para parametros em função - caso o parametro não receba argumento o valor padrão será utilizado
#Refatorar: editar o código

def soma(x,y,z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}',x+y+z)
    else:
        print(f'{x=} {y=}', x+y)

soma(1,2)
soma(3,5,7)
soma(100,200)
