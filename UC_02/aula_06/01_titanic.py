#importando as bibliotecas
import pandas as pd 
import numpy as np 

#importando a base de dados
endereco_dados = '00.BASES\Titanic.csv'

#criando o DataFrame Funcionários
df_titanic = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_titanic = df_titanic[['Name','Age','Sex','Fare','Survived','Pclass']]

#criando arrays
array_idade = np.array(df_titanic['Age'])
array_tarifa = np.array(df_titanic['Fare'])
array_survived = np.array(df_titanic['Survived'])

array_categoria = np.array(df_titanic['Pclass'])
array_sexo = np.array(df_titanic['Sex'])

#métricas_idades
media_idade = np.mean(array_idade)
maior_idade = np.max(array_idade)
menor_idade = np.min(array_idade)
mediana_idade = np.median(array_idade)
distancia_idade = abs((media_idade - mediana_idade) / mediana_idade * 100)
amplitude_idade = maior_idade - menor_idade

#obtendo os quartis da idade
q1_idade = np.quantile(array_idade, 0.25, method='weibull')
q2_idade = np.quantile(array_idade, 0.50, method='weibull')
q3_idade = np.quantile(array_idade, 0.75, method='weibull')
iqr_idade = q3_idade - q1_idade

#identificando e filtrando o DataFrame dos valores discrepantes (outliers): idade
limite_superior_idade = q3_idade + (1.5*iqr_idade)
limite_inferior_idade = q1_idade - (1.5*iqr_idade)

df_idade_outliers_superiores = df_titanic[df_titanic['Age'] > limite_superior_idade]
df_idade_outliers_inferiores = df_titanic[df_titanic['Age'] < limite_inferior_idade]

#métricas_condição econômica
media_tarifa = np.mean(array_tarifa)
maior_tarifa = np.max(array_tarifa)
menor_tarifa = np.min(array_tarifa)
mediana_tarifa = np.median(array_tarifa)
distancia_tarifa = abs((media_tarifa - mediana_tarifa) / mediana_tarifa * 100)
amplitude_tarifa = maior_tarifa - menor_tarifa

pclass_maior_tarifa = df_titanic[df_titanic['Fare'] == maior_tarifa]['Pclass']
pclass_menor_tarifa = df_titanic[df_titanic['Fare'] == menor_tarifa]['Pclass']

qtd_primeira_classe = df_titanic[df_titanic['Pclass'] == 1].count()
qtd_segunda_classe = df_titanic[df_titanic['Pclass'] == 2].count()
qtd_terceira_classe = df_titanic[df_titanic['Pclass'] == 3].count()

#obtendo os quartis da tarifa
q1_tarifa = np.quantile(array_tarifa, 0.25, method='weibull')
q2_tarifa = np.quantile(array_tarifa, 0.50, method='weibull')
q3_tarifa = np.quantile(array_tarifa, 0.75, method='weibull')
iqr_tarifa = q3_tarifa - q1_tarifa

#identificando e filtrando o DataFrame dos valores discrepantes (outliers): tarifa
limite_superior_tarifa = q3_tarifa + (1.5*iqr_tarifa)
limite_inferior_tarifa = q1_tarifa - (1.5*iqr_tarifa)

df_tarifa_outliers_superiores = df_titanic[df_titanic['Fare'] > limite_superior_tarifa]
df_tarifa_outliers_inferiores = df_titanic[df_titanic['Fare'] < limite_inferior_tarifa]

#métricas sobreviventes
qtd_passageiros = df_titanic['Survived'].count()
qtd_sobreviventes = df_titanic[df_titanic['Survived'] == 1].count()
percentual_sobreviventes = (qtd_sobreviventes / qtd_passageiros) * 100
df_titanic_survived = df_titanic[df_titanic['Survived'] == 1]

#métricas sexo
qtd_masc = df_titanic[df_titanic['Sex']=='male'].count()
qtd_fem = df_titanic[df_titanic['Sex']=='female'].count()

qtd_masc_survived = df_titanic_survived[df_titanic_survived['Sex']=='male'].count()
qtd_fem_survived = df_titanic_survived[df_titanic_survived['Sex']=='female'].count()

#exibindo as métricas
print('\n---------- Recorte da Base de Dados ----------')
print(df_titanic)

print('\n---------- Faixa etária ----------')
print(f'maior idade: {maior_idade} anos')
print(f'menor idade: {menor_idade} anos')
print(f'média: {media_idade:.0f}')
print(f'mediana: {mediana_idade:.0f}')
print(f'distância: {distancia_idade:.2f}%')
print(f'amplitude: {amplitude_idade}')
print(f'1º quartil(25%): {q1_idade}')
print(f'2º quartil(50%): {q2_idade}')
print(f'3º quartil(75%): {q3_idade}')
print(f'iqr: {iqr_idade}')
print(f'limite inferior: {limite_inferior_idade}')
print(f'limite superior:{limite_superior_idade}')
if len(df_idade_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n------------ Outliers Inferiores ------------')
    print(df_idade_outliers_inferiores)
if len(df_idade_outliers_superiores) == 0:
    print('\nNão existem outliers superiores')
else:
    print('\n------------ Outliers Superiores ------------')
    print(df_idade_outliers_superiores)

print('\n---------- Condição econômica ----------')
print(f'maior tarifa: $ {maior_tarifa:.2f}')
print(f'menor tarifa: $ {menor_tarifa:.2f}')
print(f'média: $ {media_tarifa:.2f}')
print(f'mediana: $ {mediana_tarifa:.2f}')
print(f'distância: {distancia_tarifa:.2f}%')
print(f'amplitude: $ {amplitude_tarifa:.2f}')
print(f'1º quartil(25%): {q1_tarifa}')
print(f'2º quartil(50%): {q2_tarifa}')
print(f'3º quartil(75%): {q3_tarifa}')
print(f'iqr: {iqr_tarifa}')
print(f'limite inferior: {limite_inferior_tarifa}')
print(f'limite superior:{limite_superior_tarifa}')
if len(df_tarifa_outliers_inferiores) == 0:
    print('\nNão existem outliers inferiores')
else:
    print('\n------------ Outliers Inferiores ------------')
    print(df_tarifa_outliers_inferiores)
if len(df_tarifa_outliers_superiores) == 0:
    print('\nNão existem outliers superiores')
else:
    print('\n------------ Outliers Superiores ------------')
    print(df_tarifa_outliers_superiores)

print(f'\nprimeira classe: {qtd_primeira_classe.values[0]} passageiros')
print(f'segunda classe: {qtd_segunda_classe.values[0]} passageiros')
print(f'terceira classe: {qtd_terceira_classe.values[0]} passageiros')
print(f'classe maior tarifa: {pclass_maior_tarifa.values[0]}')
print(f'classe menor tarifa: {pclass_menor_tarifa.values[0]}')

print('\n---------- Sexo ----------')
print(f'homens: {qtd_masc.values[0]}')
print(f'mulheres: {qtd_fem.values[0]}')

print('\n---------- Sobreviventes ----------')
print(f'total: {qtd_passageiros} passageiros')
print(f'sobreviventes: {qtd_sobreviventes.values[0]} passageiros')
print(f'percentual sobreviventes: {percentual_sobreviventes.values[0]:.2f}%')
print(f'homens: {qtd_masc_survived.values[0]} passageiros')
print(f'mulheres: {qtd_fem_survived.values[0]} passageiras')

print(f'\n---------- DataFrame sobreviventes ----------\n{df_titanic_survived}')

print('\n---------- Conclusões ----------')



