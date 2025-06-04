import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados, sep=';',encoding='iso-8859-1')

df_hom_doloso = df_ocorrencias[['cisp','ano','hom_doloso']]
df_hom_doloso = df_hom_doloso[df_hom_doloso['ano'].between(2003,2024)]
df_hom_doloso = df_hom_doloso.groupby(['cisp']).sum(['hom_doloso']).reset_index()

df_hom_culposo = df_ocorrencias[['cisp','ano','hom_culposo']]
df_hom_culposo = df_hom_culposo[df_hom_culposo['ano'].between(2003,2024)]
df_hom_culposo = df_hom_culposo.groupby(['cisp']).sum(['hom_culposo']).reset_index()

array_hom_doloso = np.array(df_hom_doloso['hom_doloso'])
array_hom_culposo = np.array(df_hom_culposo['hom_culposo'])

#______Indentificando os quartis e outliers______#

#homicídios dolosos
q1_hom_doloso = np.quantile(array_hom_doloso, 0.25, method='weibull')
q2_hom_doloso = np.quantile(array_hom_doloso, 0.50, method='weibull')
q3_hom_doloso = np.quantile(array_hom_doloso, 0.75, method='weibull')
iqr_hom_doloso = q3_hom_doloso - q1_hom_doloso

limite_superior_hom_doloso = q3_hom_doloso + (1.5*iqr_hom_doloso)
limite_inferior_hom_doloso = q1_hom_doloso - (1.5*iqr_hom_doloso)

df_hom_doloso_outliers_superiores = df_hom_doloso[df_hom_doloso['hom_doloso'] > limite_superior_hom_doloso]
df_hom_doloso_outliers_inferiores = df_hom_doloso[df_hom_doloso['hom_doloso'] < limite_inferior_hom_doloso]

#homicídios culposos
q1_hom_culposo = np.quantile(array_hom_culposo, 0.25, method='weibull')
q2_hom_culposo = np.quantile(array_hom_culposo, 0.50, method='weibull')
q3_hom_culposo = np.quantile(array_hom_culposo, 0.75, method='weibull')
iqr_hom_culposo = q3_hom_culposo - q1_hom_culposo

limite_superior_hom_culposo = q3_hom_culposo + (1.5*iqr_hom_culposo)
limite_inferior_hom_culposo = q1_hom_culposo - (1.5*iqr_hom_culposo)

df_hom_culposo_outliers_superiores = df_hom_culposo[df_hom_culposo['hom_culposo'] > limite_superior_hom_culposo]
df_hom_culposo_outliers_inferiores = df_hom_culposo[df_hom_culposo['hom_culposo'] < limite_inferior_hom_culposo]

#______Identificando correlações______#

df_hom_doloso_culposo = df_ocorrencias[['cisp','ano','hom_doloso','hom_culposo']]
df_hom_doloso_culposo = df_hom_doloso_culposo[df_hom_doloso_culposo['ano'].between(2003,2024)]
df_hom_doloso_culposo = df_hom_doloso_culposo.groupby(['cisp']).sum(['hom_doloso','hom_culposo']).reset_index()

corr_hom_doloso_culposo = np.corrcoef(df_hom_doloso_culposo['hom_doloso'], df_hom_doloso_culposo['hom_culposo'])[0,1]

#______Regressão Linear______#

x_hom_doloso = df_hom_doloso_culposo[['hom_doloso']]
y_hom_culposo = df_hom_doloso_culposo[['hom_culposo']]

modelo_simples_hom_doloso_culposo = LinearRegression()
modelo_simples_hom_doloso_culposo.fit(x_hom_doloso, y_hom_culposo)

print('\n---------- 10 delegacias com mais registros de homicídios dolosos ----------')
print('')
print(df_hom_doloso.drop(columns=['ano']).sort_values(by='hom_doloso', ascending=False).head(10))
print('\n---------- 10 delegacias com mais registros de homicídios culposos ----------')
print('')
print(df_hom_culposo.drop(columns=['ano']).sort_values(by='hom_culposo', ascending=False).head(10))

print('---------- Identificando outliers ----------')
print('\n--- Homicídios Dolosos:')
if len(df_hom_doloso_outliers_superiores) == 0:    
    print('\nNão existem outliers superiores')
