# entrada de dados
soma = 0
maior = 0

# processamento dos dados - estrutura de repetição
for i in range(5):
    n = int(input('Informe um valor inteiro: '))
    if n > maior:
        maior = n
    soma = soma + n

# saída de dados
print(f'A soma é {soma}.')
print(f'O maior valor encontrado foi {maior}.')