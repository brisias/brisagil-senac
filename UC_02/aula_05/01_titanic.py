#importando as bibliotecas
import pandas as pd 
import numpy as np 

#funções_formatação

#importando a base de dados
endereco_dados = '00.BASES\Titanic.csv'

#criando o DataFrame Funcionários
df_titanic = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_titanic = df_titanic[['Name','Sex','Age','Survived','Pclass','Fare']]

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

#métricas_condição econômica
media_tarifa = np.mean(array_tarifa)
maior_tarifa = np.max(array_tarifa)
menor_tarifa = np.min(array_tarifa)
mediana_tarifa = np.median(array_tarifa)
distancia_tarifa = abs((media_tarifa - mediana_tarifa) / mediana_tarifa * 100)

pclass_maior_tarifa = df_titanic[df_titanic['Fare'] == maior_tarifa]['Pclass']
pclass_menor_tarifa = df_titanic[df_titanic['Fare'] == menor_tarifa]['Pclass']
pclass_mediana_tarifa = df_titanic[df_titanic['Fare'] == mediana_tarifa]['Pclass']

qtd_primeira_classe = df_titanic[df_titanic['Pclass'] == 1].count()
qtd_segunda_classe = df_titanic[df_titanic['Pclass'] == 2].count()
qtd_terceira_classe = df_titanic[df_titanic['Pclass'] == 3].count()

#métricas sobreviventes
qtd_passageiros = df_titanic['Survived'].count()
qtd_sobreviventes = df_titanic[df_titanic['Survived'] == 1].count()
percentual_sobreviventes = (qtd_sobreviventes / qtd_passageiros) * 100
df_titanic_survived = df_titanic[df_titanic['Survived'] == 1]


#exibindo as métricas
print('\n---------- Recorte da Base de Dados ----------')
print(df_titanic)

print('\n---------- Faixa etária ----------')
print(f'maior idade: {maior_idade} anos')
print(f'menor idade: {menor_idade} anos')
print(f'média: {media_idade:.0f}')
print(f'mediana: {mediana_idade:.0f}')
print(f'distância: {distancia_idade:.2f}%')

print('\n---------- Condição econômica ----------')
print(f'maior tarifa: $ {maior_tarifa:.2f}')
print(f'menor tarifa: $ {menor_tarifa:.2f}')
print(f'média: $ {media_tarifa:.2f}')
print(f'mediana: $ {mediana_tarifa:.2f}')
print(f'distância: {distancia_tarifa:.2f}%')

print(f'\nprimeira classe: {qtd_primeira_classe.values[0]} passageiros')
print(f'segunda classe: {qtd_segunda_classe.values[0]} passageiros')
print(f'terceira classe: {qtd_terceira_classe.values[0]} passageiros')
print(f'classe maior tarifa: {pclass_maior_tarifa.values[0]}')
print(f'classe menor tarifa: {pclass_menor_tarifa.values[0]}')
print(f'classe tarifa mediana: {pclass_mediana_tarifa}')

print('\n---------- Sobreviventes ----------')
print(f'total: {qtd_passageiros} passageiros')
print(f'sobreviventes: {qtd_sobreviventes.values[0]} passageiros')
print(f'percentual sobreviventes: ')

print(f'_dataframe sobreviventes_\n{df_titanic_survived}')

print('\n---------- Sexo ----------')

print('\n---------- Conclusões ----------')



