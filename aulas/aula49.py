# lista=[10,20,30,40]
# print(lista)
# numero=lista[2]
# print(numero)
# lista[2]=300
# print(numero)
# print(lista)
# del lista[2]
# print(lista)
# lista.append(300)
# print(lista)

lista=[1]
i=1
j=2
k=3
first_run=True
while i<200:
    if first_run:
        lista.append(i)
        lista.append(j)
        lista.append(k)
        i=j
        j=k
        k=i+j
        first_run=False
    else:
        lista.append(k)
        i=j
        j=k
        k=i+j

print(f'Fibonacci: {lista[0::]}')