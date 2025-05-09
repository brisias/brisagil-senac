# Importando a biblioteca
import pandas as pd

def moeda(v):
    return "R$ {:.2f}".format(v)

# Criando a tabela vendedor
vendedores = [
    ['Maria',800,700,1000,900,1200,600,600],
    ['João',900,500,1100,1000,900,500,700],
    ['Manuel',700,600,900,1200,900,700,400]
]

# Criando as colunas da tabela vendedor
colunas = ['Nome','Seg','Ter','Qua','Qui','Sex','Sáb','Dom']

# Criando o DataFrame vendedor
df_vendedores = pd.DataFrame(vendedores,columns=colunas)

# Exibindo o DataFrame
print(df_vendedores.to_string(index=False))

# Criando as métricas
soma_seg = df_vendedores['Seg'].sum()
media_seg = df_vendedores['Seg'].mean()
menor_seg = df_vendedores['Seg'].min()
maior_seg = df_vendedores['Seg'].max()
nome_vend_seg = df_vendedores[df_vendedores['Seg'] == maior_seg]['Nome']

# Exibindo as métricas
print(f'Total em vendas na segunda-feira: {soma_seg}')
print(f'Média de vendas na segunda-feira: {media_seg}')
print(f'Menor valor entre as vendas na segunda-feira: {menor_seg}')
print(f'Maior valor entre as vendas na segunda-feira: {maior_seg}')
print(f'O vendedor responsável pela venda de maior valor: {nome_vend_seg}')