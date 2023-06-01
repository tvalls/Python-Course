frase='O Python é uma linguagem de programação multiparadigma. Python oi criado por Guido van Rossum.'
# print(frase.lower().count('a'))

i=0
mais_reps=0
letra_mais_reps=''
while i < len(frase):
    letra_atual=frase[i]
    i+=1
    if letra_atual != ' ':
        reps=frase.count(letra_atual)
        if reps > mais_reps:
            mais_reps=reps
            letra_mais_reps=letra_atual
        elif reps==mais_reps and letra_atual not in letra_mais_reps:
            letra_mais_reps+=' '
            letra_mais_reps+=letra_atual
else:
    print(f'A(s) letra(s) {letra_mais_reps} repete(m) {mais_reps} vezes.')
    # print(f'{letra atual}: {reps}')