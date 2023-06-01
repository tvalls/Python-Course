texto=input('Digite o texto a ser separado: ')
novo_texto=''
for letra in texto:
    print(letra)
    novo_texto+=f'*{letra}'

print(novo_texto)
