'''
formatação de strings com f-strings

s-string
d-int
f-float
.<numero de digitos>f
x ou X - hex
(caractere)(<>^)(quantidade)
>-esquerda
<-direita
^-centro
sinal - + ou - 
conversion flags - !r !s !a - repr/str/ask
'''

variavel='ABC'
print(f'{variavel}')
print(f'{variavel:>10}')
print(f'{variavel:<10}')
print(f'{variavel:.^10}')
print(f'{1000.6546531354:0=+10,.2f}')
print(f'Hex: {100000:08x}')