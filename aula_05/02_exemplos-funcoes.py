num = [10,2,3,5,6,20,50,77,4,15]

soma = sum(num)
maior = max(num)
menor = min(num)
media = sum(num) / len(num)

# padrão é ordem crescente
num.sort()
print(num)

# adicionando o reverse=true organiza em ordem decrescente
num.sort(reverse=True) 
print(num)

print(soma)
print(maior)
print(menor)
print(media)