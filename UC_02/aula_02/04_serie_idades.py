import pandas as pd
idades = pd.Series([23,37,3,8,45,13,94,72,62,56])
maiores = idades[idades >= 18]
menores = idades[idades < 18]
print('Participantes com idade abaixo de 18 anos:')
print(menores.to_string(index=False)) # comando para remover a coluna de índices (que representam a posição dos elementos na lista) na exibição final;
print('\nParticipantes com idade maior ou igual a 18 anos:')
print(maiores.to_string(index=False))