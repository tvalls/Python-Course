for i in range(10):
    if i==2:
        print('pula')
        continue
    if i==8:
        print('i=8 else não executa')
        break
    for j in range(1,3):
        print(i,j)
else:
    print('sucesso')
