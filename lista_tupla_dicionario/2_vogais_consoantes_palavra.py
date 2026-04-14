#Dada uma palavra lida com input(), crie um programa que conte quantas vogais e
#quantas consoantes ela possui.
#• Considere apenas letras (ignore espaços ou outros caracteres).
#• Use uma tupla para armazenar as vogais: vogais = ('a','e','i','o','u').
#• Exiba a palavra, a quantidade de vogais e a quantidade de consoantes.
vogais = ("a", "e", "i", "o", "u")

palavra = input("Digite um nome: ")

while not palavra.isalpha():
    palavra = input("Digite um nome: ")

print(palavra)
consoante = 0
vogal = 0
for letra in palavra:

    if letra not in vogais:
        consoante +=1
    if letra in vogais:
        vogal += 1

print("Quantidade de Vogais na Palavra: ", vogal)
print("Quantidade de Consoantes na Palavra: ", consoante)
    