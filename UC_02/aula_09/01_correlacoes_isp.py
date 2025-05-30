import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados, sep=';',encoding='iso-8859-1')

df_roubo_veiculo = df_ocorrencias[['roubo_veiculo', 'cisp']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['cisp']).sum(['roubo_veiculo']).reset_index()

df_furto_veiculo = df_ocorrencias[['furto_veiculos', 'cisp']]
df_furto_veiculo = df_furto_veiculo.groupby(['cisp']).sum(['furto_veiculos']).reset_index()

df_recuperacao_veiculo = df_ocorrencias[['recuperacao_veiculos', 'cisp']]
df_recuperacao_veiculo = df_recuperacao_veiculo.groupby(['cisp']).sum(['recuperacao_veiculos']).reset_index()

array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
array_furto_veiculo = np.array(df_furto_veiculo['furto_veiculos'])
array_recuperacao_veiculo = np.array(df_recuperacao_veiculo['recuperacao_veiculos'])

#Indentificando os quartis e outliers
q1_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
q2_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.50, method='weibull')
q3_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.75, method='weibull')
iqr_roubo_veiculo = q3_roubo_veiculo - q1_roubo_veiculo

limite_superior_roubo_veiculo = q3_roubo_veiculo + (1.5*iqr_roubo_veiculo)
limite_inferior_roubo_veiculo = q1_roubo_veiculo - (1.5*iqr_roubo_veiculo)

df_roubo_veiculo_outliers_sup = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior_roubo_veiculo]
df_roubo_veiculo_outliers_inf = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior_roubo_veiculo]

q1_furto_veiculo = np.quantile(array_furto_veiculo, 0.25, method='weibull')
q2_furto_veiculo = np.quantile(array_furto_veiculo, 0.50, method='weibull')
q3_furto_veiculo = np.quantile(array_furto_veiculo, 0.75, method='weibull')
iqr_furto_veiculo = q3_furto_veiculo - q1_furto_veiculo

limite_superior_furto_veiculo = q3_furto_veiculo + (1.5*iqr_furto_veiculo)
limite_inferior_furto_veiculo = q1_furto_veiculo - (1.5*iqr_furto_veiculo)

df_furto_veiculo_outliers_sup = df_furto_veiculo[df_furto_veiculo['furto_veiculos'] > limite_superior_furto_veiculo]
df_furto_veiculo_outliers_inf = df_furto_veiculo[df_furto_veiculo['furto_veiculos'] < limite_inferior_furto_veiculo]

q1_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo, 0.25, method='weibull')
q2_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo, 0.50, method='weibull')
q3_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo, 0.75, method='weibull')
iqr_recuperacao_veiculo = q3_recuperacao_veiculo - q1_recuperacao_veiculo

limite_superior_recuperacao_veiculo = q3_recuperacao_veiculo + (1.5*iqr_recuperacao_veiculo)
limite_inferior_recuperacao_veiculo = q1_recuperacao_veiculo - (1.5*iqr_recuperacao_veiculo)

df_recuperacao_veiculo_outliers_sup = df_recuperacao_veiculo[df_recuperacao_veiculo['recuperacao_veiculos'] > limite_superior_recuperacao_veiculo]
df_recuperacao_veiculo_outliers_inf = df_recuperacao_veiculo[df_recuperacao_veiculo['recuperacao_veiculos'] < limite_inferior_recuperacao_veiculo]

#DataFrames das correlações
df_roubo_furto_veiculo = df_ocorrencias[['roubo_veiculo','furto_veiculos','cisp']]
df_roubo_furto_veiculo = df_roubo_furto_veiculo.groupby(['cisp']).sum(['roubo_veiculo','furto_veiculos']).reset_index()

df_furto_recuperacao_veiculo = df_ocorrencias[['furto_veiculos','recuperacao_veiculos','cisp']]
df_furto_recuperacao_veiculo = df_furto_recuperacao_veiculo.groupby(['cisp']).sum(['furto_veiculos','recuperacao_veiculos']).reset_index()

df_roubo_recuperacao_veiculo = df_ocorrencias[['roubo_veiculo','recuperacao_veiculos','cisp']]
df_roubo_recuperacao_veiculo = df_roubo_recuperacao_veiculo.groupby(['cisp']).sum(['roubo_veiculo','recuperacao_veiculos']).reset_index()

#Cálculo das correlações
corr_roubo_furto_veiculo = np.corrcoef(df_roubo_furto_veiculo['roubo_veiculo'], df_roubo_furto_veiculo['furto_veiculos'])[0,1]
corr_furto_recuperacao_veiculo = np.corrcoef(df_furto_recuperacao_veiculo['furto_veiculos'], df_furto_recuperacao_veiculo['recuperacao_veiculos'])[0,1]
corr_roubo_recuperacao_veiculo = np.corrcoef(df_roubo_recuperacao_veiculo['roubo_veiculo'], df_roubo_recuperacao_veiculo['recuperacao_veiculos'])[0,1]

