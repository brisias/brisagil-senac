import pandas as pd
import numpy as np

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
df_hom_doloso = df_ocorrencias[['ano','hom_doloso']]
#df_hom_doloso = df_hom_doloso[df_hom_doloso['ano'].between(2003,2024)]
#filtrando os anos de 2003 a 2024; outra opção seria usar o isin para filtrar o recorte desejado, ideal para quando os dados forem strings.
df_hom_doloso = df_hom_doloso.groupby(['ano']).sum(['hom_doloso']).reset_index()
df_hom_doloso.drop(22,axis=0,inplace=True) #eliminando o ano 2025. axis=0 elimina linhas; axis=1 elimina colunas.

array_hom_doloso = np.array(df_hom_doloso['hom_doloso'])

media_hom_doloso = np.mean(array_hom_doloso)
mediana_hom_doloso = np.median(array_hom_doloso)
max_hom_doloso = np.max(array_hom_doloso)
min_hom_doloso = np.min(array_hom_doloso)
distancia_hom_doloso = abs((media_hom_doloso - mediana_hom_doloso) / mediana_hom_doloso * 100)
amplitude_hom_doloso = max_hom_doloso - min_hom_doloso

q1_hom_doloso = np.quantile(array_hom_doloso, 0.25, method='weibull')
q2_hom_doloso = np.quantile(array_hom_doloso, 0.50, method='weibull')
q3_hom_doloso = np.quantile(array_hom_doloso, 0.75, method='weibull')
iqr_hom_doloso = q3_hom_doloso - q1_hom_doloso

limite_superior_hom_doloso = q3_hom_doloso + (1.5*iqr_hom_doloso)
limite_inferior_hom_doloso = q1_hom_doloso - (1.5*iqr_hom_doloso)

df_hom_doloso_outliers_superiores = df_hom_doloso[df_hom_doloso['hom_doloso'] > limite_superior_hom_doloso]
df_hom_doloso_outliers_inferiores = df_hom_doloso[df_hom_doloso['hom_doloso'] < limite_inferior_hom_doloso]

print(f'\n---------- DataFrame Homicídios Dolosos ----------')
print(df_hom_doloso)

print('\n---------- Métricas Homicídios Dolosos ----------')
print(f'média: {media_hom_doloso:.2f}')
print(f'mediana: {mediana_hom_doloso:.0f}')
print(f'distância: {distancia_hom_doloso:.2f}%')
print(f'menor: {min_hom_doloso} ocorrências')
print(f'maior: {max_hom_doloso} ocorrências')
print(f'amplitude: {amplitude_hom_doloso}')
print(f'\n1º quartil(25%): {q1_hom_doloso}')
print(f'2º quartil(50%): {q2_hom_doloso}')
print(f'3º quartil(75%): {q3_hom_doloso}')
print(f'iqr: {iqr_hom_doloso}')

print(f'\nlimite inferior: {limite_inferior_hom_doloso}')
print(f'limite superior:{limite_superior_hom_doloso}')

if len(df_hom_doloso_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n------------ Outliers Inferiores ------------')
    print(df_hom_doloso_outliers_inferiores)
if len(df_hom_doloso_outliers_superiores) == 0:
    print('\nNão existem outliers superiores')
else:
    print('\n------------ Outliers Superiores ------------')
    print(df_hom_doloso_outliers_superiores)