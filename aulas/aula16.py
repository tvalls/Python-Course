#if / elif / else (elif = elseif)
entrada=input('Aperte 1 para entrar, 2 para sair:')
if entrada == '1':
    print('Entrou')
elif entrada=='2':
    print('Saiu')
else:
    print('Opção inválida')
print('fora dos blocos')