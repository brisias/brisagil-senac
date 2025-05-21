import pandas as pd
import numpy as np

endereco_dados = '00.BASES\enem_2014_2023.csv'
df_enem = pd.read_csv(endereco_dados, sep=';', encoding='UTF-8')
df_enem_uf = df_enem[['ESTADOS','Total']]



#exibindo as métricas
print(df_enem_uf)

