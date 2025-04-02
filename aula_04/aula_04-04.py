for i in range(3):
    nome = input('Informe o nome do(a) aluno(a): ')
    nota_1 = float(input('Informe a nota da primeira avaliação: '))
    nota_2 = float(input('Informe a nota da segunda avaliação: '))

    media = (nota_1 + nota_2)/2

    if media >= 70:
        situacao = "APROVADO" # print(f'Parabéns {nome.title()}, com sua média {media:.2f}, você foi APROVADO')   
    elif media >= 30 and media < 70:
        situacao = "PARCIALMENTE APROVADO" # print(f'{nome.title()}, com sua média {media:.2f}, você foi PARCIALMENTE APROVADO')  
    else:
        situacao = "REPROVADO" # print(f'{nome.title()}, com sua média {media:.2f}, você foi REPROVADO')
    
    print(f'{nome.title()}, com sua média {media:.2f}, você foi {situacao}')