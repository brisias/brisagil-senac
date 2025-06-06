import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

base_dados = 'BASES_DADOS\dados_sorvete_clima.csv'
df_sorvete = pd.read_csv(base_dados, sep=';', encoding='iso-8859-1')
df_producao_temperatura = df_sorvete[['Data','Producao_Sorvete', 'Temperatura_Media']]

array_producao = np.array(df_producao_temperatura['Producao_Sorvete'])
array_temperatura = np.array(df_producao_temperatura['Temperatura_Media'])

#______Métricas______#

media_producao = np.mean(array_producao)
maior_producao = np.max(array_producao)
menor_producao = np.min(array_producao)
mediana_producao = np.median(array_producao)
distancia_producao = abs((media_producao - mediana_producao) / mediana_producao * 100)
amplitude_producao = maior_producao - menor_producao

media_temperatura = np.mean(array_temperatura)
maior_temperatura = np.max(array_temperatura)
menor_temperatura = np.min(array_temperatura)
mediana_temperatura = np.median(array_temperatura)
distancia_temperatura = abs((media_temperatura - mediana_temperatura) / mediana_temperatura * 100)
amplitude_temperatura = maior_temperatura - menor_temperatura

#______Indentificando os quartis e outliers______#

#produção de sorvete
q1_producao = np.quantile(array_producao, 0.25, method='weibull')
q2_producao = np.quantile(array_producao, 0.50, method='weibull')
q3_producao = np.quantile(array_producao, 0.75, method='weibull')
iqr_producao = q3_producao - q1_producao

limite_superior_producao = q3_producao + (1.5*iqr_producao)
limite_inferior_producao = q1_producao - (1.5*iqr_producao)

df_producao_outliers_inferiores = df_producao_temperatura[df_producao_temperatura['Producao_Sorvete'] < limite_inferior_producao]
df_producao_outliers_superiores = df_producao_temperatura[df_producao_temperatura['Producao_Sorvete'] > limite_superior_producao]

#temperatura média
q1_temperatura = np.quantile(array_temperatura, 0.25, method='weibull')
q2_temperatura = np.quantile(array_temperatura, 0.50, method='weibull')
q3_temperatura = np.quantile(array_temperatura, 0.75, method='weibull')
iqr_temperatura = q3_temperatura - q1_temperatura

limite_superior_temperatura = q3_temperatura + (1.5*iqr_temperatura)
limite_inferior_temperatura = q1_temperatura - (1.5*iqr_temperatura)

df_temperatura_outliers_inferiores = df_producao_temperatura[df_producao_temperatura['Temperatura_Media'] < limite_inferior_temperatura]
df_temperatura_outliers_superiores = df_producao_temperatura[df_producao_temperatura['Temperatura_Media'] > limite_superior_temperatura]

#______Identificando correlações______#
corr_producao_temperatura = np.corrcoef(df_producao_temperatura['Producao_Sorvete'], df_producao_temperatura['Temperatura_Media'])[0,1]


#______Regressão Linear______#
x_temperatura = df_producao_temperatura[['Temperatura_Media']]
y_producao = df_producao_temperatura[['Producao_Sorvete']]

modelo_simples_producao_temperatura = LinearRegression()
modelo_simples_producao_temperatura.fit(x_temperatura, y_producao)

print('\n-------- Métricas --------')
print('\n--- Produção de Sorvete:')
print(f'\nMédia: {media_producao:.2f}')
print(f'\nMaior: {maior_producao:.2f}')
print(f'\nMenor: {menor_producao:.2f}')
print(f'\nMediana: {mediana_producao:.2f}')
print(f'\nDistancia: {distancia_producao:.2f}%')
print(f'\nAmplitude: {amplitude_producao:.2f}')

print('\n--- Temperatura Média:')
print(f'\nMédia: {media_temperatura:.2f}')
print(f'\nMaior: {maior_temperatura:.2f}')
print(f'\nMenor: {menor_temperatura:.2f}')
print(f'\nMediana: {mediana_temperatura:.2f}')
print(f'\nDistancia: {distancia_temperatura:.2f}%')
print(f'\nAmplitude: {amplitude_temperatura:.2f}')

print('\n-------- Identificando outliers --------')
print('\n--- Produção de Sorvete:')
if len(df_producao_outliers_superiores) == 0:    
    print('\nNão existem outliers superiores')
else:
    print('- Outliers Superiores_')
    print(df_producao_outliers_superiores.sort_values(by='Producao_Sorvete', ascending=False).head(10))

if len(df_producao_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n- Outliers Inferiores_')
    print(df_producao_outliers_inferiores)

print('\n--- Temperatura Média:')
if len(df_temperatura_outliers_superiores) == 0:    
    print('\nNão existem outliers superiores')
else:
    print('- Outliers Superiores_')
    print(df_temperatura_outliers_superiores.sort_values(by='Temperatura_Media', ascending=False).head(10))

if len(df_temperatura_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n- Outliers Inferiores_')
    print(df_temperatura_outliers_inferiores)

print('\n-------- Correlação --------')
print(f'Produção de Sorvete x Temperatura Média: {corr_producao_temperatura:0.4f}')

if corr_producao_temperatura >= 0.9:
    print('Correlação positiva muito forte')
elif corr_producao_temperatura >= 0.7 and corr_producao_temperatura < 0.9:
    print('Correlação positiva forte')
elif corr_producao_temperatura >= 0.5 and corr_producao_temperatura < 0.7:
    print('Correlação positiva moderada')
elif corr_producao_temperatura >= 0.3 and corr_producao_temperatura < 0.5:
    print('Correlação positiva fraca')
elif corr_producao_temperatura <= -0.3 and corr_producao_temperatura > -0.5:
    print('Correlação negativa fraca')
elif corr_producao_temperatura <= -0.5 and corr_producao_temperatura > -0.3:
    print('Correlação negativa moderada')
elif corr_producao_temperatura <= -0.7 and corr_producao_temperatura > -0.5:
    print('Correlação negativa forte')
elif corr_producao_temperatura <= -0.9 and corr_producao_temperatura > -0.7:
    print('Correlação negativa muito forte')
else:
    print('Sem correlação')

if corr_producao_temperatura > 0:
    print('Produção de Sorvete aumenta com Temperatura Média')
else:
    print('Produção de Sorvete diminui com Temperatura Média')

print('\n-------- Identificando Regressão Linear --------')
print(f'\nCoeficiente: {modelo_simples_producao_temperatura.coef_[0][0]:.2f}')
print(f'\nIntercepto: {modelo_simples_producao_temperatura.intercept_[0]:.2f}')
print(f'\nR-quadrado: {modelo_simples_producao_temperatura.score(x_temperatura, y_producao):.4f}')

print('\n-------- Visualização de Dados --------')
fig, axs = plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise de Dados - Produção de Sorvete e Temperaturas (janeiro/2024)', fontsize=15)

#Posição 01: Gráfico de Maior produção de sorvete
plt.subplot(2,2,1)
plt.title('Maior Produção de Sorvete')
plt.barh(