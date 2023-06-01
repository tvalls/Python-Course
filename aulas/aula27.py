#fatiamento de strings
'''
-987654321 
 Olá mundo
 012345678

Fatiamento [i:f:p][::]
função len retorna qt de caracteres da str
'''
variavel='Olá mundo'
print(variavel[2]) #retorna caracere 2
print(variavel[4:]) #fatia a partir de 4 até fim (se incluir indice final ele retorna a qtd de caracteres isolada)
print(variavel[4:8]) #caractere 8 não é incluido
print(variavel[::2]) #fatia em 2 em 2
print(variavel[:8]) #fatia do inicio até o 8
print(variavel[::-1]) #inverte a sequencia
print(variavel[::-2]) #inverte a sequencia em 2 em 2

qtd=len(variavel) #conta os caracteres
print(qtd)