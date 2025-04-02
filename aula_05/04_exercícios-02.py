n = 1
num = []
pares = []
impares = []

for i in range(10):
    num.append(int(input(f'Informe o {n}º valor inteiro:')))
    n += 1
    if num[i] % 2 == 0:
        pares.append(num[i])
    else:
        impares.append(num[i])
        
print("\n--------------")
print(f'\nVocê informou {len(pares)} números pares: {pares}')
print(f'Você informou {len(impares)} números ímpares: {impares}')
print("\n--------------")

num.reverse() 
print('Lista em ordem reversa:')
print(num)
print("\n--------------")

num.sort()
print('Lista em ordem crescente:')
print(num)