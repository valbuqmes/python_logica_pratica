#Dada uma lista de valores inteiros, crie um programa que percorra a lista e calcule
#separadamente a soma dos valores pares e a soma dos valores ímpares.
#• Defina a lista diretamente no código (ex: [3, 8, 15, 4, 7, 22, 11, 6]).
#• Percorra a lista com for e use if para classificar cada elemento.
#• Exiba a soma dos pares, a soma dos ímpares e a soma total.
def linas():
    print("---------------------------")
lista = [1,2,3,5,6,7,8,9,10]
soma_par = 0
soma_impar = 0
for numero in lista:
    if numero % 2 == 0:
        soma_par = soma_par + numero
        print("Soma pares: ", soma_par)

linas()

for numero in lista:
    if numero % 2 != 0:
        soma_impar = soma_impar + numero
        print("Soma impares: ", soma_impar)
    

