import pandas as pd

def moeda(v):
    return "R$ {:.2f}".format(v)

maria = pd.Series([800,700,1000,900,1200,600,600], index = ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom'])
joao = pd.Series([900,500,1100,1000,900,500,700], index = ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom'])
manuel = pd.Series([700,600,900,1200,900,700,400], index = ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom'])

print('\n--------------------------------------')
print('_V E N D E D O R A  M A R I A_')
print(f'\nVendas: \n{maria.apply(moeda)}')
print(f'\nTotal em vendas: R$ {maria.sum():.2f}')
print(f'Média em vendas: R$ {maria.mean():.2f}')
print(f'Maior valor vendido: R$ {maria.max():.2f}')
print(f'Menor valor vendido: R$ {maria.min():.2f}')

print('\n--------------------------------------')
print('_V E N D E D O R  J O A O_')
print(f'\nVendas: \n{joao.apply(moeda)}')
print(f'\nTotal em vendas: R$ {joao.sum():.2f}')
print(f'Média em vendas: R$ {joao.mean():.2f}')
print(f'Maior valor vendido: R$ {joao.max():.2f}')
print(f'Menor valor vendido: R$ {joao.min():.2f}')

print('\n--------------------------------------')
print('_V E N D E D O R  M A N U E L_')
print(f'\nVendas: \n{manuel.apply(moeda)}')
print(f'\nTotal em vendas: R$ {manuel.sum():.2f}')
print(f'Média em vendas: R$ {manuel.mean():.2f}')
print(f'Maior valor vendido: R$ {manuel.max():.2f}')
print(f'Menor valor vendido: R$ {manuel.min():.2f}')