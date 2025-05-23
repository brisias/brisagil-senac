import pandas as pd
import numpy as np

endereco_dados = '00.BASES\BaseDPEvolucaoMensalCisp(1).csv'
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
df_roubo_carga = df_ocorrencias[['munic','ano','roubo_carga']]
df_roubo_carga = df_roubo_carga[df_roubo_carga['ano'].between(2003,2024)]
df_roubo_carga = df_roubo_carga.groupby(['munic']).sum(['roubo_carga']).reset_index()

array_roubo_carga = np.array(df_roubo_carga['roubo_carga'])

media_roubo_carga = np.mean(array_roubo_carga)
mediana_roubo_carga = np.median(array_roubo_carga)
max_roubo_carga = np.max(array_roubo_carga)
min_roubo_carga = np.min(array_roubo_carga)
distancia_roubo_carga = abs((media_roubo_carga - mediana_roubo_carga) / mediana_roubo_carga * 100)
amplitude_roubo_carga = max_roubo_carga - min_roubo_carga

q1_roubo_carga = np.quantile(array_roubo_carga, 0.25, method='weibull')
q2_roubo_carga = np.quantile(array_roubo_carga, 0.50, method='weibull')
q3_roubo_carga = np.quantile(array_roubo_carga, 0.75, method='weibull')
iqr_roubo_carga = q3_roubo_carga - q1_roubo_carga

limite_superior_roubo_carga = q3_roubo_carga + (1.5*iqr_roubo_carga)
limite_inferior_roubo_carga = q1_roubo_carga - (1.5*iqr_roubo_carga)

df_roubo_carga_outliers_inferiores = df_roubo_carga[df_roubo_carga['roubo_carga'] < limite_inferior_roubo_carga]
df_roubo_carga_outliers_superiores = df_roubo_carga[df_roubo_carga['roubo_carga'] > limite_superior_roubo_carga]

print('\n---------- DataFrame Roubo de Cargas ----------')
print(df_roubo_carga.drop(columns='ano').sort_values(by='roubo_carga', ascending=False))

print('\n---------- Métricas Roubo de Cargas ----------')
print(f'Média: {media_roubo_carga:.0f}')
print(f'Mediana: {mediana_roubo_carga:.0f}')
print(f'Distância: {distancia_roubo_carga:.2f}%')
print(f'Maior: {max_roubo_carga:.0f}')
print(f'Menor: {min_roubo_carga:.0f}')
print(f'Amplitude: {amplitude_roubo_carga:.0f}')

print(f'\n1º Quartil(25%): {q1_roubo_carga:.0f}')
print(f'2º Quartil(50%): {q2_roubo_carga:.0f}')
print(f'3º Quartil(75%): {q3_roubo_carga:.0f}')
print(f'IQR: {iqr_roubo_carga:.0f}')

print(f'\nLimite Inferior: {limite_inferior_roubo_carga:.0f}')
print(f'Limite Superior: {limite_superior_roubo_carga:.0f}')

if len(df_roubo_carga_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n------------ Outliers Inferiores ------------')
    print(df_roubo_carga_outliers_inferiores)
if len(df_roubo_carga_outliers_superiores) == 0:
    print('\nNão existem outliers superiores')
else:
    print('\n------------ Outliers Superiores ------------')
    print(df_roubo_carga_outliers_superiores.drop(columns='ano').sort_values(by='roubo_carga', ascending=False).head(10))