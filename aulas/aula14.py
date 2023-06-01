a='A'
b='B'
c=1.1
formato='a={} b={} e c={:.2f}'.format(a, b, c) #similar à f-string, onde cada colchete busca sequencialmente os argumentos do format() e dentro da chave é possível formatar o float com :.2f para determinar casas decimais
formato='a={0} b={1} e c={2:.2f}. Sim, c={2:.2f}'.format(a, b, c) #também é possível determinar qual argumento buscar numerando dentro da chave a partir de 0 o argumento desejado (dessa forma é possível repetir argumentos)
formato='a={nome1} b={letra} e c={numero:.2f}. Sim, c={numero:.2f}'.format(nome1=a, letra=b, numero=c) #é possível nomear os parâmetros e chama-los pelo nome (todos parâmetros após um parametro nomeado devem ser nomeados)
print(formato)
