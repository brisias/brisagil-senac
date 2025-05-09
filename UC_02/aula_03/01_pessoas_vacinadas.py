import pandas as pd

def percentual(x):
    return "{:.2f}%".format(x)

def milhar(y):
    return "{:,.0f}".format(y)

populacao = pd.Series([213317639, 214477744, 215574303, 216687971], index = ['2021','2022','2023','2024'])
vacinades = pd.Series([30000000,25000000,10000000,5000000], index = ['2021','2022','2023','2024'])

tx_vacinacao = ((vacinades / populacao)*100).apply(percentual)
total_tx_vacinacao = (vacinades.sum() / populacao.tail(1).iloc[0]) * 100

print('-----------------------------------')
print('_DADOS DA POPULAÇÃO BRASILEIRA_')
print(populacao.apply(milhar))
print(f'O acumulado de pessoas é: \n{populacao.tail(1).iloc[0]}') #sintaxe para puxar a última posição de uma série, os () são usados no tail pois é uma função; já o iloc está referenciando o índice, para que ele não apareça
print(f'A média de pessoas é: \n{populacao.mean():.0f}')

print('\n-----------------------------------')
print('_DADOS DA POPULAÇÃO VACINADA_')
print(vacinades.apply(milhar))
print(f'O acumulado de pessoas vacinadas nos últimos anos: \n{vacinades.sum()}')
print(f'Média da população vacinada: \n{vacinades.mean():.0f}')

print('\n-----------------------------------')
print('_PERCENTUAIS DE PESSOAS VACINADAS_')
print(f'Taxa de vacinação por ano: \n{tx_vacinacao}')
print(f'Taxa de vacinação total nos últimos 4 anos: {total_tx_vacinacao:.2f}%')