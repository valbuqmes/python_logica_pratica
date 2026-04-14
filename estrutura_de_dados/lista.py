#lista é representada por []
#lista pode remover, editar


lista_vazia = list()
#ou lista_vazia = []
numeros = [0,27,12,7]
print("Imprimindo pelo ultimo indice da lista")
print(numeros[-1])
print(numeros[-2])
print(numeros[-3])
print(numeros[-4])
print("Imprimindo em ordem: ")
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])


#adicionar elemento no final
numeros.append(27)
print(numeros)
#remove o numero especificado da lista
numeros.remove(7)
print(numeros)
ultimo = numeros.pop()
print(numeros)
print(ultimo)

#retorna o indice do numero entre paratenses
posicao = numeros.index(27)
print(posicao)
