frutas = ["maca", "banana", "cereja", "laranja"]

tamanho= len(frutas)

print(frutas)
print("Tamanho da lista: ",tamanho)
print("Maçâ tem: ",len(frutas[0]))
print("Banana tem: ",len(frutas[1]))
print("Cereja tem: ",len(frutas[2]))
print("Laranja tem: ",len(frutas[3]))

print("Imprimindo tmanho dos elementos usando lista: ")
for frutinhas in frutas:
    print("Tamanho de ", frutinhas, ": ", len(frutinhas))