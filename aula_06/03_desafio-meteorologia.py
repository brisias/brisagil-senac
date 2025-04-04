# O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem como a média delas.
# --------------------------------------------------------------------- #

temp = [] #lista das temperaturas
n = "S"

while n == "S":
    temp.append(float(input('Insira um valor de temperatura em graus Celcius: ')))
    n = input('Gostaria de inserir mais um valor? Digite S- SIM ou N- NÃO: ').upper()

maior = max(temp)
menor = min(temp)
soma = sum(temp)
media = sum(temp) / len(temp)

print(f'\nA menor temperatura informada foi {menor}°C.')
print(f'A maior temperatura informada foi {maior}°C.')
print(f'A média das temperaturas informadas foi {media}°C')