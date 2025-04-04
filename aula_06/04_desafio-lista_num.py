# Crie um programa que:
# a- Peça ao usuário para digitar dez números inteiros e os armazene em uma lista.
# b- Exiba a lista completa.
# c- Exiba o maior e o menor número da lista.
# d- Exiba a soma e a média de todos os números
# --------------------------------------------------------------------- #

cont = 1 #contador
num = [] # lista dos números inteiros
for i in range(5):
    num.append(int(input(f'Informe o {cont}º valor inteiro:')))
    cont += 1

maior = max(num)
menor = min(num)
soma = sum(num)
media = sum(num) / len(num)

print(f'\nLista completa: {num}')
print(f'O maior número da lista: {maior}')
print(f'O menor número da lista: {menor}')
print(f'Soma de todos os valores: {soma}')
print(f'Média de todos os valores: {media:.1f}')