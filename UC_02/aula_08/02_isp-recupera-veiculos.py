import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

df_recupera_veiculos_outliers_superior = df_recupera_veiculos[df_recupera_veiculos['recuperacao_veiculos'] > limite_superior_recupera_veiculos]
df_recupera_veiculos_outliers_inferior = df_recupera_veiculos[df_recupera_veiculos['recuperacao_veiculos'] < limite_inferior_recupera_veiculos]

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

if len(df_recupera_veiculos_outliers_inferior) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n------------ Outliers Inferiores ------------')
    print(df_recupera_veiculos_outliers_inferior)
if len(df_recupera_veiculos_outliers_superior) == 0:    
    print('\nNão existem outliers superiores')
else:
    print('\n------------ Outliers Superiores ------------')
    print(df_recupera_veiculos_outliers_superior.drop(columns='ano').sort_values(by='recuperacao_veiculos', ascending=False).head(10))

variancia_recupera_veiculos = np.var(array_recupera_veiculos)
distancia_var_recupera_veiculos = variancia_recupera_veiculos / (media_recupera_veiculos**2)

desvio_padrao_recupera_veiculos = np.std(array_recupera_veiculos)
coeficiente_variacao_recupera_veiculos = desvio_padrao_recupera_veiculos / media_recupera_veiculos

print('\n---------- Visualizando dados sobre recuperação de veículos ----------')
fig, axs = plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Recuperação de Veículos (2003-2024)', fontsize=15)

plt.subplot(2,2,1)
plt.title('Boxplot das Recuperações de Veículos', fontsize=13)
plt.boxplot(array_recupera_veiculos,vert=False,showmeans=True)

plt.subplot(2,2,2)
plt.title('Histograma das Recuperações de Veículos', fontsize=13)
plt.hist(array_recupera_veiculos,bins=100,edgecolor='black')

df_recupera_veiculos_outliers_superiores_order = df_recupera_veiculos_outliers_superior.sort_values(by='recuperacao_veiculos', ascending=True)
plt.subplot(2,2,3)
plt.title('Outliers de Recuperação de Veículos', fontsize=13)
plt.barh(df_recupera_veiculos_outliers_superiores_order['aisp'].astype(str),df_recupera_veiculos_outliers_superiores_order['recuperacao_veiculos'])

plt.subplot(2,2,4)
plt.title('Medidas descritivas das Recuperações de Veículos', fontsize=13)
plt.axis('off')
plt.text(0.05,0.9,f'Média de Recuperação de Veículos: {media_recupera_veiculos:.0f}', fontsize=11)
plt.text(0.05,0.75,f'Mediana de Recuperação de Veículos: {mediana_recupera_veiculos:.0f}', fontsize=11)
plt.text(0.05,0.6,f'Distância entre a média e a mediana de Recuperação de veículos: {distancia_recupera_veiculos:.2f}%', fontsize=11)
plt.text(0.05,0.45,f'Maior Valor de Recuperação de Veículos: {max_recupera_veiculos:.0f}', fontsize=11)
plt.text(0.05,0.3,f'Menor Valor de Recuperação de Veículos: {min_recupera_veiculos:.0f}', fontsize=11)
plt.text(0.05,0.15,f'O coeficiente de variação de Recuperação de Veículos: {coeficiente_variacao_recupera_veiculos:.2f}', fontsize=11)
plt.text(0.05,0,f'A distância da variância de Recuperação de Veículos: {distancia_var_recupera_veiculos:.2f}', fontsize=11)
plt.show()