print(f'-------- Identificando Outliers -------')
print('\n--- Roubos de Veículos:')
if len(df_roubo_veiculo_outliers_sup) == 0:    
    print('\nNão existem outliers superiores')
else:
    print('- Outliers Superiores_')
    print(df_roubo_veiculo_outliers_sup.sort_values(by='roubo_veiculo', ascending=False).head(10))

if len(df_roubo_veiculo_outliers_inf) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n- Outliers Inferiores_')
    print(df_roubo_veiculo_outliers_inf)

print('\n--- Furto de Veículos:')
if len(df_furto_veiculo_outliers_sup) == 0:    
    print('\nNão existem outliers superiores')
else:
    print('- Outliers Superiores_')
    print(df_furto_veiculo_outliers_sup.sort_values(by='furto_veiculos', ascending=False).head(10))

if len(df_furto_veiculo_outliers_inf) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n- Outliers Inferiores_')
    print(df_furto_veiculo_outliers_inf)

print('\n--- Recuperação de Veículos:')
if len(df_recuperacao_veiculo_outliers_sup) == 0:    
    print('\nNão existem outliers superiores')
else:
    print('- Outliers Superiores_')
    print(df_recuperacao_veiculo_outliers_sup.sort_values(by='recuperacao_veiculos', ascending=False).head(10))

if len(df_recuperacao_veiculo_outliers_inf) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n- Outliers Inferiores_')
    print(df_recuperacao_veiculo_outliers_inf)

print(f'\n-------- Correlações -------')
print(f'Correlação entre roubo e furto de veículos: {corr_roubo_furto_veiculo:.3f}')
print(f'Correlação entre furto e recuperação de veículos: {corr_furto_recuperacao_veiculo:.3f}')
print(f'Correlação entre roubo e recuperação de veículos: {corr_roubo_recuperacao_veiculo:.3f}')

print('\n-------- Visualização dos Dados -------')
plt.subplots(2,3,figsize=(18,7))
plt.suptitle('Análise dos Dados - Roubos, Furtos e Recuperações de Veículos (2003-2025)', fontsize=15)

df_roubo_veiculo_outliers_sup_order = df_roubo_veiculo_outliers_sup.sort_values(by='roubo_veiculo', ascending=True)
plt.subplot(2,3,1)
plt.title('Outliers dos Roubos de Veículos', fontsize=13)
plt.barh(df_roubo_veiculo_outliers_sup_order['cisp'].astype(str),df_roubo_veiculo_outliers_sup_order['roubo_veiculo'])

df_furto_veiculo_outliers_sup_order = df_furto_veiculo_outliers_sup.sort_values(by='furto_veiculos', ascending=True)
plt.subplot(2,3,2)
plt.title('Outliers dos Furto de Veículos', fontsize=13)
plt.barh(df_furto_veiculo_outliers_sup_order['cisp'].astype(str),df_furto_veiculo_outliers_sup_order['furto_veiculos'])

df_recuperacao_veiculo_outliers_sup_order = df_recuperacao_veiculo_outliers_sup.sort_values(by='recuperacao_veiculos', ascending=True)
plt.subplot(2,3,3)
plt.title('Outliers da Recuperação de Veículos', fontsize=13)
plt.barh(df_recuperacao_veiculo_outliers_sup_order['cisp'].astype(str),df_recuperacao_veiculo_outliers_sup_order['recuperacao_veiculos'])

plt.subplot(2,3,4)
plt.title('Correlação entre Roubo e Furto de Veículos', fontsize=13)
plt.scatter(df_roubo_furto_veiculo['roubo_veiculo'], df_roubo_furto_veiculo['furto_veiculos'])
plt.xlabel('Roubos de Veículos')
plt.ylabel('Furtos de Veículos')

plt.subplot(2,3,5)
plt.title('Correlação entre Furto e Recuperação de Veículos', fontsize=13)
plt.scatter(df_furto_recuperacao_veiculo['furto_veiculos'], df_furto_recuperacao_veiculo['recuperacao_veiculos'])
plt.xlabel('Furtos de Veículos')
plt.ylabel('Recuperação de Veículos')

plt.subplot(2,3,6)
plt.title('Correlação entre Roubo e Recuperação de Veículos', fontsize=13)
plt.scatter(df_roubo_recuperacao_veiculo['roubo_veiculo'], df_roubo_recuperacao_veiculo['recuperacao_veiculos'])
plt.xlabel('Roubos de Veículos')
plt.ylabel('Recuperação de Veículos')

plt.show()