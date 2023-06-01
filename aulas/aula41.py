#while/else
string='valor qualquer'
i=0
while i<len(string):
    letra=string[i]
    print(letra)
    i+=1
    if letra==' ':
        break
else:
    print('String sem espaços')
    print('Fim') #se tivesse um break dentro do while o else não é executado, se o while executar por completo o else é executado