#listas de listas e indices

salas=[
    ['aluno1','aluno2'], #0
    ['aluno1'], #1
    ['aluno1','aluno2','aluno3',(0,10,20,30,40)],#2

]

print(salas[2][3][2])

for sala in salas:
    print(sala)

for aluno in salas[0]:
    print(aluno)

for numero in salas[2][3]:
    print(numero)