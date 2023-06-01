#variáveis devem iniciar com letras minúsculas, podem ter números e underline - nome_variavel1
user_name=input('User:')
password=input('Password:')
numero=input('Número:')
int_num=int(numero)
if(password=='teste'):
    print('Bem vindo,', user_name)
    print(int_num*int_num)
else:
    print('Senha inválida')
