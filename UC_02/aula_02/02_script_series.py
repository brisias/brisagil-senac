import pandas as pd 
notas = pd.Series([81,44,92,64,36,70,96,26,84,54])
acima = notas[notas >= 70]
abaixo = notas[notas < 70]
print('\nNotas acima da média:')
print(acima)
print('Notas abaixo da média:')
print(abaixo)