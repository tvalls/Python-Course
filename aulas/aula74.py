#closure e funções que retornam outras funções

def criar_saudacao(saudacao,nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar
s1=criar_saudacao('Olá','Maria')
print(s1())