# Entrada dos dados
n1 = int(input('Informe o dividendo: '))
n2 = int(input('Informe o divisor:'))
while n2 == 0:
    n2 = int(input('O divisor não pode ser igual a zero. Informe um novo valor: '))
print(f'O resultado da divisão entre os dois valores é {n1 / n2}')