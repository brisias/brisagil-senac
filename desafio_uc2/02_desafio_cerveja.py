import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

base_dados = 'UC2/BASESDADOS/consumo_cerveja.csv'

df_cerveja = pd.read_csv(base_dados, sep=',', encoding='iso-8859-1')
#df_cerveja['Data'] = pd.to_datetime(df_cerveja['Data'], dayfirst=True) #transforma a coluna data em formato datetime padrão aaaa-mm-dd

df_consumo = df_cerveja[['data', 'consumo_cerveja']]
df_temperatura = df_cerveja[['data', 'temperatura']]
df_consumo_temperatura = df_cerveja[['data','consumo_cerveja', 'temperatura']]

df_consumo_tempo = df_cerveja[['consumo_cerveja', 'tempo']]
df_consumo_tempo = df_consumo_tempo.groupby('tempo').sum('consumo_cerveja').reset_index()

array_consumo = np.array(df_consumo_temperatura['consumo_cerveja'])
array_temperatura = np.array(df_consumo_temperatura['temperatura'])

#______Identificando quartis e outliers______#

#consumo cerveja
q1_consumo = np.quantile(array_consumo, 0.25, method='weibull')
q2_consumo = np.quantile(array_consumo, 0.50, method='weibull')
q3_consumo = np.quantile(array_consumo, 0.75, method='weibull')
iqr_consumo = q3_consumo - q1_consumo

limite_superior_consumo = q3_consumo + (1.5*iqr_consumo)
limite_inferior_consumo = q1_consumo - (1.5*iqr_consumo)

df_consumo_outliers_inferiores = df_consumo_temperatura[df_consumo_temperatura['consumo_cerveja'] < limite_inferior_consumo]
df_consumo_outliers_superiores = df_consumo_temperatura[df_consumo_temperatura['consumo_cerveja'] > limite_superior_consumo]

#temperatura
q1_temperatura = np.quantile(array_temperatura, 0.25, method='weibull')
q2_temperatura = np.quantile(array_temperatura, 0.50, method='weibull')
q3_temperatura = np.quantile(array_temperatura, 0.75, method='weibull')
iqr_temperatura = q3_temperatura - q1_temperatura

limite_superior_temperatura = q3_temperatura + (1.5*iqr_temperatura)
limite_inferior_temperatura = q1_temperatura - (1.5*iqr_temperatura)

df_temperatura_outliers_inferiores = df_consumo_temperatura[df_consumo_temperatura['temperatura'] < limite_inferior_temperatura]
df_temperatura_outliers_superiores = df_consumo_temperatura[df_consumo_temperatura['temperatura'] > limite_superior_temperatura]

#______Identificando correlações______#

corr_consumo_temperatura = df_consumo_temperatura['consumo_cerveja'].corr(df_consumo_temperatura['temperatura'])
#corr_consumo_tempo = df_consumo_tempo['consumo_cerveja'].corr(df_consumo_tempo['tempo'])

#______Regressão Linear______#

X_temperatura = df_consumo_temperatura[['temperatura']]
y_consumo = df_consumo_temperatura['consumo_cerveja']

modelo_simples_consumo_temperatura = LinearRegression()
modelo_simples_consumo_temperatura.fit(X_temperatura, y_consumo)

print('\n-------- Identificando outliers --------')
print('\n--- Consumo de Cerveja:')
if len(df_consumo_outliers_superiores) == 0:
    print('\nNão existem outliers superiores')
else:
    print('- Outliers Superiores_')
    print(df_consumo_outliers_superiores.sort_values(by='consumo_cerveja', ascending=False).head(10))

