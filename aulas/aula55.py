#imprecisão de numeros float

import decimal #esse módulo pode ajudar com o problema
numero2=(decimal.Decimal('0.1')+decimal.Decimal('0.7')) #importante passar o valor como Str
print(0.1+0.7) #=0.79999
#chama double precision float format IEEE754
numero=0.1+0.7
print(f'{numero:.2f}')#limitar a 2 casas decimais arredonda
print(round(numero,10))
print(numero2)
#round arredonda o numero pra cima