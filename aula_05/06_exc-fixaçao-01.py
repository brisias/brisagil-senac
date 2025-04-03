alune = []
media = []
situacao = ['APROVADO(A)','REPROVADO(A)','EM RECUPERAÇÃO']

for i in range(3):
    alune.append(input(f'Insira o nome do(a) aluno(a): ').upper())
    media.append(float(input(f'Insira a média dele(a): ')))

print("\n--------------")
print('')
for i in range (len(alune)):
    if media[i] >= 7:
        print(f'Aluno(a) {alune[i]}, foi {situacao[0]}: média {media[i]}')
    elif media[i] < 5:
        print(f'Aluno(a) {alune[i]}, foi {situacao[1]}:  média {media[i]}')
    else:
        print(f'Aluno(a) {alune[i]}, está {situacao[2]}: média {media[i]}')
