nome = input('Olá, vamos verificar se você está apto a doar sangue hoje? Informe seu nome: ')
idade = int(input('Informe sua idade: '))
peso = float(input('Qual seu peso hoje? '))
sono = int(input('Quantas horas, aproximadamente, você dormiu na noite passada: '))

if idade < 16 or idade > 69:
    print(f'{nome.title()}, infelizmente, você não pode doar sangue hoje! É preciso ter entre 16 e 69 anos.')
elif peso <= 50:
    print(f'{nome.title()}, infelizmente, você não pode doar sangue hoje! É preciso ter mais de 50kg.')
elif sono < 6:
    print(f'{nome.title()}, infelizmente, você não pode doar sangue hoje! É preciso estar bem descansado(a), durma mais de 6h e volte outro dia!')
else:
    print(f'Oba, {nome.title()}, você está apto para doar sangue hoje! Siga para a próxima sala.')