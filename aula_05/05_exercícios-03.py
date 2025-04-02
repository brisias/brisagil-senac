gabarito = ['A','B','B','D','E']
resposta = []
a = 0 #número de acertos
e = 0 #número de erros
n = 1 #contagem de perguntas

for i in range(5):
    resposta.append(input(f'Insira a resposta da {n}ª questão: ').upper())
    n += 1
    if resposta[i] == gabarito[i]:
        a += 1
    else:
        e += 1

print("\n--------------")
print('\n As alternativas informadas foram:')
print(resposta)
print('\n As alternativas corretas são:')
print(gabarito)
print(f'\n Você acertou {a} e errou {e} questões.')