nomes = "João, José, Juliana"
nomes_lista = ["João","José","Juliana"]
lista_vazia = []
num = []

for i in range(5):
    num.append(int(input("Informe um valor inteiro:")))

for i in range(len(num)):
    print(f"O {num[i]} está na posição {i} da lista.")
print("-------------------")
print(num)
print("-------------------")
print(nomes)
print(nomes_lista[2])