notas = [81,44,92,64,36,70,96,26,84,54]
acima = []
abaixo = []
notas.sort()
print(f'As notas finais foram: {notas}')
for i in range(len(notas)):
    if notas[i] >= 70:
        acima.append(notas[i])        
    else:
        abaixo.append(notas[i])
print('\n------------------------------')
print('\nNotas acima da média:')
print(acima)
print('Notas abaixo da média:')
print(abaixo)