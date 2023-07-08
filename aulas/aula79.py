#exemplo de uso do Set
letras=()
while True:
    letra=input('Digite uma letra: ')
    if letra.lower() in letras:
        break
    else:
        letras.add(letra.lower())