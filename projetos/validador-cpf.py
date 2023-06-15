"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
import os
import random
while True:
    dv1=0
    dv1check=0
    dv2=0
    dv2check=0
    somatoria=0
    somatoria2=0
    mult=10
    mult2=11
    os.system('cls')
    decide=input('Selecione uma opção:\n[V]alidar CPF | [G]erar CPF Válido | [S]air:\n')
    try:
        decide=decide.upper()
    except:
        print('Opção inválida')
        continue
    if decide=='V':
        cpf=input('Digite o CPF sem pontos e traço:\n')
        if len(cpf) != 11:
            print('O CPF deve conter 11 dígitos, sem pontos e sem traços.')
            x=input('Aperte Enter para continuar')
            continue
        elif cpf == cpf[0]*len(cpf):
            print('CPF inválido!')
            input('Aperte Enter para continuar')
            continue
        else:
            try:
                dv2=int(cpf[-1])
                dv1=int(cpf[-2])
                for indice,digito in enumerate(cpf):
                    if indice>8:
                        continue
                    else:
                        somatoria=somatoria+(int(digito)*mult)
                        mult-=1
                dv1check=(somatoria*10)%11
                dv1check = dv1check if dv1check<=9 else 0
                for indice,digito in enumerate(cpf):
                    if indice>9:
                        continue
                    else:
                        somatoria2=somatoria2+(int(digito)*mult2)
                        mult2-=1
                dv2check=(somatoria2*10)%11
                dv2check=dv2check if dv2check<=9 else 0
                if dv1==dv1check and dv2==dv2check:
                    print(f'O CPF {cpf} é válido!')
                    input('Aperte enter para continuar')
                else:
                    print(f'O CPF {cpf} é INVÁLIDO!\n Para ser válido deveria ter os dígitos {dv1check}{dv2check} em vez de {dv1}{dv2}')
                    input('Aperte enter para continuar')
            except:
                print('O CPF digitado é inválido.')
                input('Aperte enter para continuar')
    elif decide=='G':
        cpf=random.randint(100000000,999999999)
        cpf=str(cpf)
        for indice,digito in enumerate(cpf):
            if indice>8:
                continue
            else:
                somatoria=somatoria+(int(digito)*mult)
                mult-=1
        dv1check=(somatoria*10)%11
        dv1check = dv1check if dv1check<=9 else 0
        for indice,digito in enumerate(cpf):
            if indice>9:
                continue
            else:
                somatoria2=somatoria2+(int(digito)*mult2)
                mult2-=1
        cpf_formatado=(f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{dv1check}{dv2check}')

        print(f'CPF: {cpf_formatado}')
        input('Aperte enter para continuar')
        continue
    elif decide=='S':
        break
    else:
        print('Opção não encontrada')
        input('Aperte enter para continuar.')
        continue