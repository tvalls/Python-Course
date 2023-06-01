#and or not
#and: todas as condições precisam ser verdadeiras
#or: uma ou outra condição precisa ser verdadeira
#considerado falsy: 0, 0.0, '' e False

user='admin'
password='admin'



entrada=input('Usuário:')
entrada2=input('Senha:')

if entrada==user and entrada2==password:
    print('Acesso Permitido')
elif entrada==user and entrada2!=password:
    print('Senha Inválida')
elif entrada!=user and entrada2==password:
    print('Usuário Inválido')
elif entrada=='' or entrada2=='':
    print('É necessário digitar um usuário e senha.')
else:
    print('Acesso Negado')


