while True:
    var1=input('Digite o primeiro número: ')
    try:
        var1=float(var1)
    except Exception as error:
        print(f'{var1} não é um valor válido. Erro: {error}')
        continue
    var2=input('Digite o segundo número: ')
    try:
        var2=float(var2)
    except Exception as error:
        print(f'{var2} não é um valor válido. Erro: {error}')
        continue
    op=input('Escolha a operação desejada: [+] [-] [*] [/]')
    permitido='+-*/'
    if op in permitido and len(op)==1:
        try:
            print(f'{var1} {op} {var2} = {eval(f"{var1} {op} {var2}")}')
        except Exception as error:
            print(f'Erro: {error}')
    else:
        print('Operação não reconhecida.')
        continue  
    sair=input('Deseja sair? [s]im:').lower().startswith('s')
    if sair:
        break