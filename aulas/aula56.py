#split e join com list e str
frase='Olha só que, coisa interessante'
lista=frase.split() #sem argumentos divite nos espaços em branco
i=0
for item in lista:
    print(i,item)
    i+=1
i=0
lista2=frase.split(', ') #com argumentos remove o argumento e divide nele
for item in lista2:
    print(item)
    i+=1

texto1="The quick brown fox"
texto2="Jumps over the lazy dog"
texto_unido='\n'.join(texto1)
print(texto_unido)