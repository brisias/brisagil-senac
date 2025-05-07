import pandas as pd

# 'def' é o comando que permite criar uma função para codificar ações dentro do código que podem ser usadas ao longo do projeto. "valor" poderia ser qualquer palavra,letra, etc., é uma variável exclusiva para a função que não deve ser reutilizada ao longo do código 

def formatar(valor):
    return "{:.2f}%".format(valor)

roubos_auto = pd.Series([100,90,80,120,110,90,70], index = ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom'])
furtos_auto = pd.Series([80,60,70,60,100,50,30], index = ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom'])
rec_auto = pd.Series([70,50,90,80,100,70,50], index = ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom'])

#processamento de dados:
soma = roubos_auto + furtos_auto
taxa_rec = ((rec_auto / roubos_auto)*100).apply(formatar)

print('A quantidade de roubos e furtos de automóveis por dia, nos últimos 7 dias, foi:')
print(soma)
print('\nAssim, a soma total de roubos e furtos de automóveis durante a semana, foi:')
print(soma.sum()) # somando todas os valores dentro da própria série
print('\nJá as taxas de recuperação de automóveis diárias, nos útimos 7 dias,  foram:')
print(taxa_rec)