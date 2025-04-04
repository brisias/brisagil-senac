#Faça um programa que pergunte quanto um funcionário recebe por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) Quanto pagou ao IRRF.
# c) quanto pagou ao INSS.
# d) quanto pagou ao sindicato.
# e) o salário líquido.
# -------------------------------------------------------------------------------------------------------------------- #

valor_hora = float(input('Vamos calcular todas as partes do seu salário. Informe quanto você recebe por hora trabalhada em um mês: R$'))
qtd_horas = int(input('Agora informe quantas horas você trabalhou no mês: '))

pag_bruto = valor_hora * qtd_horas
valor_IRRF = pag_bruto * 11/100
valor_INSS = pag_bruto * 8/100
valor_sind = pag_bruto * 5/100

print(f'\nSeu salário bruto neste mês foi R${pag_bruto:.2f}')
print('Desse valor, foram descontados:')
print(f'Para o Imposto de renda: R${valor_IRRF:.2f};')
print(f'Para o INSS: R${valor_INSS:.2f};')
print(f'Para o Sindicato: R${valor_sind:.2f}.')
print(f'\nSeu salário líquido foi: R${pag_bruto * 76/100:.2f};')