"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# palavra='PINCESA'
# iterador=iter(palavra)
# caracteres=len(palavra)
# escondida=f'*'*caracteres
# indice=0
# qtd_tentativa=0
# print('JOGO DA PALAVRA SECRETA!')
# print('Letra por letra, tente adivinhar a palavra secreta')
# print(f'A palavra secreta contém {caracteres} letras: {escondida}')
# while escondida !='PINCESA':
#     tentativa=input('Tente adivinhar uma letra: ').upper()
#     qtd_tentativa+=1
#     if tentativa in palavra:
#         indice=palavra.index(tentativa)
#         escondida=escondida[:indice]+tentativa+escondida[indice+1:]
#         print(escondida)
#     else:
#         print(f'A letra {tentativa} não está na palavra {escondida}')
# print(f'Parabéns, a palavra secreta é {escondida}! Você acertou em {qtd_tentativa} tentativas!')

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0