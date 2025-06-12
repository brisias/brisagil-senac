import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

base_dados = 'UC2/BASESDADOS/dados_sorvete_clima.csv'
df_sorvete = pd.read_csv(base_dados, sep=';', encoding='iso-8859-1')
#df_sorvete['Data'] = pd.to_datetime(df_sorvete['Data'], dayfirst=True)
df_producao = df_sorvete[['Data', 'Producao_Sorvete']]
df_temperatura = df_sorvete[['Data', 'Temperatura_Media']]
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
print()

# Visualização de dados 
sns.set_theme(style='whitegrid')

#paleta de cores
cor_barras = '#837594'
cor_fundo = '#EBE9F3'
cor_grid = '#B6AFBE'
cor_texto = '#443045'
cor_regressao = '#5A3C5C'

fig, axs = plt.subplots(2,2, figsize=(16,10)) #cria uma grade com 4 gráficos (2linhas x 2colunas)
print(type(fig)) #verifica o tipo de objeto criado na variável fig
fig.patch.set_facecolor(cor_fundo) #altera a cor de fundo da área total
plt.suptitle('Análise de Dados - Produção de Sorvete e Temperatura Média (2024)', #título do painel
             fontsize=15,
             color=cor_texto,
             fontweight='bold') 

#posição 1: Gráfico de Barra Top 10 Produção de Sorvete
df_raking_producao = df_producao.sort_values(by='Producao_Sorvete', ascending=False).head(10)
axs[0, 0].barh(df_raking_producao['Data'].astype(str), df_raking_producao['Producao_Sorvete'],
               color=cor_barras, edgecolor='none')
axs[0, 0].set_title('Ranking dos dias com maior Produção de Sorvete (unidades produzidas)',
                    color=cor_texto,
                    fontsize=13,
                    fontweight='bold',
                    pad=15)
axs[0, 0].set_facecolor(cor_fundo)
axs[0, 0].grid(True, color=cor_grid, linestyle='--', linewidth=0.7)
axs[0, 0].tick_params(axis='x', colors=cor_texto)
axs[0, 0].tick_params(axis='y', colors=cor_texto)

#posição 2: Gráfico de Barra Top 10 Temperatura Média
df_raking_temperatura = df_temperatura.sort_values(by='Temperatura_Media', ascending=False).head(10)
axs[0, 1].barh(df_raking_temperatura['Data'].astype(str), df_raking_temperatura['Temperatura_Media'],
               color=cor_barras, edgecolor='none')
axs[0, 1].set_title('Ranking dos dias com maior Temperatura Média (°C)',
                    color=cor_texto,
                    fontsize=13,
                    fontweight='bold',
                    pad=15)
axs[0, 1].set_facecolor(cor_fundo)
axs[0, 1].grid(True, color=cor_grid, linestyle='--', linewidth=0.7)
axs[0, 1].tick_params(axis='x', colors=cor_texto)
axs[0, 1].tick_params(axis='y', colors=cor_texto)

#posição 3: Gráfico de Linha Produção de Sorvete x Temperatura Média
axs[1, 0].scatter(df_producao['Producao_Sorvete'], df_temperatura['Temperatura_Media'],
                  color=cor_barras)
axs[1, 0].set_title('Correlação entre Produção de Sorvete e Temperatura Média', 
                    color=cor_texto,
                    fontsize=13,
                    fontweight='bold',
                    pad=15)
axs[1, 0].set_xlabel('Produção de Sorvete', color=cor_texto)
axs[1, 0].set_ylabel('Temperatura Média (°C)', color=cor_texto)
axs[1, 0].set_facecolor(cor_fundo)
axs[1, 0].grid(True, color=cor_grid, linestyle='--', linewidth=0.7)
axs[1, 0].tick_params(axis='x', colors=cor_texto)
axs[1, 0].tick_params(axis='y', colors=cor_texto)

#posição 4: Gráfico de Linha Regressão Linear Produção de Sorvete x Temperatura Média
sns.regplot(x="Producao_Sorvete", y="Temperatura_Media",
            data=df_producao_temperatura,
            ax=axs[1, 1],
            scatter_kws={"color": cor_barras},
            line_kws={"color": cor_regressao})

axs[1, 1].set_title('Regressão Linear: Produção de Sorvete x Temperatura Média', 
                    color=cor_texto,
                    fontsize=13,
                    fontweight='bold',
                    pad=15)
axs[1, 1].set_xlabel('Produção de Sorvete', color=cor_texto)
axs[1, 1].set_ylabel('Temperatura Média (°C)', color=cor_texto)
axs[1, 1].set_facecolor(cor_fundo)
axs[1, 1].grid(True, color=cor_grid, linestyle='--', linewidth=0.7)
axs[1, 1].tick_params(axis='x', colors=cor_texto)
axs[1, 1].tick_params(axis='y', colors=cor_texto)

plt.tight_layout(rect=[0, 0, 1, 1])
plt.savefig("relatório_produção_sorvete_temperatura-v3.png", format='png', dpi=300)
plt.show()