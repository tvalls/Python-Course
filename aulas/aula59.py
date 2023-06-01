#desempacotamento em chamadas de métodos e funções
string='ABCD'
lista=['Maria', 'Helena', 'Eduarda']
tupla='Python', 'é', 'legal'
salas=[
    ['aluno1','aluno2'], #0
    ['aluno1'], #1
    ['aluno1','aluno2','aluno3',(0,10,20,30,40)],#2

]
# a, *_, u=lista #pega primeiro valor, deixa resto, pega ultimo valor
# print(a,u)

# print(*lista) #desempacota cada valor da lista no print
# print(*string)
# print(*tupla)

print(*salas, sep="\n")

