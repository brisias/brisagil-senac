# Entrada dos dados
n1 = int(input('Informe o dividendo: '))
marcador = 0
# Processamento e saída
while marcador == 0:
    n2 = int(input('Informe o divisor: '))
    if n2 == marcador:
        print('o divisor não pode ser igual a zero')
    else:
        marcador = n2
        print(f'O resultado da divisão entre os dois valores é {n1 / n2}')