import pandas as pd
serieA = pd.Series([104,25,33,47,5,14,73,324,90,116])
serieB = pd.Series([4,2,31,9,5,7,3,84,45,58])

#processamento de dados: operações matemáticas
soma = serieA+serieB
sub = serieA-serieB
mult = serieA*serieB
div = serieA/serieB

#ordenamento das séries:
soma_ord = soma.sort_values() #criando uma variáveis/séries específicas para a organização é possível acessar a ordem original dos dados ainda, caso seja necessário
sub_ord = sub.sort_values()
mult_ord = mult.sort_values()
div_ord = div.sort_values()

#exibição dos resultados:
print('Resultado da soma entre os valores das séries A e B:')
print(soma_ord)
print('\nResultado da subtração entre os valores das séries A e B:')
print(sub_ord)
print('\nResultado da razão entre os valores das séries A e B:')
print(mult_ord)
print('\nResultado da divisão entre os valores das séries A e B:')
print(div) #exibe os dados processados na ordem original

#se uma das séries for maior que a outra, na hora de realizar as operações matemáticas o código vai gerar um erro (NaN) de informação não encontrada