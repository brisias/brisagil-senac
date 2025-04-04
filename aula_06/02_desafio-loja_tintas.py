# Faça um programa para uma loja de tintas, que solicite o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 130,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o valor a ser pago.
# ------------------------------------------------------------------------------------------------------------------- #

import math
area = float(input('Bem-vindo(a) à calculadora de galões da Loja TutoTinta. Insira o valor da área em m² a ser pintada: '))

galoes_prt = ((area/3)/18)
galoes_int = math.ceil(galoes_prt)
preco = galoes_int * 130

if galoes_int > 1:
    print(f'\nVocê precisará de {galoes_int} galões da tinta escolhida, que custará R${preco:.0f},00')
else:
    print(f'\nVocê precisará de 1 galão da tinta escolhida, que custará R$130,00')