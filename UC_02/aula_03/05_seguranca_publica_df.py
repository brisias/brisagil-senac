import pandas as pd

def percentual(x):
    return "{:.2f}%".format(x)

ocorrencias = [
    ['Rio de Janeiro',6775561,35000], 
    ['Niteroi',515317,2500], 
    ['São Gonçalo',1091737,15000], 
    ['Duque de Caxias',924624,12000], 
    ['Nova Iguaçu',821128,10000], 
    ['Belford Roxo',513118,9000], 
    ['São João de Meriti',471906,8500], 
    ['Petrópolis',306678,1000], 
    ['Volta Redonda',273988,2000], 
    ['Campos dos Goytacazes',507548,4000],
]

colunas = ['Município','População','Roubos']

df_ocorrencias = pd.DataFrame(ocorrencias,columns = colunas)

#métricas gerais
soma_pop_RJ = df_ocorrencias['População'].sum()
media_pop_RJ = df_ocorrencias['População'].mean()
soma_roubo_RJ = df_ocorrencias['Roubos'].sum()
media_roubo_RJ = df_ocorrencias['Roubos'].mean()

#métricas de roubo
maior_roubo = df_ocorrencias['Roubos'].max()
menor_roubo = df_ocorrencias['Roubos'].min()
mun_maior_roubo = df_ocorrencias[df_ocorrencias['Roubos'] == maior_roubo]['Município']
mun_menor_roubo = df_ocorrencias[df_ocorrencias['Roubos'] == menor_roubo]['Município']

#métricas de população
maior_pop = df_ocorrencias['População'].max()
menor_pop = df_ocorrencias['População'].min()
mun_maior_pop = df_ocorrencias[df_ocorrencias['População'] == maior_pop]['Município']
mun_menor_pop = df_ocorrencias[df_ocorrencias['População'] == menor_pop]['Município']

#taxa de roubos a pedestre
taxa_roubo = (df_ocorrencias['Roubos'] / df_ocorrencias['População'] * 100).apply(percentual)

#exibição
print('--------- Tabela Ocorrências -------')
print(df_ocorrencias)
print('\n------- Medidas Descritivas -------')
print(f'A quantidade total de roubos a pedestres no período foi {soma_roubo_RJ}')
print(f'A quantidade média de roubos a pedestres no período foi {media_roubo_RJ:.0f}')
print(f'A população total do estado é {soma_pop_RJ}')
print(f'A população média do estado é {media_pop_RJ:.0f}')
print(f'O maior valor de roubos de pedestres no período foi {maior_roubo}')
print(f'O município que apresentou esse valor foi \n{mun_maior_roubo.values[0]}')
print(f'O menor valor de roubos de pedestres no período foi {menor_roubo}')
print(f'O município que apresentou esse valor foi \n{mun_menor_roubo.values[0]}')
print(f'A maior população encontrada foi {maior_pop}')
print(f'O município com a maior população é \n{mun_maior_pop.values[0]}')
print(f'A menor população encontrada foi {menor_pop}')
print(f'O município com a menor população é \n{mun_menor_pop.values[0]}')
print('\n------- Taxas de Roubo -------')
print(df_ocorrencias['Município'] + "  " + taxa_roubo)