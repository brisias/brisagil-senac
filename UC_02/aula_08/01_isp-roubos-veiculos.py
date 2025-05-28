import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
df_roubo_automoveis = df_ocorrencias[['ano','roubo_veiculo','cisp']]
df_roubo_automoveis = df_roubo_automoveis[df_roubo_automoveis['ano'].between(2003,2024)]
df_roubo_automoveis = df_roubo_automoveis.groupby(['cisp']).sum(['roubo_veiculo']).reset_index()

array_roubo_automoveis = np.array(df_roubo_automoveis['roubo_veiculo'])

media_roubo_automoveis = np.mean(array_roubo_automoveis)
maior_roubo_automoveis = np.max(array_roubo_automoveis)
menor_roubo_automoveis = np.min(array_roubo_automoveis)
mediana_roubo_automoveis = np.median(array_roubo_automoveis)
distancia_roubo_automoveis = abs((media_roubo_automoveis - mediana_roubo_automoveis) / mediana_roubo_automoveis * 100)
amplitude_roubo_automoveis = maior_roubo_automoveis - menor_roubo_automoveis

q1_roubo_automoveis = np.quantile(array_roubo_automoveis, 0.25, method='weibull')
q2_roubo_automoveis = np.quantile(array_roubo_automoveis, 0.50, method='weibull')
q3_roubo_automoveis = np.quantile(array_roubo_automoveis, 0.75, method='weibull')
iqr_roubo_automoveis = q3_roubo_automoveis - q1_roubo_automoveis

limite_superior_roubo_automoveis = q3_roubo_automoveis + (1.5*iqr_roubo_automoveis)
limite_inferior_roubo_automoveis = q1_roubo_automoveis - (1.5*iqr_roubo_automoveis)

df_rb_auto_outliers_superiores = df_roubo_automoveis[df_roubo_automoveis['roubo_veiculo'] > limite_superior_roubo_automoveis]
df_rb_auto_outliers_inferiores = df_roubo_automoveis[df_roubo_automoveis['roubo_veiculo'] < limite_inferior_roubo_automoveis]

variancia_roubo_automoveis = np.var(array_roubo_automoveis)
distancia_var_rb_auto = variancia_roubo_automoveis / (media_roubo_automoveis**2)

desvio_padrao_roubo_automoveis = np.std(array_roubo_automoveis)
coeficiente_variacao_roubo_automoveis = desvio_padrao_roubo_automoveis / media_roubo_automoveis

print('\n---------- DataFrame Roubo de Automoveis ----------')
print(df_roubo_automoveis.drop(columns='ano').sort_values(by='roubo_veiculo', ascending=False))

print('\n---------- Métricas Roubo de Automoveis ----------')
print(f'Média: {media_roubo_automoveis:.0f}')
print(f'Mediana: {mediana_roubo_automoveis:.0f}')
print(f'Distância: {distancia_roubo_automoveis:.2f}%')
print(f'Maior: {maior_roubo_automoveis:.0f}')
print(f'Menor: {menor_roubo_automoveis:.0f}')
print(f'Amplitude: {amplitude_roubo_automoveis:.0f}')

print(f'\n1º Quartil(25%): {q1_roubo_automoveis:.0f}')
print(f'2º Quartil(50%): {q2_roubo_automoveis:.0f}')
print(f'3º Quartil(75%): {q3_roubo_automoveis:.0f}')
print(f'IQR: {iqr_roubo_automoveis:.0f}')

print(f'\nLimite Inferior: {limite_inferior_roubo_automoveis:.0f}')
print(f'Limite Superior: {limite_superior_roubo_automoveis:.0f}')

if len(df_rb_auto_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n------------ Outliers Inferiores ------------')
    print(df_rb_auto_outliers_inferiores)
if len(df_rb_auto_outliers_superiores) == 0:
    print('\nNão existem outliers superiores')
else:
    print('\n------------ Outliers Superiores ------------')
    print(df_rb_auto_outliers_superiores.drop(columns='ano').sort_values(by='roubo_veiculo', ascending=False).head(10))

print('\n---------- Visualizando dados sobre roubo de veículos ----------')
fig, axs = plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Roubo de Veículos')

plt.subplot(2,2,1)
plt.title('Boxplot dos Roubos de Veículos')
plt.boxplot(array_roubo_automoveis,vert=False,showmeans=True)

plt.subplot(2,2,2)
plt.title('Histograma dos Roubos de Veículos')
plt.hist(array_roubo_automoveis,bins=100,edgecolor='black')

df_rb_auto_outliers_superiores_order = df_rb_auto_outliers_superiores.sort_values(by='roubo_veiculo', ascending=True)
plt.subplot(2,2,3)
plt.title('Outliers dos Roubos de Veículos')
plt.barh(df_rb_auto_outliers_superiores_order['cisp'].astype(str),df_rb_auto_outliers_superiores_order['roubo_veiculo'])

plt.subplot(2,2,4)
plt.title('Medidas descritivas dos Roubos de Veículos')
plt.axis('off')
plt.text(0.1,0.9,f'Média de Roubos de Veículos: {media_roubo_automoveis:.0f}')
plt.text(0.2,0.8,f'Mediana de Roubos de Veículos: {mediana_roubo_automoveis:.0f}')
plt.text(0.3,0.7,f'Distância entre a média e a mediana dos roubos de veículos: {distancia_roubo_automoveis:.2f}%')
plt.text(0.4,0.6,f'Maior Valor de Roubos de Veículos: {maior_roubo_automoveis:.0f}')
plt.text(0.5,0.5,f'Menor Valor de Roubos de Veículos: {menor_roubo_automoveis:.0f}')
plt.text(0.6,0.4,f'O coeficiente de variação de Roubos de Veículos: {coeficiente_variacao_roubo_automoveis:.2f}%')
plt.text(0.7,0.3,f'A distância da variancia de Roubos de Veículos: {distancia_var_rb_auto:.2f}%')
plt.show()