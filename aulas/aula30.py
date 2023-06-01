'''
constante = 'variaveis' que não vão mudar
muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim) (quanto mais afastado da margem mais complexo, então ruim)
'''
#variáveis em caixa alta são CONSTANTES (não devem ser alteradas ao longo do código)
#variáveis em caixa baixa são VARIÁVEIS (podem ser alteradas ao longo do código)

velocidade=61 #velocidade atual do carro
kmatual=99 #posição do carro

RADAR_1=60 #velocidade máxima do radar 1
LOCAL_1=100 #posição do radar 1
RADAR_RANGE=1 #distância onde o radar pega

acima_limite=velocidade>RADAR_1
range_radar=kmatual>=(LOCAL_1-RADAR_RANGE) and kmatual<=(LOCAL_1+RADAR_RANGE)
requisito_multa=range_radar and acima_limite

if velocidade>RADAR_1:
    print('Acima do limite de velocidade')

if requisito_multa:
    print('Veículo autuado')