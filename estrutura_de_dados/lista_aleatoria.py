import random

num_objetos = int(input("Digite o tamanho da lista: "))

lista_aleatoria = []

#cria uma lista aleatoria com valores de 1 a 99
for i in range(num_objetos):
    lista_aleatoria.append(random.randint(1, 99))

print(lista_aleatoria)

#pega o meio da lista, so pode ser com impar
print(lista_aleatoria[len(lista_aleatoria)//2])

#imprime o ultimo numero da lista
print(lista_aleatoria[-1])