if len(df_consumo_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n- Outliers Inferiores_')
    print(df_consumo_outliers_inferiores)

print('\n--- Temperatura:')
if len(df_temperatura_outliers_superiores) == 0:
    print('\nNão existem outliers superiores')
else:
    print('- Outliers Superiores_')
    print(df_temperatura_outliers_superiores.sort_values(by='temperatura', ascending=False).head(10))

if len(df_temperatura_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n- Outliers Inferiores_')
    print(df_temperatura_outliers_inferiores)

print('\n-------- Correlações --------')
print(f'Consumo de Cerveja x Temperatura: {corr_consumo_temperatura:0.4f}')
if corr_consumo_temperatura >= 0.9:
    print('Correlação positiva muito forte')
elif corr_consumo_temperatura >= 0.7 and corr_consumo_temperatura < 0.9:
    print('Correlação positiva forte')
elif corr_consumo_temperatura >= 0.5 and corr_consumo_temperatura < 0.7:
    print('Correlação positiva moderada')
elif corr_consumo_temperatura >= 0.3 and corr_consumo_temperatura < 0.5:
    print('Correlação positiva fraca')
elif corr_consumo_temperatura >= 0.1 and corr_consumo_temperatura < 0.3:
    print('Correlação positiva muito fraca')
elif corr_consumo_temperatura <= -0.1 and corr_consumo_temperatura > -0.3:
    print('Correlação negativa muito fraca')
elif corr_consumo_temperatura <= -0.3 and corr_consumo_temperatura > -0.5:
    print('Correlação negativa fraca')
elif corr_consumo_temperatura <= -0.5 and corr_consumo_temperatura > -0.7:
    print('Correlação negativa moderada')
elif corr_consumo_temperatura <= -0.7 and corr_consumo_temperatura > -0.9:
    print('Correlação negativa forte')
elif corr_consumo_temperatura <= -0.9:
    print('Correlação negativa muito forte')
else:
    print('Sem correlação')

#print(f'Consumo de Cerveja x Tempo: {corr_consumo_tempo:0.4f}')

print('\n-------- Regressão Linear --------')
print(f'Coeficiente: {modelo_simples_consumo_temperatura.coef_[0]:.2f}')
print(f'Intercepto: {modelo_simples_consumo_temperatura.intercept_:.2f}')
print(f'R-quadrado: {modelo_simples_consumo_temperatura.score(X_temperatura, y_consumo):.4f}')

# Visualização de dados 
sns.set_theme(style='whitegrid')

#paleta de cores
cor_barras = '#837594'
cor_fundo = '#EBE9F3'
cor_grid = '#B6AFBE'
cor_texto = '#443045'
cor_linhas = '#5A3C5C'

fig, axs = plt.subplots(3,2, figsize=(16,20))
fig.patch.set_facecolor(cor_fundo)
plt.suptitle('Análise de Dados - Temperaturas e Consumo de Cervejas (1º semestre - 2023)',
             fontsize=15,
             color=cor_texto,
             fontweight='bold')

#posição 1: série histórica temperaturas
axs[0,0].plot(df_temperatura['data'], df_temperatura['temperatura'], color=cor_linhas)
axs[0,0].set_title('Temperatura Média Diária (°C)', color=cor_texto)
axs[0,0].set_xlabel('Data')
axs[0,0].set_ylabel('Temperatura (°C)')
axs[0,0].tick_params(axis='x', rotation=45)
axs[0,0].grid(color=cor_grid, linestyle='--', linewidth=0.7)

#posição 2: série histórica consumo cerveja
axs[0,1].plot(df_consumo['data'], df_consumo['consumo_cerveja'], color=cor_linhas)
axs[0,1].set_title('Consumo Diário de Cerveja', color=cor_texto)
axs[0,1].set_xlabel('Data')
axs[0,1].set_ylabel('Consumo de cerveja (unidades)')
axs[0,1].tick_params(axis='x', rotation=45)
axs[0,1].grid(color=cor_grid, linestyle='--', linewidth=0.7)

# posição 3: correlação temperatura x consumo
axs[1, 0].scatter(df_consumo['consumo_cerveja'], df_temperatura['temperatura'],
                  color=cor_barras)
axs[1, 0].set_title('Correlação entre Consumo de cerveja e Temperatura Média', 
                    color=cor_texto,
                    fontsize=13,
                    fontweight='bold',
                    pad=15)
axs[1, 0].set_xlabel('Consumo de cerveja (unidades)', color=cor_texto)
axs[1, 0].set_ylabel('Temperatura Média (°C)', color=cor_texto)
axs[1, 0].set_facecolor(cor_fundo)
axs[1, 0].grid(True, color=cor_grid, linestyle='--', linewidth=0.7)
axs[1, 0].tick_params(axis='x', colors=cor_texto)
axs[1, 0].tick_params(axis='y', colors=cor_texto)

# posição 4: regressão linear
sns.regplot(x="temperatura", y="consumo_cerveja",
            data=df_consumo_temperatura,
            ax=axs[1, 1],
            scatter_kws={"color": cor_barras},
            line_kws={"color": cor_linhas})

axs[1, 1].set_title('Regressão Linear: Consumo de cervejas x Temperatura Média', 
                    color=cor_texto,
                    fontsize=13,
                    fontweight='bold',
                    pad=15)
axs[1, 1].set_xlabel('Consumo de cerveja (unidades)', color=cor_texto)
axs[1, 1].set_ylabel('Temperatura Média (°C)', color=cor_texto)
axs[1, 1].set_facecolor(cor_fundo)
axs[1, 1].grid(True, color=cor_grid, linestyle='--', linewidth=0.7)
axs[1, 1].tick_params(axis='x', colors=cor_texto)
axs[1, 1].tick_params(axis='y', colors=cor_texto)

# posição 5: tempo x consumo
sns.barplot(x='tempo', y='consumo_cerveja', data=df_consumo_tempo, ax=axs[1,1], palette='pastel')
axs[2,0].set_title('Consumo por Tipo de Clima', color=cor_texto)
axs[2,0].set_xlabel('Condição Climática')
axs[2,0].set_ylabel('Consumo Total (litros)')
axs[2,0].tick_params(axis='x', rotation=45)
axs[2,0].grid(color=cor_grid, linestyle='--', linewidth=0.5)

# posição 6: tabela medidas descritivas
tabela_descritiva = df_consumo_temperatura[['temperatura', 'consumo_cerveja']].describe().round(2)
axs[2,1].axis('off')
table = axs[2,1].table(cellText=tabela_descritiva.values,
                       rowLabels=tabela_descritiva.index,
                       colLabels=tabela_descritiva.columns,
                       cellLoc='center',
                       loc='center')
table.scale(1, 2)
table.auto_set_font_size(False)
table.set_fontsize(10)
axs[2,1].set_title('Resumo Estatístico', color=cor_texto, pad=10)

plt.tight_layout(rect=[0, 0.03, 1, 1])

plt.show()