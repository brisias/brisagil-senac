#importando as bibliotecas
import pandas as pd 
import numpy as np 

#importando a base de dados
endereco_dados = '00.BASES\Funcionarios.csv'

#criando o DataFrame Funcionários
df_funcionarios = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

#criando uma array para salário
array_salario = np.array(df_funcionarios['Salário'])

#criando uma array para idade
array_idade = np.array(df_funcionarios['Idade'])

#criando uma array para tempo de empresa
array_tempo = np.array(df_funcionarios['Tempo'])

#obtendo as métricas
media_salario = np.mean(array_salario)
maior_salario = np.max(array_salario)
menor_salario = np.min(array_salario)
nome_salario = df_funcionarios[df_funcionarios['Salário'] == maior_salario]['Nome']

media_idade = np.mean(array_idade)
maior_idade = np.max(array_idade)
menor_idade = np.min(array_idade)
amplitude_idade = maior_idade - menor_idade
nome_velho = df_funcionarios[df_funcionarios['Idade'] == maior_idade]['Nome']
nome_novo = df_funcionarios[df_funcionarios['Idade'] == menor_idade]['Nome']

media_tempo = np.mean(array_tempo)
maior_tempo = np.max(array_tempo)
menor_tempo = np.min(array_tempo)
amplitude_tempo = maior_tempo - menor_tempo
nome_antigo = df_funcionarios[df_funcionarios['Tempo'] == maior_tempo]['Nome']

qtd_func = np.count_nonzero(array_idade)

#exibindo as métricas
print('\n---------- Tabela de Funcionários ----------')
print(df_funcionarios)

print('\n---------- Resultados Solicitados ----------')
print(f'A média salarial dos funcionários é: {media_salario:.2f}')
print(f'{nome_salario.values[0]} é o funcionário com maior salário.')

print(f'\n{nome_velho.values[0]} é o funcionário com mais idade da empresa, com {maior_idade} anos')
print(f'{nome_novo.values[0]} é o funcionário com menos idade da empresa, com {menor_idade} anos')
print(f'A amplitude relativa à idade dos funcionários da  empresa é {amplitude_idade} anos')
print(f'A média de idade dos funcionários é {media_idade:.0f} anos')

print(f'\n{nome_velho.values[0]} é o funcionário com mais tempo de empresa')
print(f'O(a) funcionário(a) com maior tempo de empresa possui {maior_tempo} anos de empresa')
print(f'O(a) funcionário(a) com menor tempo de empresa possui {menor_tempo} anos de empresa')
print(f'A amplitude relativa ao tempo de empresa é {amplitude_tempo}')
print(f'O tempo médio dos funcionários na empresa é {media_tempo:.0f} anos')

print(f'\nA quantidade de funcionários na empresa é {qtd_func}')