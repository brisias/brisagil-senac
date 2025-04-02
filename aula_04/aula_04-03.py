# Entrada de dados
soma = 0
maior_idade = 0
menor_idade = 200

# Processamento dos dados - estrutura de repetição
for i in range(10):
    nome = input('Informe o nome da pessoa: ')
    idade = int(input('Informe a idade desta pessoa: '))

    if idade > maior_idade:
        maior_idade = idade
        maior_nome = nome

    if idade < menor_idade:
        menor_idade = idade
        menor_nome = nome

    soma = soma + idade

# Saída dos dados
print(f'A soma das idades foi {soma}.')
print(f'A média das idades foi {(soma / (i+1)):.2f}.')
print(f'A pessoa mais velha encontrada foi {maior_nome.title()}, com {maior_idade} anos.')
print(f'A pessoa mais nova encontrada foi {menor_nome.title()}, com {menor_idade} anos.')