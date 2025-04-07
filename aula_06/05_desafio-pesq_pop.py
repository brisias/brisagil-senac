# Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a qual coletaram os seguintes dados referentes a cada habitante para serem analisados:
# - sexo (masculino e feminino)
# - cor dos olhos (azuis, verdes ou castanhos)
# - cor dos cabelos (louros, castanhos, pretos)
# - idade
# Faça um programa que determine e escreva:
# a) a maior idade dos habitantes;
# b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
# c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros
# ---------------------------------------------------------------------------------------------- #

sexo = []
olhos = []
cabelos = []
idade = []
qtd_jovens_f = 0
qtd_galegos = 0

hab = int(input('Insira a quantidade de habitantes da região pesquisada: ')) #poderia inserir a cidade e puxar automaticamente de um banco de dados do IBGE, por exemplo, a população do município para determinar o tamanho do while (num futuro distante em que eu souber fazer isso).  
n = 0

while n < hab:
    n += 1
    sexo.append(input(f'\nRegistre o sexo do {n}º indivíduo. M - masculino ou F - feminino: ').upper())
    olhos.append(input(f'Agora, registre a cor dos olhos do {n}º indivíduo. A - azuis; V - verdes ou; C - castanhos: ').upper())
    cabelos.append(input(f'Registre também a cor dos cabelos do {n}º indivíduo. L - louros; C - castanhos ou; P - pretos: ').upper())
    idade.append(int(input(f'Por fim, insira a idade do {n}º indivíduo: ')))
    print()

    for i in range(hab):
        if sexo[i] == "F" and idade[i] >= 18 and idade[i] <= 35:
            qtd_jovens_f += 1
        if cabelos[i] == "L" and olhos[i] == "V":
            qtd_galegos += 1

maior = max(idade)

print(f'\nA maior idade encontrada na população pesquisada foi: {maior} anos.')
print(f'\nA quantidade de indivíduos do sexo feminino, entre 18 e 35 anos de idade, na população pesquisada, foi: {qtd_jovens_f} pessoa(s).')
print(f'\nJá a quantidade de indivíduos com cabelos louros e olhos verdes, foi de: {qtd_galegos} galego(s).')