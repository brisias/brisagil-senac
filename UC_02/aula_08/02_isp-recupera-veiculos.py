import pandas as pd
import numpy as np

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
df_recupera_veiculos = df_ocorrencias[['ano','recuperacao_veiculos','aisp']]
df_recupera_veiculos = df_recupera_veiculos[df_recupera_veiculos['ano'].between(2003,2024)]
df_recupera_veiculos = df_recupera_veiculos.groupby(['aisp']).sum(['recuperacao_veiculos']).reset_index()

array_recupera_veiculos = np.array(df_recupera_veiculos['recuperacao_veiculos'])

media_recupera_veiculos = np.mean(array_recupera_veiculos)
mediana_recupera_veiculos = np.median(array_recupera_veiculos)
max_recupera_veiculos = np.max(array_recupera_veiculos)
min_recupera_veiculos = np.min(array_recupera_veiculos)
distancia_recupera_veiculos = abs((media_recupera_veiculos - mediana_recupera_veiculos) / mediana_recupera_veiculos * 100)
amplitude_recupera_veiculos = max_recupera_veiculos - min_recupera_veiculos

q1_recupera_veiculos = np.quantile(array_recupera_veiculos, 0.25, method='weibull')
q2_recupera_veiculos = np.quantile(array_recupera_veiculos, 0.50, method='weibull')
q3_recupera_veiculos = np.quantile(array_recupera_veiculos, 0.75, method='weibull')
iqr_recupera_veiculos = q3_recupera_veiculos - q1_recupera_veiculos

limite_superior_recupera_veiculos = q3_recupera_veiculos + (1.5*iqr_recupera_veiculos)
limite_inferior_recupera_veiculos = q1_recupera_veiculos - (1.5*iqr_recupera_veiculos)

df_recupera_veiculos_limite_superior = df_recupera_veiculos[df_recupera_veiculos['recuperacao_veiculos'] > limite_superior_recupera_veiculos]
df_recupera_veiculos_limite_inferior = df_recupera_veiculos[df_recupera_veiculos['recuperacao_veiculos'] < limite_inferior_recupera_veiculos]

print('\n---------- DataFrame Recuperação de Veículos ----------')
print(df_recupera_veiculos)

print('\n---------- Métricas Recuperação de Veículos ----------')
print(f'Média: {media_recupera_veiculos:.0f}')
print(f'Mediana: {mediana_recupera_veiculos:.0f}')
print(f'Distância: {distancia_recupera_veiculos:.2f}%')
print(f'Maior: {max_recupera_veiculos:.0f}')
print(f'Menor: {min_recupera_veiculos:.0f}')
print(f'Amplitude: {amplitude_recupera_veiculos:.0f}')

print(f'\n1º Quartil(25%): {q1_recupera_veiculos:.0f}')
print(f'2º Quartil(50%): {q2_recupera_veiculos:.0f}')    
print(f'3º Quartil(75%): {q3_recupera_veiculos:.0f}')
print(f'IQR: {iqr_recupera_veiculos:.0f}')

print(f'\nLimite Inferior: {limite_inferior_recupera_veiculos:.0f}')
print(f'Limite Superior: {limite_superior_recupera_veiculos:.0f}')

if len(df_recupera_veiculos_limite_inferior) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n------------ Outliers Inferiores ------------')
    print(df_recupera_veiculos_limite_inferior)
if len(df_recupera_veiculos_limite_superior) == 0:    
    print('\nNão existem outliers superiores')
else:
    print('\n------------ Outliers Superiores ------------')
    print(df_recupera_veiculos_limite_superior.drop(columns='ano').sort_values(by='recuperacao_veiculos', ascending=False).head(10))