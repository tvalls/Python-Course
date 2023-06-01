#or

entrada=input('[E]ntrar [S]air: ')
senha=input('Senha: ')
aut='admin'

if(entrada=='E' or entrada=='e') and senha==aut:
    print('Acesso Permitido')
else:
    print('Acesso Negado')


print(True and True and True) #retorna true, false em qualquer dos valores a expressão inteira é false
print(True or False or 0) #retorna true se qualquer um dos valores for true

string=input('Senha: ') or 'Sem senha'
string2=False or True

print(f'{string} and {string2}')