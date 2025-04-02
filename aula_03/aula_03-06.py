# Entrada dos dados
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
n3 = int(input('Informe o terceiro valor: '))

# Processamento dos dados
if n1<=n2 and n1<=n3:
   if n2<=n1 and n2<=n3:
      if n3>n1 and n3>n2:
         print(f'{n3} é o maior valor')
      elif n3==n1 and n3==n2:
         print('todos os números são iguais')
   else: 
      print(f'{n2} é o maior valor')
else:
    print(f'{n1} é o maior valor')