else:
    print('_Outliers Superiores_')
    print(df_hom_doloso_outliers_superiores.drop(columns=['ano']).sort_values(by='hom_doloso', ascending=False).head(10))

if len(df_hom_doloso_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n_Outliers Inferiores_')
    print(df_hom_doloso_outliers_inferiores)

print('\n--- Homicídios Culposos:')
if len(df_hom_culposo_outliers_superiores) == 0:
    print('\nNão existem outliers superiores')
else:
    print('_Outliers Superiores_')
    print(df_hom_culposo_outliers_superiores.drop(columns=['ano']).sort_values(by='hom_culposo', ascending=False).head(10))

if len(df_hom_culposo_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n_Outliers Inferiores_')
    print(df_hom_culposo_outliers_inferiores)

# Correlações
# 0.9 a 1.0 (positiva ou negativa) = Muito forte correlação
# 0.7 a 0.9 (positiva ou negativa) = Forte correlação
# 0.5 a 0.7 (positiva ou negativa) = Moderada correlação
# 0.3 a 0.5 (positiva ou negativa) = Fraca correlação
# 0.0 a 0.3 (positiva ou negativa) = Sem correlação

print(f'\n-------- Correlação -------')
print(f'Homicídios Dolosos x Homicídio Culposos: {corr_hom_doloso_culposo:.3f}') #forte correlação

if corr_hom_doloso_culposo >= 0.9:
    print('Correlação positiva muito forte')
elif corr_hom_doloso_culposo >= 0.7 and corr_hom_doloso_culposo < 0.9:
    print('Correlação positiva forte')
elif corr_hom_doloso_culposo >= 0.5 and corr_hom_doloso_culposo < 0.7:
    print('Correlação positiva moderada')
elif corr_hom_doloso_culposo >= 0.3 and corr_hom_doloso_culposo < 0.5:
    print('Correlação positiva fraca')
elif corr_hom_doloso_culposo <= -0.3 and corr_hom_doloso_culposo > 0.5:
    print('Correlação negativa fraca')
elif corr_hom_doloso_culposo <= -0.5 and corr_hom_doloso_culposo > -0.3:
    print('Correlação negativa moderada')
elif corr_hom_doloso_culposo <= -0.7 and corr_hom_doloso_culposo > -0.5:
    print('Correlação negativa forte')
elif corr_hom_doloso_culposo <= -0.9 and corr_hom_doloso_culposo > -0.7:
    print('Correlação negativa muito forte')
else:
    print('Sem correlação')

if corr_hom_doloso_culposo > 0:
    print('Homicídio Doloso aumenta com o Homicídio Culposo')
else:
    print('Homicídio Doloso diminui com o Homicídio Culposo')

print(f'\n-------- Regressão Linear Simples -------')
print(f'Coeficiente angular: {modelo_simples_hom_doloso_culposo.coef_[0][0]:.2f}')
print(f'Intercepto: {modelo_simples_hom_doloso_culposo.intercept_[0]:.2f}')
print(f'R2: {modelo_simples_hom_doloso_culposo.score(x_hom_doloso, y_hom_culposo):.3f}')

print('\n-------- Visualização os Dados --------')
fig, axs = plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise de Dados sobre Homicídios Dolosos e Culposos (2003-2024)', fontsize=15)

plt.subplot(2,2,1)
plt.title('Boxplot dos Homicídio Dolosos', fontsize=13)
plt.boxplot(array_hom_doloso,vert=False,showmeans=True)

plt.subplot(2,2,2)
plt.title('Histograma dos Homicídio Dolosos', fontsize=13)
plt.hist(array_hom_doloso,bins=100,edgecolor='black')

df_hom_doloso_outliers_superiores_order = df_hom_doloso_outliers_superiores.sort_values(by='hom_doloso', ascending=True)
plt.subplot(2,2,3)
plt.title('Outliers dos Homicídio Dolosos', fontsize=13)
plt.barh(df_hom_doloso_outliers_superiores_order['cisp'].astype(str),df_hom_doloso_outliers_superiores_order['hom_doloso'])

plt.subplot(2,2,4)
plt.title('Boxplot dos Homicídio Culposos', fontsize=13)

